# 키즐링 박람회 리드 후속 이메일 자동화 제출 요약

## 1. 제출 개요

이 제출물은 키즐링 박람회 리드 50건을 대상으로 개인화 후속 이메일 초안, 재사용 가능한 Skill 체인 파이프라인, 후속 캠페인 기획안을 구성한 패키지입니다.

최종 제출 폴더는 `submission/`이며, 평가자는 이 폴더만 열어 Basic, Standard, Challenge 산출물을 확인할 수 있습니다.

## 2. Basic 산출물

- `submission/output/email_drafts.csv`
- `submission/output/basic_exception_summary.md`
- `submission/output/public_link_prep.md`

요구사항 대응:

- 필수 컬럼: `lead_id`, `subject`, `body`, `review_flag`
- 생성 행 수: 49행
- 본문 길이: 250~279자
- `review_flag = Y`: L009, L012, L015, L033, L046
- 중복 제외: L050, 대표 L039

## 3. Standard 산출물

- `submission/skills/kizzling-followup/SKILL.md`
- `submission/skills/kizzling-analyze-leads/SKILL.md`
- `submission/skills/kizzling-message-strategy/SKILL.md`
- `submission/skills/kizzling-generate-emails/SKILL.md`
- `submission/skills/kizzling-quality-audit/SKILL.md`
- `submission/skills/kizzling-review-submit/SKILL.md`
- `submission/output/pipeline-usage.md`
- `submission/output/email_draft_sample.md`
- `submission/output/standard_validation_summary.md`

Skill 체인:

```text
kizzling-analyze-leads
  -> kizzling-message-strategy
  -> kizzling-generate-emails
  -> kizzling-review-submit
  -> kizzling-quality-audit
```

## 4. Challenge 산출물

- `submission/skills/kizzling-campaign-plan/SKILL.md`
- `submission/skills/kizzling-visualize-campaign/SKILL.md`
- `submission/output/campaign_plan.md`
- `submission/output/campaign_plan_preview.html`
- `submission/output/quality_audit_report.md`

캠페인 샘플:

1. 에듀테크 팀장 대상 대회 운영 자동화 전환 캠페인
2. 사업개발 대상 파트너십 제안 캠페인

각 캠페인은 세그먼트 정의, 근거 리드, 대표 상담 인용, 후속 시퀀스, 우선순위와 판단 근거를 포함합니다.

## 5. 실행 방법

Cowork 또는 Claude Code에서 `submission/skills/`의 Skill 체인을 사용합니다. 별도 API 키, 외부 스크립트, CRM, 이메일 발송 연동은 필요하지 않습니다.

Challenge 포함 전체 흐름:

```text
kizzling-followup
  -> kizzling-analyze-leads
  -> kizzling-message-strategy
  -> kizzling-generate-emails
  -> kizzling-campaign-plan
  -> kizzling-visualize-campaign
  -> kizzling-review-submit
  -> kizzling-quality-audit
```

## 6. 요구사항 대응표

| 발제 요구 | 확인 파일 |
|---|---|
| 리드별 이메일 초안 | `submission/output/email_drafts.csv` |
| 예외 처리 | `submission/output/basic_exception_summary.md` |
| 재사용 파이프라인 | `submission/output/pipeline-usage.md`, `submission/skills/` |
| 이메일 초안 샘플 1부 | `submission/output/email_draft_sample.md` |
| 캠페인 기획안 샘플 1~2건 | `submission/output/campaign_plan.md` |
| 캠페인 기획안 시각화 | `submission/output/campaign_plan_preview.html` |
| 설계 근거 | `submission/evidence/design-rationale.md` |
| 검수 결과 | `submission/output/review_report.md` |
| 품질 QA | `submission/output/quality_audit_report.md` |

## 7. 공개 링크

- Google Sheet 공개 링크는 아직 생성하지 않았다.
- `submission/output/public_link_prep.md`에 업로드와 접근 확인 절차를 정리했다.
- Cowork 제출 시 Skill 패키징으로 제출 가능하다는 조건에 맞춰 `submission/skills/`를 포함했다.

## 8. 검수 결과

- Basic: 통과
- Standard: 통과
- Challenge: 통과
- 제외 범위: 통과

상세 결과는 `submission/output/review_report.md`를 확인한다.

## 9. 제외 범위와 미검증 범위

제외:

- 실제 이메일 발송
- SMTP/Gmail API
- CRM 연동
- 다국어 이메일
- 리드 스코어링
- API 키·외부 발송 연동

미검증:

- Google Sheet 공개 링크 접근성
- 새 독립 세션에서 Skill 체인의 end-to-end 재실행
