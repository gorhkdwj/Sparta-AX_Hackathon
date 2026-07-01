---
name: kizzling-generate-emails
description: 키즐링 개인화 한국어 후속 이메일 초안과 Basic/Standard 산출물을 생성한다. 리드 분석과 메시지 전략 이후 email_drafts.csv, 예외 요약, review_flag 처리, Standard 파이프라인 사용법, 파이프라인 생성 이메일 샘플 1부가 필요할 때 사용한다. 스크립트나 외부 assets에 의존하지 않는다.
---

# 키즐링 이메일 초안 생성

리드 CSV, 리드 분석 handoff, 메시지 전략 handoff를 바탕으로 Basic 이메일 초안 표와 Standard 파이프라인 산출물을 만든다.

## 출력 스키마

`email_drafts.csv`는 정확히 다음 컬럼만 가져야 한다.

`lead_id`, `subject`, `body`, `review_flag`

제출용 CSV에는 추가 컬럼을 넣지 않는다.

## 본문 규칙

각 본문은 다음 기준을 만족해야 한다.

- 한국어로 작성한다.
- 자연스러운 비즈니스 톤을 사용한다.
- 250~400자 범위를 지킨다.
- 맞춤 인사 → 상담내용 언급 → 키즐링 제품 연결 → CTA 1개 순서를 따른다.

`review_flag = Y`인 경우:

- 구체적인 상담 내용을 지어내지 않는다.
- 상담 언급을 일반화한다.
- `review_flag`를 `Y`로 유지한다.
- 이메일 결측 리드는 발송 준비 완료 이메일이 아니라 연락처 확인용 후속 메모로 작성한다.

## 생성 절차

1. 중복 리드를 기록한 뒤 제외한다.
2. 직책별 제목을 생성한다.
3. 직책 전략과 `interest_feature`를 반영해 본문을 생성한다.
4. `follow_up_priority`에 따라 CTA 강도를 조절한다.
5. `review_flag`를 설정한다.
6. 본문 길이와 4요소 순서를 검증한다.

## 필수 산출물

다음 내용을 생성한다.

- `email_drafts.csv` 내용
- `basic_exception_summary.md` 내용
- 스킬 전용 파이프라인을 설명하는 `pipeline-usage.md` 내용
- 대표 초안 1부를 담은 `email_draft_sample.md` 내용
- `standard_validation_summary.md` 내용

## pipeline-usage.md 필수 문구

최종 Standard 파이프라인은 Python이나 스크립트 필수 의존성이 아니라 Skill 워크플로임을 명시한다.

```text
kizzling-analyze-leads
  -> kizzling-message-strategy
  -> kizzling-generate-emails
  -> kizzling-review-submit
```

Challenge는 다음 흐름을 사용한다.

```text
kizzling-analyze-leads
  -> kizzling-message-strategy
  -> kizzling-generate-emails
  -> kizzling-campaign-plan
  -> kizzling-review-submit
```

## 전달

이메일 초안, 예외 요약, Standard 검증 요약을 다음 스킬로 넘긴다.

- Challenge가 요청된 경우: `kizzling-campaign-plan`
- 최종 검수만 필요한 경우: `kizzling-review-submit`
