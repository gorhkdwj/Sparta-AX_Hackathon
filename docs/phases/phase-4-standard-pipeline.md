# Phase 4 · Standard 재현 파이프라인 구성

## 목표

새 리드 CSV에도 동일 품질로 `정제 → 직책 분기 → 초안 생성 → review_flag`가 재현되는 파이프라인을 구성하고, 사용법과 이메일 초안 샘플 1부를 제출 가능하게 만든다.

## 입력 자료

- Phase 1 데이터 분석 기준
- Phase 2 메시지 전략
- Phase 3 Basic 산출물
- `.claude/skills/kizzling-followup/SKILL.md`
- `.claude/skills/kizzling-analyze-leads/SKILL.md`
- `.claude/skills/kizzling-message-strategy/SKILL.md`
- `.claude/skills/kizzling-generate-emails/SKILL.md`
- `.claude/skills/kizzling-review-submit/SKILL.md`
- 제공 참고 자료: `키즐링/.claude/skills/analyze.md`, `insight.md`, `generate.md`, `review.md`

## 수행 계획

1. Standard 단독 흐름을 명확히 한다.
   - `kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails → kizzling-review-submit → kizzling-quality-audit`
2. 전체 제출 흐름과 구분한다.
   - `kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails → kizzling-campaign-plan → kizzling-visualize-campaign → kizzling-review-submit → kizzling-quality-audit`
3. 최종 구현 방식을 기능별 Skill 체인으로 고정한다.
4. 새 CSV 입력 조건을 정의한다.
   - 동일 필수 컬럼 9개
   - 동일 허용 값 범위
   - 결측·모호·중복 예외 처리
5. 파이프라인 사용법을 작성한다.
6. 파이프라인으로 생성한 이메일 초안 샘플 1부를 분리한다.
7. 직책별 소구점, CTA, 우선순위별 강도, review_flag 기준의 설계 근거를 1~2줄 이상 작성한다.

## 산출물

- `키즐링/output/pipeline-usage.md`
- `키즐링/output/email_draft_sample.md`
- `키즐링/output/standard_validation_summary.md`
- `.claude/skills/kizzling-followup/SKILL.md`
- `.claude/skills/kizzling-analyze-leads/SKILL.md`
- `.claude/skills/kizzling-message-strategy/SKILL.md`
- `.claude/skills/kizzling-generate-emails/SKILL.md`
- `.claude/skills/kizzling-review-submit/SKILL.md`

## 구현 방식

- 채택 방식: 기능별 Skill 체인 + 기존 슬래시 커맨드 문서 흐름 병행
- Standard 단독 흐름: `kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails → kizzling-review-submit → kizzling-quality-audit`
- 전체 제출 흐름: `kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails → kizzling-campaign-plan → kizzling-visualize-campaign → kizzling-review-submit → kizzling-quality-audit`
- 최종 실행 방식: `.claude/skills/kizzling-followup/SKILL.md`가 목표 레벨에 맞춰 기능별 스킬을 순차 호출한다.
- 개발 검증 보조: `키즐링/scripts/generate_basic_email_drafts.py`는 로컬 산출물 생성 검증에 사용했지만, 최종 제출 파이프라인의 필수 의존성으로 두지 않는다.
- 새 CSV 적용 방식: 동일 스키마 CSV를 스킬 입력으로 제공한다.

## 실행 결과

- 출력 파일: `키즐링/output/email_drafts.csv`
- 출력 행 수: 49
- 본문 길이 범위: 250~297자
- `review_flag = Y`: L009, L012, L015, L033, L046
- 중복 제외: L050. L039를 대표 행으로 유지.
- 이메일 초안 샘플: `키즐링/output/email_draft_sample.md`
- 최종 스킬 체인: `.claude/skills/kizzling-followup/SKILL.md` 및 기능별 `kizzling-*` 스킬

## 자동화된 처리 기준

- 필수 컬럼 9개가 없으면 실행을 중단한다.
- 이메일 결측은 `review_flag = Y`로 처리하고 제목에 `[검수 필요]`를 붙인다.
- 상담 메모가 비어 있거나 `상담 메모 없음`, `없음`, `미기재`이면 `review_flag = Y`로 처리한다.
- 상담 메모에 `애매`, `모호`, `구체적 니즈 파악 안 됨` 등 모호 표현이 있으면 `review_flag = Y`로 처리한다.
- 이름, 조직, 직책, 이메일, 상담 메모, 관심 기능이 동일한 리드는 첫 lead_id만 유지하고 이후 lead_id는 제외한다.
- 출력 스키마는 Basic과 동일하게 `lead_id`, `subject`, `body`, `review_flag`로 고정한다.

## 설계 근거

- 원장 리드는 원생 재능 발굴, 학부모 만족, 기관 브랜딩이 전환 동기이므로 무료 데모 CTA를 사용한다.
- 팀장 리드는 도입 난이도, 운영 공수 절감, 기존 시스템 연동이 의사결정 병목이므로 기술 도입 미팅 CTA를 사용한다.
- 사업개발 리드는 수익 모델, 공동 마케팅, 기관 공급 계약이 전환 동기이므로 파트너십 제안서 송부 CTA를 사용한다.
- `follow_up_priority = 상`은 48시간 내 즉시 행동을 유도하고, `중`은 일정 조율, `하`는 자료 기반 장기 너처링으로 압박을 낮춘다.
- `review_flag`는 데이터 결측·모호·연락처 누락처럼 자동화가 과도하게 단정하기 쉬운 지점을 사람이 보강하게 만드는 Human-in-the-loop 장치다.

## 완료 기준

- 새 CSV 입력 시 같은 절차로 이메일 초안과 review_flag를 만들 수 있다.
- 사용자가 파이프라인 실행 순서를 이해할 수 있다.
- 파이프라인 생성 이메일 초안 샘플 1부가 있다.
- 마케팅·영업 관점의 설계 근거가 문서화됐다.

## 검증 기준

- 발제의 Standard 필수 3항목을 모두 충족한다.
- `validation-plan.md`의 Standard 검증 항목을 통과한다.
- Basic 산출물과 동일한 출력 스키마를 유지한다.

## 검증 결과

- 새 리드 CSV 적용 절차 문서화: 통과
- Standard 단독 흐름과 Challenge 포함 흐름 구분: 통과
- `정제 → 직책 분기 → 초안 생성 → review_flag` 재현 기준: 통과
- 채택 방식 사용법: 통과
- 파이프라인 생성 이메일 초안 샘플 1부: 통과
- 마케팅·영업 관점 설계 근거: 통과
- Basic 출력 스키마 유지: 통과

## 다음 Phase 전달물

- 재현 파이프라인
- 파이프라인 사용법
- 이메일 초안 샘플 1부
- 캠페인 자동 생성 단계에 넘길 분석·전략 기준

## 리스크와 대응

- 리스크: 파이프라인이 실제로는 1회성 설명에 그칠 수 있음.
- 대응: 입력, 처리, 출력, 예외, 검수 단계를 기능별 Skill 체인 순서로 작성하고 별도 코드 의존 없이 재현 가능하게 한다.

## 상태

- 완료: Standard 재현 파이프라인 문서화와 기능별 Skill 체인 구조화
- 다음 단계: Phase 5 Challenge 캠페인 기획안 자동 생성
