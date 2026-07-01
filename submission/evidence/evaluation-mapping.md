# Evaluation Mapping

발제의 Basic, Standard, Challenge 평가 항목이 제출 패키지의 어느 파일에서 확인되는지 정리합니다. **평가자는 `.claude/skills/`, csv 파일(`data/leads_sample.csv`, `output/email_drafts.csv`), `evidence/`만 확인**하므로, 아래 "확인 파일"은 이 범위 안의 파일을 우선 표기합니다. `output/*.md`, `output/*.html` 원본은 참고용으로 병기하되 괄호로 구분합니다.

## Basic

| 평가 항목 | 확인 파일 |
|---|---|
| 직책별 차별화 정확도 | `output/email_drafts.csv`, `evidence/design-rationale.md` |
| 개인화 4요소 | `output/email_drafts.csv` |
| 본문 250~400자 | `evidence/qa-and-pipeline-summary.md` (원본: `output/quality_audit_report.md`) |
| review_flag 정확도 | `output/email_drafts.csv`, `evidence/decisions-summary.md` (D-003-2) |
| 이메일 없는 리드 예외 처리 | `evidence/decisions-summary.md` (D-003-1) |
| 중복 리드 처리 | `evidence/decisions-summary.md` (D-003-3) |
| 제출 형식 | `output/email_drafts.csv`, `evidence/qa-and-pipeline-summary.md`(공개 링크 준비 상태, 원본: `output/public_link_prep.md`) |

## Standard

| 평가 항목 | 확인 파일 |
|---|---|
| 파이프라인 재현성 | `.claude/skills/`, `evidence/qa-and-pipeline-summary.md` (원본: `output/pipeline-usage.md`, `output/standard_validation_summary.md`) |
| 이메일 초안 샘플 1부 | `evidence/qa-and-pipeline-summary.md` (원본: `output/email_draft_sample.md`) |
| 후속 운영 설계 (직책별 소구점·CTA·우선순위 근거) | `evidence/design-rationale.md`, `evidence/decisions-summary.md` (D-004) |
| Skill 패키징 | `.claude/skills/kizzling-followup/SKILL.md`, 기능별 `.claude/skills/*/SKILL.md` |

## Challenge

| 평가 항목 | 확인 파일 |
|---|---|
| 후속 캠페인 기획안 (세그먼트·근거 리드·인용·후속 시퀀스·우선순위) | `evidence/campaign-plan-summary.md` (원본: `output/campaign_plan.md`) |
| 이메일 양식, review_flag, 우선순위 기준 설계 | `evidence/design-rationale.md`, `evidence/decisions-summary.md` |
| 캠페인 시각화 | (`output/campaign_plan_preview.html` — 평가 범위 밖이면 `evidence/campaign-plan-summary.md` 텍스트 내용으로 대체 확인) |
| 통합 품질 QA | `evidence/qa-and-pipeline-summary.md` (원본: `output/quality_audit_report.md`) |

## 제출 제약

| 제약 | 확인 파일 |
|---|---|
| API 키 없음 | `evidence/qa-and-pipeline-summary.md` |
| 이메일 실제 발송 없음 | `evidence/qa-and-pipeline-summary.md` |
| CRM 연동 없음 | `evidence/qa-and-pipeline-summary.md` |
| 다국어 이메일 없음 | `evidence/qa-and-pipeline-summary.md` |
| 리드 스코어링 없음 | `evidence/qa-and-pipeline-summary.md`, `evidence/campaign-plan-summary.md` |
| API 키·외부 발송 연동 없음 | `evidence/qa-and-pipeline-summary.md` |

## 참고

- `output/review_report.md`는 더 이상 존재하지 않는다. `kizzling-quality-audit`이 검수·QA 체크리스트를 통합했고, 그 결과는 `evidence/qa-and-pipeline-summary.md`에 옮겨 두었다.
