# Decisionlog · Sparta_AX_Project

방향을 바꾸거나 이후 작업에 영향을 주는 **중요한 결정만** 기록한다. 사소한 수정은 Worklog에만 남긴다. (규칙: CLAUDE.md 11절)

## 기록 형식
```
### D-00N · 결정 제목
**상황** / **검토한 선택지** / **결정** / **근거** / **영향** / **재검토 조건**
```

---

### D-010 · 캠페인 시각화와 품질 QA를 추가 완성도 단계로 채택
**상황**
- Basic, Standard, Challenge 요구사항은 충족했지만, 요구사항 이상의 완성도를 보여줄 추가 Phase 후보가 필요했다.
- 사용자가 제출 품질 강화는 README로 충분하고, QA 스킬은 매 실행 사이클 마지막에 자동 실행되며, 캠페인 기획안 HTML 시각화는 진행해도 된다고 판단했다.
- 해커톤 중 안내에 따라 웹 UI 제외 제약은 제거되었고, 원본 및 의존 문서에서도 해당 제약을 제거해야 했다.

**검토한 선택지**
- (A) README 설명만 보강하고 추가 스킬은 만들지 않음
- (B) QA 스킬만 추가
- (C) 캠페인 HTML 시각화 스킬과 품질 QA 스킬을 모두 추가하고, QA를 마지막 단계로 고정

**결정**
- (C)를 채택한다.
- `kizzling-visualize-campaign`을 추가해 `campaign_plan.md`를 정적 HTML 미리보기로 시각화한다.
- `kizzling-quality-audit`을 추가해 이메일만 생성한 경우에도, 캠페인/시각화까지 진행한 경우에도 실행 사이클 마지막에 QA를 수행한다.
- 금지 범위는 실제 이메일 발송, SMTP/Gmail API, CRM, 다국어 이메일, 리드 스코어링, API 키·외부 발송 연동으로 유지한다.

**근거**
- HTML 시각화는 캠페인 세그먼트와 후속 시퀀스를 평가자가 빠르게 이해하게 해 Challenge 산출물의 전달력을 높인다.
- QA 스킬은 재사용 파이프라인의 안정성과 검수 가능성을 높이며, Standard의 재현성 요구와도 잘 맞는다.
- 웹 UI 제외 제약이 제거되었으므로 정적 HTML 보조 산출물을 제출 패키지에 포함해도 현재 제약과 충돌하지 않는다.

**영향**
- 최종 스킬 체인은 6개에서 8개로 확장된다.
- 전체 흐름은 `kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails → kizzling-campaign-plan → kizzling-visualize-campaign → kizzling-review-submit → kizzling-quality-audit`이다.
- `submission/output/campaign_plan_preview.html`과 `submission/output/quality_audit_report.md`가 추가 제출 산출물이 된다.
- `docs/phases/phase-7-quality-visualization.md`를 추가하고, README, 검증 계획, 최종 산출물 구조, 제출 요약, 평가 매핑을 갱신한다.

**재검토 조건**
- 운영 측에서 다시 HTML 산출물 또는 시각화 제출을 제한한다고 공지할 때.
- QA 스킬이 실제 사용자 실행 흐름에서 과도하게 길거나 중복된다고 판단될 때.

---

### D-009 · 로그 기록을 완료 조건으로 강화
**상황**
- 프로젝트가 Phase 문서, 스킬, 제출 패키지, 검수 산출물로 커지면서 작업 기록이 일부 대화 흐름에서 누락될 위험이 커졌다.
- 사용자가 Worklog, Decisionlog, Troubleshootinglog 기록 로직이 모든 대화에서 유지되도록 운영 규칙 강화를 요청했다.

**검토한 선택지**
- (A) 기존 로그 규칙을 유지하고 필요할 때만 수동으로 기록
- (B) `AGENTS.md`에 로그 작성 트리거와 생략 가능 조건을 명확히 추가

**결정**
- (B)를 채택한다.
- 주요 요청 완료 전 로그 기록을 작업 완료 조건으로 다루고, 파일·기준·구조·검증 방식이 바뀌는 경우의 기록 트리거를 명시한다.

**근거**
- 제출 직전에는 산출물 자체뿐 아니라 의사결정의 추적 가능성이 평가와 자체 검수에 중요하다.
- 로그 누락을 사후에 복원하는 방식보다, 완료 보고 전 체크리스트로 고정하는 편이 안정적이다.

**영향**
- 이후 작업은 완료 보고 전에 `Worklog.md`, 필요 시 `Decisionlog.md`와 `Troubleshootinglog.md` 갱신 여부를 확인한다.
- 단순 조회처럼 파일 변경이 없는 작업은 로그 생략 사유를 보고한다.

**재검토 조건**
- 로그 작성 비용이 작업 속도를 과도하게 저해하거나, 사용자가 특정 단계에서 로그 작성을 생략하라고 명시할 때.

---

### D-008 · 최종 제출 패키지를 submission/ 폴더로 고정
**상황**
- 기능별 스킬 체인과 산출물이 여러 경로에 분산되어 평가자가 확인할 최종 제출 묶음을 별도로 고정할 필요가 있었다.
- 사용자가 최종 제출용 폴더를 `submission/`으로 만들고, 스킬·입력 데이터·컨텍스트·직접 산출물·근거 요약만 포함하는 구조를 제안했다.

**검토한 선택지**
- (A) 작업 디렉터리 전체를 제출
- (B) `키즐링/` 하위 결과물을 중심으로 제출
- (C) `submission/` 폴더를 별도로 만들고 제출 핵심 파일만 복사

**결정**
- (C)를 채택한다.
- `submission/skills/`에는 기능별 `SKILL.md` 6개만 포함하고, `submission/output/`, `submission/data/`, `submission/context/`, `submission/evidence/`로 제출물을 분리한다.

**근거**
- 발제 요구사항과 금지 범위를 평가자가 빠르게 확인할 수 있다.
- 개발 보조 스크립트, 샘플 HTML, 원문 참고자료를 제외해 웹 UI·코드 의존 제출로 오해될 가능성을 줄인다.

**영향**
- 최종 제출 기준 경로는 `submission/`이다.
- `키즐링/scripts/`, `sample-*.html`, `template.md`, `docs/references/`, `out/`은 제출 폴더에서 제외한다.
- `docs/final-deliverables-structure.md`, `docs/phases/phase-6-review-submission.md`, `docs/validation-plan.md`, `README.md`, `docs/project-plan.md`는 `submission/` 기준으로 정렬한다.

**재검토 조건**
- 제출 플랫폼이 특정 파일 구조를 요구하거나, 평가자가 원본 작업 디렉터리 전체 제출을 요구한다고 확인될 때.

---

### D-007 · 최종 Skill 구조를 기능별 스킬 체인으로 세분화
**상황**
- D-006에서 최종 파이프라인을 스크립트 의존이 아닌 Skill 중심으로 전환했다.
- 이후 단일 `SKILL.md`만 고집할 필요는 없고, 기능별 `SKILL.md`가 상호 호출·의존하는 구조도 가능하다는 기준을 확인했다.

**검토한 선택지**
- (A) `kizzling-followup` 단일 스킬에 모든 절차를 유지
- (B) Basic, Standard, Challenge를 각각 큰 스킬로 분리
- (C) 발제의 실제 작업 흐름에 맞춰 분석, 전략, 생성, 캠페인, 검수 스킬로 분리하고 오케스트레이터가 순차 호출

**결정**
- (C)를 채택한다.
- `kizzling-followup`은 오케스트레이터로 두고, 기능별 스킬은 `kizzling-analyze-leads`, `kizzling-message-strategy`, `kizzling-generate-emails`, `kizzling-campaign-plan`, `kizzling-review-submit`으로 구성한다.

**근거**
- 발제의 Basic, Standard, Challenge는 누적형이므로 단계별 handoff가 명확한 스킬 체인이 평가자에게 구조적으로 보인다.
- 각 스킬의 책임을 작게 유지하면 `SKILL.md` 본문이 짧아지고, 재사용성과 검수 가능성이 높아진다.
- 별도 코드 의존 없이도 스킬 간 직렬 연결로 `정제 → 직책 분기 → 초안 생성 → review_flag → 캠페인 → 검수` 흐름을 설명할 수 있다.

**영향**
- 최종 제출 구조는 `.claude/skills/kizzling-followup/SKILL.md` 단독이 아니라 `.claude/skills/kizzling-*` 스킬 체인으로 설명한다.
- `docs/final-deliverables-structure.md`, `docs/requirements-contract.md`, `docs/phases/phase-4-standard-pipeline.md`, `키즐링/output/pipeline-usage.md`를 스킬 체인 기준으로 갱신한다.

**재검토 조건**
- 제출 환경이 다중 스킬 호출을 지원하지 않거나, 평가자가 단일 파일만 요구한다고 확인될 때.

---

### D-006 · 최종 파이프라인을 Skill 단독 구동으로 전환
**상황**
- Phase 4까지는 `키즐링/scripts/generate_basic_email_drafts.py`를 사용해 Basic/Standard 산출물을 재현했다.
- 이후 제출 전략상 별도 `py`, assets, 코드 파일 의존 없이 `SKILL.md` 단독 또는 스킬 묶음으로 구동되는 형태가 더 적합하다는 조언을 받았다.

**검토한 선택지**
- (A) 스크립트 기반 파이프라인을 최종 제출물로 유지
- (B) 스크립트를 플러그인형 보조물로 보고, 최종 제출 핵심은 `SKILL.md` 단독 워크플로로 전환
- (C) 기존 스크립트와 스킬을 모두 동일한 비중으로 제출

**결정**
- (B)를 채택한다.
- `.claude/skills/kizzling-followup/SKILL.md`를 최종 제출용 Skill 단독 파이프라인으로 둔다.
- `키즐링/scripts/generate_basic_email_drafts.py`는 개발·검증 보조물로만 취급한다.

**근거**
- 발제의 Standard는 슬래시 커맨드, 스킬, 스크립트 중 하나를 허용하지만, 해커톤 제출물로는 사용자가 `/스킬명` 형태로 재사용할 수 있는 Skill이 더 직접적이다.
- 별도 코드 의존을 제거하면 평가자가 스킬 본문만 읽고도 입력, 처리, 출력, 예외 처리, 검수 흐름을 이해하고 재현할 수 있다.

**영향**
- 최종 산출물 구조에서 `.claude/skills/kizzling-followup/SKILL.md`가 Standard/Challenge 재현성의 핵심 파일이 된다.
- `docs/final-deliverables-structure.md`, `docs/requirements-contract.md`, `docs/phases/phase-4-standard-pipeline.md`의 파이프라인 설명을 Skill 중심으로 수정한다.
- Phase 6 검수에서는 `py` 실행 가능 여부보다 `SKILL.md` 단독 절차의 완결성을 우선 확인한다.

**재검토 조건**
- 평가자가 스크립트 기반 자동 생성을 명시적으로 요구하거나, Skill 단독 실행만으로 산출물 일관성을 검증하기 어렵다고 판단될 때.

---

### D-005 · Standard 파이프라인 구현 방식을 스크립트 기반으로 확정
**상황**
- Phase 4에서 새 리드 CSV에도 같은 품질로 이메일 초안과 `review_flag`를 재현해야 했다.
- 기존 `/analyze`, `/insight`, `/generate`, `/review` 문서는 절차 기준을 제공하지만, 제출물에는 실행 가능한 사용법과 샘플이 필요했다.

**검토한 선택지**
- (A) 슬래시 커맨드 문서만 제출
- (B) 스크립트만 제출
- (C) 기존 슬래시 커맨드 흐름을 설명하고, 실제 생성은 스크립트로 재현

**결정**
- (C)를 채택한다.
- `키즐링/scripts/generate_basic_email_drafts.py`를 Standard 재현 파이프라인의 실행 단위로 사용한다.

**근거**
- 발제의 Standard 요구는 “새 CSV에도 동일 스키마로 재현”되는 실행 절차와 사용법을 요구한다.
- 스크립트는 필수 컬럼 검증, 결측·모호 탐지, 중복 제외, 직책별 분기, 출력 생성까지 재현 가능하게 만든다.
- 슬래시 커맨드 흐름은 해커톤 문제 패키지의 의도와 설명성을 유지한다.

**영향**
- `키즐링/output/pipeline-usage.md`, `키즐링/output/email_draft_sample.md`, `키즐링/output/standard_validation_summary.md`가 Standard 제출 산출물로 추가된다.
- 새 CSV 적용 시 `--input`만 교체하면 같은 파이프라인을 실행할 수 있다.

**재검토 조건**
- 사용자가 Claude Skill/슬래시 커맨드 중심 제출만 원하거나, 평가자가 스크립트 사용을 제한한다고 판단될 때.

---

### D-004 · Phase 2 메시지 전략 확정
**상황**
- Phase 2에서 `company-info.md`, `industry-news.md`, `/insight`, Phase 1 데이터 분석 결과를 바탕으로 이메일 생성 규칙을 확정해야 했다.
- 삭제된 보조 리서치 문서에는 의존하지 않고, 현재 남아 있는 기준 자료만 사용해야 했다.

**검토한 선택지**
- (A) 회사 컨텍스트의 직책별 소구점과 CTA를 그대로 채택
- (B) 리드 데이터 분포를 기준으로 직책별 CTA를 새로 설계
- (C) 삭제된 보조 리서치 문서의 내용을 복원하거나 의존

**결정**
- (A)를 기본으로 채택하고, Phase 1 분석 결과를 review_flag와 우선순위 강도에 반영한다.
- 삭제된 보조 리서치 문서에는 의존하지 않는다.

**근거**
- 발제와 `company-info.md`가 원장/팀장/사업개발별 CTA를 명시하고 있어 평가 기준과 정합성이 가장 높다.
- `industry-news.md`는 48시간 골든타임, 개인화, Human-in-the-loop 근거를 제공한다.

**영향**
- Phase 3 이메일 생성은 인사 → 상담언급 → 제품연결 → CTA 순서를 따른다.
- CTA는 원장=무료 데모 신청, 팀장=기술 도입 미팅, 사업개발=파트너십 제안서 송부로 고정한다.
- L009, L012, L015, L033, L046은 `review_flag = Y`; L050은 L039 중복 제외로 처리한다.

**재검토 조건**
- 실제 이메일 초안 검수에서 직책별 CTA가 어색하거나, 사용자가 제출 전략상 다른 CTA를 원할 때.

---

### D-003 · Phase 1 데이터 처리 기준 확정
**상황**
- Phase 1에서 `키즐링/data/leads_sample.csv`를 실제 분석한 결과, 발제 설명과 실제 데이터 사이에 상담 메모 결측 수량 차이가 있었다.
- 발제 설명은 상담 메모 결측 2건이라고 하지만 실제 CSV에는 `상담 메모 없음` 2건(L012, L046)과 빈 셀 1건(L015)이 있다.
- L039와 L050은 lead_id만 다르고 내용이 동일한 완전 중복 리드로 확인됐다.

**검토한 선택지**
- (A) 발제 설명의 수량을 우선해 상담 메모 결측 2건만 처리
- (B) 실제 CSV 값을 우선해 상담 메모 결측 3건을 처리
- (C) 중복 L039/L050을 둘 다 이메일 초안 대상으로 처리
- (D) L039를 기준 레코드로 사용하고 L050은 중복 제외로 기록

**결정**
- (B), (D)를 채택한다.
- `review_flag = Y` 후보는 이메일 결측 L009, 상담 메모 결측 L012/L015/L046, 상담 메모 모호 L033으로 총 5건이다.
- L039를 기준 레코드로 사용하고 L050은 중복 제외로 기록한다.

**근거**
- 구현 산출물은 실제 CSV를 입력으로 하므로 실제 데이터 품질 이슈를 우선해야 한다.
- 중복 리드를 모두 발송 대상으로 두면 중복 후속으로 브랜드 피로를 유발할 수 있다.

**영향**
- Phase 3 이메일 생성 시 L009, L012, L015, L033, L046은 `review_flag = Y`로 처리한다.
- L050은 별도 발송 초안 대신 중복 제외 기록에 포함한다.

**재검토 조건**
- 사용자가 발제 설명 수량에 맞추는 것이 제출상 더 안전하다고 판단하거나, 평가자가 50행 모두 출력하도록 요구하는 경우.

---

### D-002 · 제출 기준을 키즐링 발제 중심으로 전환
**상황**
- 초기 구조는 잘못된 제출가이드에 따라 Claude Skill 단독 제출을 중심으로 잡혀 있었다.
- 이후 발제문서와 키즐링 문제 패키지가 확인되었고, 실제 제출 형식은 `email_drafts.csv/.xlsx`와 Standard·Challenge 파이프라인/캠페인 산출물이었다.

**검토한 선택지**
- (A) 기존 Skill 단독 제출 구조 유지
- (B) 발제문서와 키즐링 하위 자료를 최우선 기준으로 전환

**결정**
- (B) 채택. 목표를 Basic, Standard, Challenge 전 요구사항 충족과 추가 완성도 강화로 전환한다.

**근거**
- 사용자가 제출가이드가 잘못된 안내였다고 확인했고, 발제문서가 실제 평가·제출 기준을 포함한다.
- 키즐링 폴더에는 데이터, 컨텍스트, 커맨드형 파이프라인, 샘플 산출물이 포함되어 있어 이를 기준으로 삼는 것이 요구사항 충족에 적합하다.

**영향**
- 루트 문서의 `skill-wip`, 주제 미정, SKILL.md 단독 제출 중심 문구를 제거한다.
- `키즐링/context/*.md`와 `키즐링/.claude/skills/*.md`를 필수 참고 자료로 반영한다.
- Challenge 보강을 위해 `/campaign` 또는 동등한 캠페인 기획 단계를 추가한다.

**재검토 조건**
- 운영 측에서 다시 제출 형식을 바꾸거나, 실제 구현 중 스크립트 중심 구조가 더 적합하다고 확인될 때.

---

### D-001 · 폴더 구조를 '스킬 제출형'으로 조정
**상황**
- 해커톤 제출물이 일반 앱이 아니라 Claude Skill(`.claude/skills/<이름>/SKILL.md`) 하나.

**검토한 선택지**
- (A) project-setup 표준 구조(src/tests/tools 포함) 그대로
- (B) 스킬 중심 구조 — src/tests/tools 생략, `.claude/skills/` + docs + out/demo

**결정**
- (B) 채택. 임시 스킬 이름 `skill-wip` 사용.

**근거**
- 산출물이 스킬 한 개라 일반 코드 트리는 과함. 제출 가이드가 요구하는 SKILL.md + 실행결과 형식에 맞춤.

**영향**
- 최상위 src/tests/tools 미생성. 보조 스크립트 필요 시 스킬 폴더 내부 scripts/로.

**재검토 조건**
- 스킬이 별도 실행 코드/테스트를 크게 동반하게 되면 구조 재검토.
