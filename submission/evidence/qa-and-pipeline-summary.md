# QA and Pipeline Summary

`output/`의 파이프라인 사용법·이메일 샘플·QA 결과·제출 요약을 평가 범위(`.claude/skills/` + csv + `evidence/`) 안에서 확인할 수 있도록 옮긴 요약본입니다. 원문은 각각 `output/pipeline-usage.md`, `output/email_draft_sample.md`, `output/quality_audit_report.md`, `output/submission-summary.md`, `output/public_link_prep.md`, `output/standard_validation_summary.md`입니다.

## 1. Standard 파이프라인 재현성

**입력 조건**
- 필수 컬럼: `lead_id`, `name`, `organization`, `org_type`, `title`, `email`, `consultation_note`, `interest_feature`, `follow_up_priority`
- 허용 직책: `원장`, `팀장`, `사업개발` / 허용 관심 기능: `대회운영SaaS`, `콘텐츠안전필터`, `파트너십` / 허용 우선순위: `상`, `중`, `하`

**Standard 단독 흐름**
```text
kizzling-analyze-leads -> kizzling-message-strategy -> kizzling-generate-emails
  -> kizzling-review-submit -> kizzling-quality-audit
```

**Challenge 포함 흐름**
```text
kizzling-analyze-leads -> kizzling-message-strategy -> kizzling-generate-emails
  -> kizzling-campaign-plan -> kizzling-visualize-campaign
  -> kizzling-review-submit -> kizzling-quality-audit
```

- 최종 파이프라인은 별도 `py`, assets, 외부 API 없이 `.claude/skills/kizzling-followup/SKILL.md`가 기능별 Skill을 호출하는 워크플로다. 새 리드 CSV를 동일 스키마로 넣으면 같은 순서로 재현된다.
- 개발 과정에서 쓴 로컬 검증 보조 스크립트(`키즐링/scripts/generate_basic_email_drafts.py`)는 최종 제출 패키지에 포함하지 않았고 필수 의존성도 아니다.

**자동 처리 기준**
- 이메일 결측: `review_flag = Y`, 제목에 `[검수 필요]` 표시, 본문은 연락처 확인 메모로 작성.
- 상담 메모 결측(빈 값·"상담 메모 없음"·"없음"·"미기재") 및 모호("애매"·"모호"·"구체적 니즈 파악 안 됨" 등): `review_flag = Y`.
- 중복 리드: 이름·조직·직책·이메일·상담 메모·관심 기능이 동일하면 첫 lead_id만 유지, 이후 lead_id는 제외.

**Standard 재현 검증 결과** (`standard_validation_summary.md` 기준)
- 출력 행 수 49 / 본문 길이 250~297자 / `review_flag = Y`: L009, L012, L015, L033, L046 / 중복 제외: L050
- Standard 스킬 체인 흐름 문서화, 기능별 Skill 사용법 문서화, 이메일 초안 샘플 1부 생성, 직책별 소구점·CTA 설계 근거 문서화, review_flag 기준 문서화 — 모두 통과

## 2. 파이프라인 생성 이메일 초안 샘플 1부

- `lead_id = L001` / `title = 원장` / `follow_up_priority = 상` / `interest_feature = 대회운영SaaS` / `review_flag = N`
- `subject`: "[키즐링] 김민준 원장님, 우리 원 아이들의 재능을 보여주는 키즐콘 안내"
- `body`(개인화 4요소 확인): ①"김민준 원장님" + 에듀플러스위크 만남 언급 ②접수·심사·결과발표 수기 운영의 번거로움(상담 언급) ③대회운영SaaS 자동화 → 원생 성취를 학부모께 전달(원장 소구점 연결) ④무료 데모 신청(CTA, 우선순위 `상`이라 "이번 주 안")
- 전체 본문은 `output/email_draft_sample.md`와 `output/email_drafts.csv`(L001 행)에서 동일하게 확인 가능.

## 3. 품질 QA 결과 (`quality_audit_report.md` 기준)

| 구분 | 결과 |
|---|---|
| Basic (필수 컬럼·행수·본문 길이 250~279자·4요소 순서·직책별 차별화·review_flag·이메일 결측·중복 처리) | 통과 |
| Standard (Skill 체인·새 CSV 대응·이메일 샘플·스크립트 비의존·설계 근거) | 통과 |
| Challenge (캠페인 샘플 2건·세그먼트·근거 리드·대표 인용·후속 시퀀스·우선순위·review_flag 반영) | 통과 |
| 시각화 (`campaign_plan_preview.html` — 외부 호출 없음, 금지 기능 없음) | 통과 |
| 금지 범위 (실발송·SMTP·CRM·다국어·리드 스코어링·API 키·실제 고객 데이터 없음) | 통과 |
| **최종 판정** | **통과** — Basic/Standard/Challenge 요구사항과 캠페인 시각화 포함, 금지 범위 위반 없음 |

- 참고: 과거 `kizzling-review-submit`이 별도로 만들던 `review_report.md`는 이 QA 리포트와 체크리스트가 거의 동일해 중복이었다. 현재는 QA 리포트 하나로 통합했고, `review-submit`은 `submission-summary.md`와 `public_link_prep.md`만 생성한다.

## 4. 남은 미검증 범위

- 노션/구글 시트 공개 링크 접근성 — 외부 Google/노션 계정 작업이 필요해 이번 세션에서는 완료하지 못했다. 제출 직전 담당자가 직접 생성·접근 확인해야 한다(`public_link_prep.md` 절차 참조).
- 완전히 새로운 독립 세션에서 `kizzling-followup`을 호출해 전체 스킬 체인을 재실행하는 end-to-end 검증은 아직 수행하지 않았다.

## 5. 제외 범위 (모든 레벨 공통)

실제 이메일 발송, SMTP/Gmail API, CRM 연동, 다국어 이메일, 리드 스코어링(`follow_up_priority`는 입력값으로만 사용), API 키·외부 발송 연동 — 모두 미포함을 확인했다.
