# 검증 계획 · 키즐링 리드 후속 이메일 자동화

검증은 `docs/references/발제.md`의 기대 Output과 self-review 채점표를 최우선 기준으로 한다. 최종 파이프라인 검증은 `.claude/skills/kizzling-*` 스킬 체인 기준으로 수행하고, 검증하지 못한 부분은 `미검증 범위`에 남긴다.

> 이 문서의 체크리스트는 검증 항목 정의이며, 실제 실행된 판정 결과는 항목별로 체크하지 않고 `submission/output/quality_audit_report.md`(통합 QA 판정)와 `Worklog.md`(W-015~W-019)에 기록한다. 아래 1~6번 항목은 현재 제출물 기준으로 모두 통과 상태다.

## 검증 항목

### 1. 데이터 검증

- [ ] `키즐링/data/leads_sample.csv`가 존재한다.
- [ ] 필수 컬럼 9개가 모두 있다.
- [ ] 전체 50건을 확인했다.
- [ ] 직책 분포를 확인했다.
- [ ] 이메일 결측 리드를 확인했다.
- [ ] 상담 메모 결측·모호 리드를 확인했다.
- [ ] 완전 중복 리드를 확인했다.

### 2. Basic 검증

- [ ] `email_drafts.csv` 또는 `.xlsx`가 생성됐다.
- [ ] 컬럼이 `lead_id, subject, body, review_flag`다.
- [ ] 원장, 팀장, 사업개발 제목이 서로 다르다.
- [ ] 원장, 팀장, 사업개발 소구점과 CTA가 서로 다르다.
- [ ] 직책별 CTA가 원장=무료 데모 신청, 팀장=기술 도입 미팅, 사업개발=파트너십 제안서 송부로 맞다.
- [ ] 각 본문에 맞춤 인사, 상담 내용 언급, 제품 연결, CTA 1개가 포함됐다.
- [ ] 각 본문이 인사 → 상담언급 → 제품연결 → CTA 순서를 따른다.
- [ ] 본문이 250~400자 범위다.
- [ ] 상담 메모 결측·모호 리드는 `review_flag = Y`다.
- [ ] 이메일 없는 리드는 `review_flag = Y`와 발송 불가 후속 메모로 처리됐다.
- [ ] 중복 리드는 한 건으로 처리되고 기준 lead_id와 제외 lead_id가 기록됐다.
- [ ] 노션 또는 구글 시트 공개 링크 제출 준비와 접근 확인 기준이 있다.

### 3. Standard 검증

- [ ] 새 리드 CSV에 적용 가능한 절차가 문서화됐다.
- [ ] Standard 흐름(`kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails → kizzling-review-submit → kizzling-quality-audit`)이 설명됐다.
- [ ] Challenge 포함 흐름(`kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails → kizzling-campaign-plan → kizzling-visualize-campaign → kizzling-review-submit → kizzling-quality-audit`)과 구분된다.
- [ ] `정제 → 직책 분기 → 초안 생성 → review_flag`가 동일 스키마로 재생성된다는 기준이 있다.
- [ ] 채택한 방식이 기능별 Skill 체인임이 명확하고 간단한 사용법이 있다.
- [ ] 파이프라인으로 생성한 이메일 초안 샘플 1부가 있다.
- [ ] 직책별 소구점·CTA 설계 근거가 있다.
- [ ] 우선순위별 CTA 강도 설계 근거가 있다.
- [ ] review_flag 기준 설계 근거가 있다.
- [ ] 설계 근거가 마케팅·영업 관점에서 무엇이 전환을 만드는지 1~2줄 이상 설명한다.
- [ ] 별도 `py`, assets, 외부 API가 최종 필수 의존성이 아님이 명확하다.

### 4. Challenge 검증

- [ ] 캠페인 기획안이 파이프라인의 자동 생성 단계로 포함됐다.
- [ ] 자동 생성된 캠페인 기획안 샘플 1~2건이 있다.
- [ ] 각 기획안에 세그먼트 정의가 있다.
- [ ] 근거 리드 건수와 lead_id가 있다.
- [ ] 대표 상담 인용이 있다.
- [ ] 후속 시퀀스가 있다.
- [ ] 우선순위와 판단 근거가 있다.
- [ ] 이메일 양식, review_flag 기준, 우선순위 판단 기준의 설계 근거가 설명됐다.
- [ ] `industry-news.md`의 골든타임, 개인화, Human-in-the-loop, 데이터 품질 맥락과 연결된다.

### 4-1. 추가 완성도 검증

- [ ] `campaign_plan_preview.html`이 캠페인 기획안을 정적 HTML로 시각화한다.
- [ ] HTML 미리보기에 세그먼트, 근거 리드, 대표 인용, 후속 시퀀스, 검수 필요 리드가 표시된다.
- [ ] `quality_audit_report.md`가 이메일, 캠페인, 시각화, 금지 범위를 함께 검수한다.
- [ ] `kizzling-quality-audit`이 매 실행 사이클 마지막 단계로 설명된다.

### 5. 문서 정합성 검증

- [ ] 삭제된 구 제출가이드를 현재 제출 기준으로 사용하지 않는다.
- [ ] 이전 골격 문구가 현재 운영 기준으로 남아 있지 않다.
- [ ] 스킬 구조가 오케스트레이터 + 기능별 Skill 체인으로 일관되게 설명된다.
- [ ] `CLAUDE.md`, `AGENTS.md`, `README.md`, `docs/*`의 목표와 산출물이 일치한다.
- [ ] `Worklog.md`와 `Decisionlog.md`에 이번 구조 전환이 기록됐다.

### 6. 제출 폴더 검증

- [ ] `submission/.claude/skills/`에 8개 Skill `SKILL.md`만 있다.
- [ ] `submission/data/`에는 `leads_sample.csv`만 있다.
- [ ] `submission/context/`에는 `company-info.md`, `industry-news.md`만 있다.
- [ ] `submission/output/`에는 직접 생성한 제출 산출물만 있다.
- [ ] `submission/evidence/`에는 판단·설계·평가 대응 요약만 있다.
- [ ] 제공 샘플인 `sample-*.html`, `template.md`, `scripts/`, `docs/references/`, `out/`이 `submission/`에 없다.
- [ ] API 키, `.env`, SMTP/Gmail, CRM, 외부 발송 연동 파일이 `submission/`에 없다.
- [ ] `submission/output/campaign_plan_preview.html`은 제공 샘플 HTML이 아니라 직접 생성한 캠페인 시각화 산출물로 포함된다.

## 검증 방법과 도구

- 파일 참조 확인: `rg`
- CSV 구조 확인: PowerShell 또는 Python 읽기
- 산출물 검수: `.claude/skills/kizzling-review-submit/SKILL.md` 체크리스트
- 문서 정합성 확인: 주요 키워드 검색

## 완료 선언 기준

- Basic, Standard, Challenge 검증 항목이 모두 통과한다.
- 실패 항목은 수정하거나 `미검증 범위`에 사유와 함께 남긴다.
- 실제 이메일 발송, CRM 연동, 다국어, 리드 스코어링, API 키·외부 발송 연동은 금지 범위라 수행하지 않는다.

## 현재 미검증 범위

- `키즐링/output/email_drafts.csv`는 생성했고 로컬 검증을 완료했다. 실제 Google Sheet 공개 링크 접근성은 아직 확인하지 않았다.
- 기능별 Skill 체인 구조는 이 저장소와 무관한 독립 폴더(`C:\Users\gorhk\새 폴더`)에 `.claude/skills`를 복사하고 더미 리드 CSV로 `kizzling-followup` 전체 체인을 실행하는 방식으로 end-to-end 검증을 완료했다(Worklog W-019, Troubleshootinglog T-004). 스키마·본문 길이·`review_flag`·중복 처리·캠페인 근거·시각화 안전성은 원본 제출물과 동일 품질로 재현됐고, 우선순위별 CTA 강도 규칙 적용에 경미한 런투런 편차 2건이 발견되어 사람 검수 대상으로 남겼다.
- `키즐링/output/campaign_plan.md`와 `submission/output/campaign_plan.md`를 생성했다.
- `키즐링/output/campaign_plan_preview.html`와 `submission/output/campaign_plan_preview.html`를 생성했다.
- `키즐링/output/quality_audit_report.md`와 `submission/output/quality_audit_report.md`를 생성했다.
- 파이프라인 사용법과 이메일 초안 샘플 1부는 `키즐링/output/pipeline-usage.md`, `키즐링/output/email_draft_sample.md`로 정리했다.
- 전체 검수 리포트와 제출 요약은 `키즐링/output/` 및 `submission/output/`에 생성했다.
