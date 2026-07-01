# 기준 계약 문서 · 키즐링 리드 후속 이메일 자동화

> 구현 전에 합의해 고정하는 기준이다. 기준이 바뀌면 산출물보다 이 문서를 먼저 갱신하고, 중요한 변경은 `Decisionlog.md`에 남긴다.

## 기준 자료

- 최우선 발제: `docs/references/발제.md`
- 문제 패키지: `키즐링/problem.md`, `키즐링/CLAUDE.md`
- 필수 컨텍스트: `키즐링/context/company-info.md`, `키즐링/context/industry-news.md`
- 기존 파이프라인 참고: `키즐링/.claude/skills/analyze.md`, `insight.md`, `generate.md`, `review.md`
- 최종 제출 스킬 체인:
  - `.claude/skills/kizzling-followup/SKILL.md`
  - `.claude/skills/kizzling-analyze-leads/SKILL.md`
  - `.claude/skills/kizzling-message-strategy/SKILL.md`
  - `.claude/skills/kizzling-generate-emails/SKILL.md`
  - `.claude/skills/kizzling-campaign-plan/SKILL.md`
  - `.claude/skills/kizzling-visualize-campaign/SKILL.md`
  - `.claude/skills/kizzling-review-submit/SKILL.md`
  - `.claude/skills/kizzling-quality-audit/SKILL.md`

## 목표

Basic, Standard, Challenge 요구사항을 모두 구현한다.

- Basic: 리드별 개인화 이메일 초안 일괄 생성
- Standard: 새 CSV에도 재현 가능한 파이프라인 구성
- Challenge: 리드 패턴 기반 후속 캠페인 기획안 생성

## 입력

- 기본 입력 파일: `키즐링/data/leads_sample.csv`
- 필수 컬럼:
  - `lead_id`
  - `name`
  - `organization`
  - `org_type`
  - `title`
  - `email`
  - `consultation_note`
  - `interest_feature`
  - `follow_up_priority`
- 허용 직책: `원장`, `팀장`, `사업개발`
- 허용 관심 기능: `대회운영SaaS`, `콘텐츠안전필터`, `파트너십`
- 허용 우선순위: `상`, `중`, `하`

## 출력

### Basic 필수 출력

- 파일: `키즐링/output/email_drafts.csv` 또는 `키즐링/output/email_drafts.xlsx`
- 컬럼: `lead_id, subject, body, review_flag`
- `subject`: 직책별로 차별화된 제목
- `body`: 인사 → 상담언급 → 제품연결 → CTA 순서의 한국어 250~400자, 자연스러운 비즈니스 문체
- `review_flag`: `Y` 또는 `N`
- 제출 링크: 노션 페이지 또는 구글 시트 공개 링크. 접근 가능 여부를 제출 전 확인한다.
- 예외 처리 요약: 이메일 결측, 상담 메모 결측·모호, 중복 리드를 별도로 확인할 수 있게 남긴다.

### Standard 필수 출력

- 새 리드 CSV에도 동일 스키마로 `정제 → 직책 분기 → 초안 생성 → review_flag`가 재현되는 실행 절차 또는 파이프라인 문서
- 채택한 방식의 간단한 사용법. 최종 방식은 스크립트 의존 없이 `.claude/skills/kizzling-followup/SKILL.md`가 기능별 Skill을 순차 호출하는 스킬 체인 워크플로다.
- 위 파이프라인으로 생성한 이메일 초안 샘플 1부
- 직책별 소구점, CTA, 우선순위별 CTA 강도, review_flag 기준의 설계 근거
- 설계 근거는 “마케팅·영업 관점에서 무엇이 전환을 만드는가”를 기준으로 1~2줄 이상 설명한다.

### Challenge 필수 출력

- Standard 산출물 전체
- 리드 데이터에서 도출한 후속 캠페인 기획안 자동 생성 결과 샘플 1~2건
- 파일 예시: `키즐링/output/campaign_plan.md`
- 각 기획안 필수 항목:
  - 세그먼트 정의
  - 근거 리드 건수와 lead_id
  - 대표 상담 인용
  - 후속 시퀀스
  - 우선순위와 판단 근거
- 이메일 양식, review_flag 기준, 우선순위 판단 기준의 설계 근거

### 추가 출력

- 검수 리포트
- 예외 처리 요약
- 제출용 요약 문서

## 이메일 생성 규칙

각 이메일 본문은 다음 4요소를 순서대로 포함한다.

1. 맞춤 인사: 이름과 직책 호칭, 박람회 만남 감사
2. 부스 상담내용 언급: `consultation_note`의 구체적 내용 참조
3. 직책별 소구점과 키즐콘 기능 연결
4. 명확한 CTA 1개

직책별 기본 매핑:

| 직책 | 핵심 소구점 | 제품 연결 | CTA |
|---|---|---|---|
| 원장 | 원생 재능 발굴, 학부모 만족, 기관 브랜딩 | 대회 운영·콘텐츠 안전을 원생 효과로 연결 | 무료 데모 신청 |
| 팀장 | 도입 난이도, 운영 공수 절감, 기존 시스템 연동 | 접수·결제·심사·결과발표 자동화와 연동성 강조 | 기술 도입 미팅 |
| 사업개발 | 파트너십 수익 모델, 공동 마케팅, 기관 공급 계약 | 공동 공급·공동 마케팅·기관 공급으로 연결 | 파트너십 제안서 송부 |

직책별 제목도 서로 달라야 하며, 제목에는 해당 직책의 관심사가 드러나야 한다.

우선순위별 CTA 강도:

| follow_up_priority | CTA 강도 |
|---|---|
| 상 | 48시간 내 데모·미팅·제안서 등 즉시 행동 유도 |
| 중 | 편한 일정 조율과 자료 안내 중심 |
| 하 | 사례집·소개자료 등 장기 너처링 중심 |

## 예외 처리 기준

- 상담 메모 결측: `consultation_note`가 비어 있거나 `상담 메모 없음`이면 `review_flag = Y`
- 상담 메모 모호: 구체적 니즈가 파악되지 않으면 `review_flag = Y`
- 이메일 결측: `review_flag = Y`로 표시하고 이메일 발송 대상이 아니라 별도 후속 메모로 전환
- 중복 리드: lead_id만 다르고 동일한 리드는 한 건으로 처리하고, 제외된 lead_id와 기준 lead_id를 기록
- 내부 메모성 표현은 이메일 본문에 그대로 노출하지 않는다.

## 파이프라인 계약

기본 흐름:

1. `kizzling-analyze-leads`: CSV 구조, 분포, 결측, 모호, 중복 확인
2. `kizzling-message-strategy`: 컨텍스트 반영, 직책별 소구점, CTA, review_flag, 우선순위 기준 확정
3. `kizzling-generate-emails`: Basic/Standard 이메일 초안과 예외 메모 생성
4. `kizzling-campaign-plan`: 리드 패턴 분석 기반 Challenge 캠페인 기획안 자동 생성
5. `kizzling-visualize-campaign`: 캠페인 기획안을 정적 HTML 미리보기로 시각화
6. `kizzling-review-submit`: 채점 기준 기반 검수와 제출 요약
7. `kizzling-quality-audit`: 매 실행 사이클 마지막에 이메일·캠페인·시각화·금지 범위를 통합 검수

`kizzling-campaign-plan`, `kizzling-visualize-campaign`, `kizzling-quality-audit`은 기존 키즐링 커맨드에 없는 보강 스킬이다. `kizzling-campaign-plan`은 Challenge 요구사항인 “후속 캠페인 기획안까지 자동 생성”을 위해, `kizzling-visualize-campaign`과 `kizzling-quality-audit`은 발제 요구사항 이상의 완성도(시각화, 통합 품질 QA)를 위해 추가했다.

Standard 검증 시에는 `kizzling-campaign-plan` 이전까지의 흐름만으로도 `email_drafts.csv/.xlsx`, 사용법, 이메일 초안 샘플 1부가 재현되어야 한다. 캠페인 시각화가 필요 없으면 `kizzling-visualize-campaign`을 건너뛸 수 있지만, `kizzling-quality-audit`은 실행 사이클마다 항상 마지막 단계로 수행한다. 최종 제출 기준에서는 별도 `py` 파일이나 assets 없이 `.claude/skills/kizzling-followup/SKILL.md`와 기능별 `SKILL.md` 체인만으로 이 절차를 설명하고 실행할 수 있어야 한다.

## 캠페인 자동 생성 규칙

`kizzling-campaign-plan` 단계는 `kizzling-analyze-leads`의 분포와 `kizzling-message-strategy`의 전략 기준을 입력으로 받아 캠페인 기획안 샘플 1~2건을 생성한다.

각 캠페인 기획안은 다음 형식을 따른다.

| 항목 | 내용 |
|---|---|
| 세그먼트 정의 | org_type, title, interest_feature, follow_up_priority 조합으로 정의 |
| 근거 리드 | 해당 lead_id 목록, 건수, 대표 상담 인용 |
| 핵심 인사이트 | 왜 이 세그먼트를 묶었는지, 어떤 전환 가능성이 있는지 |
| 후속 시퀀스 | Day0 이메일, Day2~3 보강 자료, Day7 미팅/제안 후속 등 |
| 우선순위 | follow_up_priority 입력값, 리드 수, 골든타임, 실행 용이성을 근거로 판단 |
| 담당자 액션 | 영업·마케팅 담당자가 바로 실행할 다음 행동 |

금지:

- follow_up_priority를 새 점수로 재계산하지 않는다.
- 실제 발송, CRM 등록, 외부 자동화를 수행하지 않는다.
- 근거 리드 없이 캠페인 아이디어만 제안하지 않는다.

## 완료 기준

- Basic, Standard, Challenge 필수 항목이 모두 산출물에 반영된다.
- `email_drafts.csv/.xlsx`가 필수 컬럼을 가진다.
- 본문 250~400자와 개인화 4요소의 순서를 충족한다.
- 노션 또는 구글 시트 공개 링크 제출 준비와 접근 확인 기준이 문서화된다.
- review_flag, 이메일 결측, 중복 처리가 검수된다.
- 캠페인 기획안 자동 생성 샘플 1~2건이 실제 리드 근거와 업계 맥락을 포함한다.
- Standard 파이프라인 사용법, 동일 스키마 재현 기준, 파이프라인 생성 이메일 샘플 1부가 포함된다.
- 제출 전 검수 리포트가 작성된다.

## 안전장치

- 실제 이메일 발송은 하지 않는다.
- CRM 연동은 하지 않는다.
- 리드 스코어링을 하지 않는다. `follow_up_priority`는 입력값 그대로 CTA 강도 조절에만 사용한다.
- 제공된 더미 데이터만 사용한다.
- 수신 동의와 개인정보 위험은 검수 리포트 또는 제출 요약에 주의 문구로 남긴다.
