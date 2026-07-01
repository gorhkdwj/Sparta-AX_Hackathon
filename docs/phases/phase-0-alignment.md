# Phase 0 · 기준 정렬과 범위 고정

## 목표

발제 요구사항을 Basic, Standard, Challenge로 빠짐없이 재정리하고, 이번 프로젝트가 무엇을 만들고 무엇을 만들지 않을지 고정한다.

## 입력 자료

- `docs/references/발제.md`
- `docs/references/AX 해커톤 평가 기준.md`
- `키즐링/problem.md`
- `키즐링/CLAUDE.md`
- `docs/project-plan.md`
- `docs/requirements-contract.md`

## 수행 계획

1. 발제의 제출 형식과 레벨별 요구사항을 다시 분해한다.
2. Basic 필수 산출물을 고정한다:
   - `email_drafts.csv/.xlsx`
   - 컬럼 `lead_id, subject, body, review_flag`
   - 본문 250~400자
   - 개인화 4요소
   - 노션 또는 구글 시트 공개 링크
3. Standard 필수 산출물을 고정한다:
   - 재현 파이프라인
   - 간단한 사용법
   - 파이프라인으로 생성한 이메일 초안 샘플 1부
   - 직책별 소구점·CTA·우선순위별 강도 설계 근거
4. Challenge 필수 산출물을 고정한다:
   - Standard 산출물 전체
   - 후속 캠페인 기획안 샘플 1~2건
   - 이메일 양식·review_flag·우선순위 판단 기준 설계 근거
5. 금지 범위를 문서화한다:
   - 실제 이메일 발송
   - CRM 연동
   - 다국어 이메일
   - 리드 스코어링
   - API 키·외부 발송 연동

## 산출물

- 최종 산출물 체크리스트
- 범위와 제외 범위 목록
- `docs/requirements-contract.md`와 `docs/validation-plan.md`의 정합성 확인 결과

## Phase 0 실행 결과

### 최종 산출물 체크리스트

> 아래 "상태" 열은 Phase 0 계획 시점 기준이었다. 현재는 Phase 7까지 모두 완료됐으며, 실제 상태는 이 표 대신 `submission/output/quality_audit_report.md`(통합 QA 판정)와 `Worklog.md`를 기준으로 확인한다.

| 구분 | 제출/관리 산출물 | 경로 또는 형식 | 상태 |
|---|---|---|---|
| Basic | 리드별 이메일 초안 | `키즐링/output/email_drafts.csv`, `submission/output/email_drafts.csv` | 생성 완료 |
| Basic | 제출 공개 링크 | 노션 또는 구글 시트 공개 링크 | 미완료 — `public_link_prep.md`에 절차만 준비, 실제 업로드·접근 확인은 남음 |
| Basic | 예외 처리 요약 | 이메일 결측, 상담 메모 결측·모호, 중복 리드 요약 | 생성 완료 |
| Standard | 재현 파이프라인 사용법 | `submission/output/pipeline-usage.md` | 생성 완료 |
| Standard | 파이프라인 생성 이메일 샘플 1부 | `submission/output/email_draft_sample.md` | 생성 완료 |
| Standard | 설계 근거 | `submission/evidence/design-rationale.md` 등 | 생성 완료 |
| Challenge | 자동 생성 캠페인 기획안 샘플 1~2건 | `submission/output/campaign_plan.md` | 생성 완료 (2건) |
| Challenge | 양식·기준 설계 근거 | 이메일 양식, review_flag 기준, 우선순위 판단 기준 | 생성 완료 |
| 제출 보강 | 캠페인 시각화 (Phase 7 추가) | `submission/output/campaign_plan_preview.html` | 생성 완료 |
| 제출 보강 | 통합 품질 QA (Phase 7 추가) | `submission/output/quality_audit_report.md` | 생성 완료 (구 `키즐링/output/review_report.md` 역할 통합, 최종 패키지는 이 리포트 하나로 검수) |
| 제출 보강 | 제출용 요약 | `submission/output/submission-summary.md` | 생성 완료 |

### 레벨별 고정 요구사항

#### Basic

- `키즐링/data/leads_sample.csv` 50건을 분석한다.
- 결과 파일은 `email_drafts.csv` 또는 `.xlsx`다.
- 필수 컬럼은 `lead_id, subject, body, review_flag`다.
- 본문은 인사 → 상담언급 → 제품연결 → CTA 순서의 한국어 250~400자다.
- 원장, 팀장, 사업개발별 제목·소구점·CTA가 다르다.
- CTA 기본값은 원장=무료 데모 신청, 팀장=기술 도입 미팅, 사업개발=파트너십 제안서 송부다.
- 상담 메모 결측·모호 리드는 `review_flag = Y`다.
- 이메일 없는 리드는 `review_flag = Y`와 발송 불가 후속 메모로 전환한다.
- 중복 리드는 한 건으로 처리하고 기준 lead_id와 제외 lead_id를 기록한다.
- 노션 또는 구글 시트 공개 링크 제출과 접근 가능 여부 확인을 준비한다.

#### Standard

- 새 리드 CSV에도 동일 스키마로 `정제 → 직책 분기 → 초안 생성 → review_flag`가 재현되어야 한다.
- Standard 흐름은 `kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails → kizzling-review-submit → kizzling-quality-audit`이다.
- Challenge 포함 흐름은 `kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails → kizzling-campaign-plan → kizzling-visualize-campaign → kizzling-review-submit → kizzling-quality-audit`이다.
- 채택 방식은 기능별 Skill 체인이며, 간단한 사용법을 제공한다.
- 파이프라인으로 생성한 이메일 초안 샘플 1부를 제공한다.
- 직책별 소구점·CTA·우선순위별 강도·review_flag 기준을 마케팅·영업 관점에서 1~2줄 이상 설명한다.

#### Challenge

- Standard 산출물 전체를 포함한다.
- 리드 데이터 패턴 기반 후속 캠페인 기획안을 파이프라인에서 자동 생성한다.
- 캠페인 기획안 샘플 1~2건을 제공한다.
- 각 기획안에는 세그먼트 정의, 근거 리드(건수·인용), 후속 시퀀스, 우선순위를 포함한다.
- 이메일 양식·review_flag 기준·우선순위 판단 기준의 설계 근거를 설명한다.

### 범위와 제외 범위

포함 범위:

- 제공 더미 데이터 기반 이메일 초안 생성
- 새 CSV 재사용 파이프라인 구성
- 후속 캠페인 기획안 자동 생성
- 검수 리포트와 제출용 요약 작성
- 공개 링크 제출 준비

제외 범위:

- 실제 이메일 발송
- CRM 연동
- 다국어 이메일
- 리드 스코어링
- API 키·외부 발송 연동
- 실제 고객 데이터 사용

### 기준 문서 정합성 확인 결과

| 확인 항목 | 결과 |
|---|---|
| `docs/requirements-contract.md`에 Basic/Standard/Challenge 산출물이 정의됨 | 통과 |
| `docs/validation-plan.md`에 Basic/Standard/Challenge 검증 기준이 정의됨 | 통과 |
| 구 제출가이드가 현재 제출 기준으로 사용되지 않음 | 통과 |
| 이전 단일 스킬·스크립트 중심 기준이 현재 운영 기준으로 남아 있지 않음 | 통과 |
| 이후 Phase가 참조할 산출물 경로가 고정됨 | 통과 |

### Phase 0 상태

- 상태: 완료
- 완료일: 2026-07-01
- 다음 Phase: Phase 1 데이터 분석과 예외 기준 설계

## 완료 기준

- 평가자가 요구하는 제출물이 문서상 빠짐없이 보인다.
- 구 제출가이드나 이전 단일 스킬·스크립트 중심 기준이 현재 운영 기준으로 남아 있지 않다.
- 이후 Phase가 참조할 기준 문서가 확정된다.

## 검증 기준

- `rg`로 이전 골격 문구와 삭제된 제출가이드 참조를 확인한다.
- 발제의 Basic, Standard, Challenge 요구 문장이 `requirements-contract.md`와 `validation-plan.md`에 반영됐는지 확인한다.

## 다음 Phase 전달물

- 고정된 제출 산출물 목록
- 금지 범위
- 레벨별 검증 기준

## 리스크와 대응

- 리스크: 요구사항 일부가 암묵적으로만 남아 구현에서 누락될 수 있음.
- 대응: Phase 0 완료 전 발제의 “기대 Output”과 “self-review”를 체크리스트화한다.
