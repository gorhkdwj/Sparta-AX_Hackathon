---
name: kizzling-quality-audit
description: 키즐링 산출물의 최종 품질 QA를 수행한다. 이메일 초안만 생성했거나 캠페인 기획안, HTML 시각화까지 생성한 뒤 매 실행 사이클 마지막에 사용한다. 필수 컬럼, 본문 길이, review_flag, 중복 처리, 캠페인 근거, 시각화 산출물, 금지 범위, 제출 폴더 구조를 검수한다.
---

# 키즐링 품질 QA

스킬 실행 사이클의 마지막 단계에서 산출물을 검수한다. 이메일 초안만 만든 경우에도 실행하고, 캠페인 기획안이나 HTML 시각화가 있으면 해당 산출물까지 함께 검수한다.

## 입력

가능한 산출물을 모두 확인한다.

- `email_drafts.csv`
- `basic_exception_summary.md`
- `pipeline-usage.md`
- `email_draft_sample.md`
- `standard_validation_summary.md`
- `campaign_plan.md`
- `campaign_plan_preview.html`
- `public_link_prep.md`
- `submission-summary.md`

## Basic QA

다음을 확인한다.

- `email_drafts.csv` 컬럼이 `lead_id`, `subject`, `body`, `review_flag`만 있는지
- 본문이 한국어 250~400자인지
- 인사 → 상담언급 → 제품연결 → CTA 순서가 유지되는지
- 직책별 제목과 CTA가 차별화되는지
- 이메일 결측, 상담 메모 결측·모호 리드가 `review_flag = Y`인지
- 중복 제외 리드가 문서화됐는지

## Standard QA

다음을 확인한다.

- Skill 체인 사용법이 있는지
- 새 CSV에 같은 스키마로 적용 가능하다고 설명하는지
- 파이프라인 생성 이메일 샘플 1부가 있는지
- 스크립트, 외부 assets, API가 최종 필수 의존성이 아닌지

## Challenge QA

캠페인 기획안이 있으면 다음을 확인한다.

- 캠페인 샘플이 1~2건인지
- 세그먼트 정의, 근거 리드, 대표 인용, 후속 시퀀스, 우선순위, 담당자 액션이 있는지
- 우선순위가 새 점수 산출이 아니라 제공된 `follow_up_priority`와 리드 근거로 설명되는지

## 시각화 QA

`campaign_plan_preview.html`이 있으면 다음을 확인한다.

- 캠페인 세그먼트와 후속 시퀀스가 시각적으로 구분되는지
- `review_flag` 또는 사람 검수 필요 리드가 눈에 띄게 표시되는지
- 외부 CDN, 외부 이미지, 추적 스크립트, API 호출이 없는지
- 실제 발송, CRM 연결, 리드 점수 산출 기능이 없는지

## 금지 범위 QA

다음을 확인한다.

- 실제 이메일 발송 없음
- SMTP/Gmail API 없음
- CRM 연동 없음
- 다국어 이메일 없음
- 제공된 `follow_up_priority` 외 리드 스코어링 없음
- API 키, `.env`, 토큰 없음

## 출력

다음 구조로 `quality_audit_report.md` 내용을 생성한다.

```text
# 품질 QA 리포트

## 1. 실행 범위
## 2. Basic QA
## 3. Standard QA
## 4. Challenge QA
## 5. 시각화 QA
## 6. 금지 범위 QA
## 7. 남은 미검증 범위
## 8. 최종 판정
```
