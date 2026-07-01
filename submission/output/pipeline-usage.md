# Standard Pipeline Usage

새 리드 CSV에도 같은 방식으로 `정제 → 직책 분기 → 초안 생성 → review_flag`를 재현하기 위한 사용법입니다.

## 입력 조건

- 필수 컬럼: `lead_id`, `name`, `organization`, `org_type`, `title`, `email`, `consultation_note`, `interest_feature`, `follow_up_priority`
- 허용 직책: `원장`, `팀장`, `사업개발`
- 허용 관심 기능: `대회운영SaaS`, `콘텐츠안전필터`, `파트너십`
- 허용 우선순위: `상`, `중`, `하`

## Standard 단독 흐름

1. `kizzling-analyze-leads`: CSV 구조, 분포, 결측, 모호, 중복을 확인한다.
2. `kizzling-message-strategy`: 직책별 소구점, CTA, 우선순위별 CTA 강도, review_flag 기준을 확정한다.
3. `kizzling-generate-emails`: 이메일 초안, 예외 요약, Standard 샘플을 생성한다.
4. `kizzling-review-submit`: 생성 결과를 검수한다.
5. `kizzling-quality-audit`: 최종 품질 QA를 수행한다.

## 최종 실행 방식

최종 제출 파이프라인은 별도 `py`, assets, 외부 API 없이 `.claude/skills/kizzling-followup/SKILL.md`가 기능별 Skill을 호출하는 워크플로다.

사용자는 동일 스키마 CSV를 스킬 입력으로 제공하고, 스킬은 아래 순서로 산출물을 만든다.

```text
CSV 분석
  -> 키즐링 컨텍스트 반영
  -> 직책별 메시지 전략 확정
  -> email_drafts.csv 생성
  -> 예외 요약 생성
  -> 검수·QA
```

실제 스킬 체인은 다음과 같다.

```text
kizzling-analyze-leads
  -> kizzling-message-strategy
  -> kizzling-generate-emails
  -> kizzling-review-submit
  -> kizzling-quality-audit
```

Challenge까지 포함할 때는 다음 단계를 추가한다.

```text
kizzling-analyze-leads
  -> kizzling-message-strategy
  -> kizzling-generate-emails
  -> kizzling-campaign-plan
  -> kizzling-visualize-campaign
  -> kizzling-review-submit
  -> kizzling-quality-audit
```

개발 과정에서 사용한 로컬 검증 보조 스크립트는 최종 제출 패키지에 포함하지 않았으며, 최종 제출 파이프라인의 필수 의존성이 아니다.

## 출력

- `output/email_drafts.csv`: Basic/Standard 공통 이메일 초안
- `output/basic_exception_summary.md`: 이메일 결측, 상담 메모 결측·모호, 중복 제외 요약
- `output/email_draft_sample.md`: 파이프라인 생성 이메일 초안 샘플 1부
- `output/public_link_prep.md`: 공개 링크 제출 준비 메모

## 자동 처리 기준

- 이메일 결측: `review_flag = Y`, 제목에 `[검수 필요]` 표시, 본문은 연락처 확인 메모로 작성한다.
- 상담 메모 결측: 빈 값, `상담 메모 없음`, `없음`, `미기재`는 `review_flag = Y`로 처리한다.
- 상담 메모 모호: `애매`, `모호`, `구체적 니즈 파악 안 됨` 등은 `review_flag = Y`로 처리한다.
- 중복 리드: 이름, 조직, 직책, 이메일, 상담 메모, 관심 기능이 동일하면 첫 lead_id만 유지하고 이후 lead_id는 제외한다.

## 설계 근거

- 원장은 원생 재능 발굴, 학부모 만족, 기관 브랜딩을 전환 동기로 보므로 무료 데모 CTA가 적합하다.
- 팀장은 도입 난이도와 운영 공수 절감이 의사결정의 병목이므로 기술 도입 미팅 CTA가 적합하다.
- 사업개발은 공동 공급, 공동 마케팅, 수익 모델이 전환 동기이므로 파트너십 제안서 CTA가 적합하다.
- 우선순위 `상`은 48시간 내 행동을 유도하고, `중`은 일정 조율, `하`는 소개자료 중심으로 낮은 압박의 너처링을 적용한다.
- `review_flag`는 자동화가 오판하기 쉬운 데이터 품질 이슈를 사람이 보강하게 만드는 장치다.

## 전체 제출 흐름과의 구분

- Standard 단독 흐름: `kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails → kizzling-review-submit`
- Challenge 포함 흐름: `kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails → kizzling-campaign-plan → kizzling-visualize-campaign → kizzling-review-submit`
