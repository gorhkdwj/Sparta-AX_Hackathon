# Phase 7 · 시각화와 품질 QA

## 목표

Basic, Standard, Challenge 요구사항을 충족한 뒤, 평가자가 산출물을 더 빠르게 이해하고 사용자가 반복 실행 결과를 더 안전하게 검수할 수 있도록 추가 완성도 산출물을 만든다.

## 입력 자료

- `submission/output/email_drafts.csv`
- `submission/output/basic_exception_summary.md`
- `submission/output/campaign_plan.md`
- `키즐링/output/review_report.md` (Phase 6 검수 체크리스트 원본. 이 Phase에서 `quality_audit_report.md`로 통합하고 대체한다)
- `.claude/skills/kizzling-visualize-campaign/SKILL.md`
- `.claude/skills/kizzling-quality-audit/SKILL.md`

## 수행 계획

1. `kizzling-visualize-campaign`을 추가해 캠페인 기획안을 정적 HTML 미리보기로 변환한다.
2. HTML에는 캠페인 세그먼트, 근거 리드, 대표 상담 인용, Day 0/Day 2~3/Day 7 후속 시퀀스, 검수 필요 리드를 표시한다.
3. `kizzling-quality-audit`을 추가해 모든 실행 사이클 마지막에 QA가 수행되도록 한다.
4. QA는 이메일만 생성한 경우에도 실행하며, 캠페인이나 HTML 시각화가 있으면 해당 산출물까지 검수한다.
5. 해커톤 중 안내에 따라 HTML 시각화 산출물을 허용하되, 실제 발송·CRM·다국어·리드 스코어링·API 키 금지는 유지한다.

## 산출물

- `.claude/skills/kizzling-visualize-campaign/SKILL.md`
- `.claude/skills/kizzling-quality-audit/SKILL.md`
- `키즐링/output/campaign_plan_preview.html`
- `키즐링/output/quality_audit_report.md`
- `submission/.claude/skills/kizzling-visualize-campaign/SKILL.md`
- `submission/.claude/skills/kizzling-quality-audit/SKILL.md`
- `submission/output/campaign_plan_preview.html`
- `submission/output/quality_audit_report.md`

## 완료 기준

- `kizzling-followup`의 전체 체인이 `분석 → 전략 → 이메일 생성 → 캠페인 → 시각화 → 검수 → QA` 순서로 설명된다.
- `kizzling-quality-audit`이 항상 마지막 단계로 명시된다.
- `campaign_plan_preview.html`이 정적 HTML로 생성되고 외부 API, 외부 CDN, 실제 발송, CRM 연결, 리드 점수 산출 기능을 포함하지 않는다.
- `quality_audit_report.md`가 Basic, Standard, Challenge, 시각화, 금지 범위를 함께 검수한다.

## 검증 기준

- `submission/.claude/skills/`에 8개 `SKILL.md`가 있다.
- `submission/output/campaign_plan_preview.html`과 `submission/output/quality_audit_report.md`가 있다.
- HTML 시각화는 허용된 추가 완성도 산출물이며, 금지 범위는 실제 발송·CRM·다국어·리드 스코어링·API 키·외부 발송 연동으로 유지된다.
- 제공 샘플 HTML(`sample-*.html`)과 새 시각화 HTML(`campaign_plan_preview.html`)이 문서상 구분된다.

## 다음 Phase 전달물

- 최종 제출 전 검수 시 `submission/README.md`, `submission/output/submission-summary.md`, `submission/output/quality_audit_report.md`를 함께 확인한다.

## 리스크와 대응

- 리스크: HTML 시각화가 실제 발송 또는 외부 연동 기능으로 오해될 수 있다.
- 대응: 정적 HTML이며 실제 발송, CRM 연결, 리드 점수 산출 기능이 없음을 README, QA 리포트, HTML 푸터에 명시한다.
