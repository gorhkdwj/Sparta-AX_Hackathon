# CLAUDE.md · Sparta_AX_Project 작업 헌법

이 문서는 이 프로젝트에서 AI 협업 에이전트가 매번 따라야 하는 기준이다. 현재 프로젝트의 최우선 목표는 **키즐링 박람회 리드 맞춤 후속 이메일 자동화 과제의 Basic, Standard, Challenge 요구사항을 모두 충족하고 그 이상의 완성도를 구현하는 것**이다.

## 0. 프로젝트 정보

- 프로젝트 이름: Sparta_AX_Project (스파르타 AX 해커톤 제출용)
- 주제: 키즐링 박람회 리드 맞춤 후속 이메일 자동화
- 최우선 기준: `docs/references/발제.md`, `키즐링/problem.md`, `키즐링/CLAUDE.md`
- 필수 컨텍스트: `키즐링/context/company-info.md`, `키즐링/context/industry-news.md`
- 목표 레벨: Basic + Standard + Challenge 전 요구사항 충족, 추가 완성도 강화
- 핵심 산출물:
  - `키즐링/output/email_drafts.csv` 또는 `.xlsx`
  - `.claude/skills/kizzling-followup/SKILL.md`와 기능별 `kizzling-*` 스킬 체인
  - 파이프라인으로 생성한 이메일 초안 샘플 1부
  - 자동 생성 후속 캠페인 기획안 샘플 1~2건
  - 캠페인 기획안 HTML 미리보기
  - 품질 QA 리포트
  - 검수 리포트와 제출용 요약
- 금지 범위: 실제 이메일 발송, CRM 연동, 다국어 이메일, 리드 스코어링, API 키·외부 발송 연동

## 1. 대화와 보고 방식

- 결론을 먼저, 근거와 세부는 뒤에 둔다.
- 기술 용어는 처음 등장할 때 한 줄로 설명한다.
- 실행하거나 확인하지 않은 것을 완료라고 말하지 않는다.
- 불확실하면 단정하지 말고 `확인 필요`로 표시한다.
- 사용자가 정해야 할 기획 판단은 먼저 묻고, 파일과 데이터로 확인 가능한 사실은 직접 확인한다.

## 2. 작업 시작 전 확인

- 현재 폴더 구조와 기존 변경사항을 먼저 확인한다.
- 기존 파일과 사용자 변경사항을 덮어쓰지 않는다.
- 발제문서와 키즐링 하위 자료를 먼저 읽고, 그 기준에 맞춰 계획과 구현을 진행한다.
- 삭제된 구 제출가이드는 잘못된 안내로 보며 다시 참조하지 않는다.

## 3. 파일 구조 원칙

- 루트 문서는 프로젝트 운영과 계획을 관리한다.
- 실제 과제 자료와 산출물은 `키즐링/` 하위에 둔다.
- 주요 입력: `키즐링/data/leads_sample.csv`
- 필수 맥락: `키즐링/context/company-info.md`, `키즐링/context/industry-news.md`
- 최종 스킬 체인:
  - `.claude/skills/kizzling-followup/SKILL.md`
  - `.claude/skills/kizzling-analyze-leads/SKILL.md`
  - `.claude/skills/kizzling-message-strategy/SKILL.md`
  - `.claude/skills/kizzling-generate-emails/SKILL.md`
  - `.claude/skills/kizzling-campaign-plan/SKILL.md`
  - `.claude/skills/kizzling-visualize-campaign/SKILL.md`
  - `.claude/skills/kizzling-review-submit/SKILL.md`
  - `.claude/skills/kizzling-quality-audit/SKILL.md`
- 제공 커맨드 참고: `키즐링/.claude/skills/analyze.md`, `insight.md`, `generate.md`, `review.md`
- 제출 산출물: `키즐링/output/`
- 임시·로컬 실행 결과는 Git 포함 여부를 확인하고, 불필요한 결과물은 커밋하지 않는다.

## 4. 구현 원칙

- Basic, Standard, Challenge를 누락 없이 모두 만족시킨다.
- 작은 성공 단위부터 진행하되, 최종 목적은 Challenge 이상의 완성도다.
- 기본 파이프라인은 기능별 스킬 체인으로 설계한다:
  - `kizzling-analyze-leads` → `kizzling-message-strategy` → `kizzling-generate-emails` → `kizzling-campaign-plan` → `kizzling-visualize-campaign` → `kizzling-review-submit` → `kizzling-quality-audit`
- Standard 검증 흐름은 `kizzling-campaign-plan` 이전까지의 체인으로 동일 스키마 이메일 초안을 재생성한다.
- `kizzling-campaign-plan`은 Challenge 요구사항을 충족하기 위해 캠페인 기획안 샘플 1~2건을 산출한다.
- `kizzling-visualize-campaign`은 캠페인 기획안을 정적 HTML로 시각화해 추가 완성도를 보여준다.
- `kizzling-quality-audit`은 이메일 생성만 했거나 캠페인/시각화까지 진행했거나 관계없이 매 실행 사이클 마지막에 수행한다.
- 각 단계는 왜 필요한가, 이전 단계와 연결, 다음 단계 전달물, 완료 조건, 검증 방법, 실패 시 중단점을 명확히 한다.

## 5. 기준 계약 문서 원칙

- 구현 전 `docs/requirements-contract.md`에 입력, 출력, 절차, 완료 기준, 안전장치를 고정한다.
- 같은 기준이 문서마다 다르게 정의되지 않게 한다.
- 기준이 바뀌면 구현보다 계약 문서를 먼저 갱신하고, 중요한 변경은 `Decisionlog.md`에 남긴다.

## 6. Basic 요구사항

- `키즐링/data/leads_sample.csv` 50건을 분석한다.
- `email_drafts.csv` 또는 `.xlsx`를 생성한다.
- 필수 컬럼은 `lead_id, subject, body, review_flag`다.
- 본문은 한국어 250~400자이며 다음 4요소를 포함한다:
  - 맞춤 인사
  - 부스 상담내용 언급
  - 직책별 소구점과 키즐콘 기능 연결
  - 명확한 CTA 1개
- 본문 4요소는 인사 → 상담언급 → 제품연결 → CTA 순서를 따른다.
- 원장, 팀장, 사업개발의 제목, 소구점, CTA를 서로 다르게 작성한다.
- CTA는 원장=무료 데모 신청, 팀장=기술 도입 미팅, 사업개발=파트너십 제안서 송부를 기본값으로 한다.
- 상담 메모 결측·모호 리드는 `review_flag = Y`로 처리한다.
- 이메일 없는 리드는 `review_flag = Y`로 표시하고 발송 불가 별도 후속 메모로 전환한다.
- 완전 중복 리드는 한 건으로 처리하고 기준 lead_id와 제외 lead_id를 남긴다.
- 노션 또는 구글 시트 공개 링크 제출과 접근 가능 여부 확인을 준비한다.

## 7. Standard 요구사항

- 새 리드 CSV에도 동일 품질로 동작하는 재현 파이프라인을 만든다.
- `정제 → 직책 분기 → 초안 생성 → review_flag` 흐름이 기능별 스킬 체인으로 반복 가능해야 한다.
- Challenge 포함 시 `캠페인 기획안 생성 → 검수`까지 이어진다.
- Standard 검증에서는 `kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails → kizzling-review-submit → kizzling-quality-audit` 흐름으로 동일 스키마 이메일 초안이 재생성되고 QA되어야 한다.
- 직책별 소구점, CTA, 우선순위별 CTA 강도, review_flag 기준을 직접 설계하고 근거를 문서화한다.
- 설계 근거는 마케팅·영업 관점에서 무엇이 전환을 만드는지 1~2줄 이상 설명한다.
- 파이프라인 사용법과 파이프라인으로 생성한 이메일 초안 샘플 1부를 남긴다.
- 별도 `py`, assets, 외부 API는 최종 필수 의존성으로 두지 않는다.

## 8. Challenge 요구사항

- 리드 데이터 패턴 기반 후속 캠페인 기획안을 파이프라인에서 자동 생성한다.
- 자동 생성된 캠페인 기획안 샘플 1~2건을 제출물로 남긴다.
- 각 기획안에는 세그먼트 정의, 근거 리드, 대표 상담 인용, 후속 시퀀스, 우선순위를 포함한다.
- `industry-news.md`의 48시간 골든타임, 개인화 효과, Human-in-the-loop, 데이터 품질 이슈를 근거로 연결한다.
- 이메일 양식, review_flag 기준, 우선순위 판단 기준을 직접 설계하고 `키즐링/decisions.md` 또는 루트 `Decisionlog.md`에 남긴다.

## 9. 검증 원칙

- 검증하지 못한 부분은 숨기지 않고 `미검증 범위`로 보고한다.
- 최종 검증은 발제 채점표 기준으로 한다:
  - 직책별 차별화
  - 개인화 4요소
  - 본문 250~400자
  - review_flag 정확도
  - 이메일 결측과 중복 처리
  - 파이프라인 재현성
  - 캠페인 기획안의 근거와 실행 가능성
- 실제 이메일 발송, CRM 연동, 리드 스코어링은 검증 대상이 아니라 금지 범위다.

## 10. 보안·개인정보·비밀정보 원칙

- API 키, 비밀번호, 토큰, 세션 쿠키, 실제 고객정보, 실제 계좌정보, 민감 내부정보를 코드·문서·로그·테스트 데이터에 넣지 않는다.
- 제공된 더미 데이터만 사용한다.
- 이메일 실제 발송은 하지 않는다. 초안은 사람이 검토 후 발송한다.
- 수신 동의와 개인정보 관련 위험은 `industry-news.md` 기준으로 주의 문구를 남긴다.

## 11. 문서화 원칙

- README와 계획 문서에는 실제 구현했거나 이번 목표에 포함된 기능만 쓴다.
- 발제문서, 기준 계약 문서, 구현 계획, 검증 계획, README, Worklog, Decisionlog가 서로 모순되지 않게 관리한다.
- 외부 자료를 사용할 때는 URL, 제목, 확인일, 적용 범위를 기록한다. 로컬 제공 자료의 통계는 “제공 컨텍스트 기준”으로 표기한다.

## 12. Git 원칙

- 주요 단계가 끝날 때마다 변경 파일을 확인하고, 불필요한 파일과 비밀정보를 제외한다.
- 검증 가능한 단계에서는 검증 후 커밋·푸시한다.
- 현재 사용자 변경사항은 되돌리지 않는다.

## 13. 로그 기록 규칙

### Worklog.md

주요 사용자 요청이 끝날 때마다 기록한다.

```
### W-001 · 작업 제목
**요청** / **수행 작업** / **변경 파일** / **검증**(미실행 시 사유) / **판단 근거** / **결과**(완료·남은 작업)
```

### Decisionlog.md

방향을 바꾸는 결정만 기록한다.

```
### D-001 · 결정 제목
**상황** / **검토한 선택지** / **결정** / **근거** / **영향** / **재검토 조건**
```

### Troubleshootinglog.md

실제 오류, 실패, 환경 문제, 검증 실패, 설계 충돌이 발생하면 기록한다.

```
### T-001 · 문제 제목
**발생 상황** / **증상** / **확인된 원인**(+불확실점) / **조치**(+최종 해결) / **재발 방지**
```

## 14. 완료 보고 기준

작업 완료 시 다음 형식으로 보고한다.

```
완료했습니다.
- 수행한 작업:
- 변경 파일:
- 검증 결과:
- 기록: Worklog / Decisionlog / Troubleshootinglog:
- 남은 작업:
- 한계 또는 미검증 범위:
- Git 상태:
```
