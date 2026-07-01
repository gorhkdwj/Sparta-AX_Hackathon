# 최종 산출물 구조

이 문서는 키즐링 과제의 최종 제출 패키지인 `submission/` 폴더 구조를 고정한다. 평가자가 Basic, Standard, Challenge 요구사항과 추가 검수 자료를 빠르게 확인하는 것이 목적이다.

## 제출 패키지 원칙

- 최종 제출자가 직접 여는 폴더는 `submission/`이다.
- `submission/.claude/skills/`에는 최종 Skill 체인 8개만 둔다.
- `submission/output/`에는 우리가 직접 생성한 제출 산출물만 둔다.
- `submission/evidence/`에는 원문 자료 복사본이 아니라 판단·설계·평가 대응 요약만 둔다.
- `키즐링/scripts/`, 제공 샘플 `sample-*.html`, `template.md`, `docs/references/`, `out/`은 제출 폴더에 포함하지 않는다.
- 실제 이메일 발송, CRM 연동, 다국어, 리드 스코어링, API 키·외부 발송 연동은 포함하지 않는다.

## 최종 제출 파일 세트

| 구분 | 파일 | 상태 | 역할 |
|---|---|---|---|
| Skill 핵심 | `submission/.claude/skills/kizzling-followup/SKILL.md` | 생성 완료 | 전체 워크플로를 조율하는 오케스트레이터 스킬 |
| Skill 기능 | `submission/.claude/skills/kizzling-analyze-leads/SKILL.md` | 생성 완료 | CSV 분석, 결측·모호·중복 탐지 |
| Skill 기능 | `submission/.claude/skills/kizzling-message-strategy/SKILL.md` | 생성 완료 | 직책별 소구점, CTA, review_flag 전략 |
| Skill 기능 | `submission/.claude/skills/kizzling-generate-emails/SKILL.md` | 생성 완료 | 이메일 초안과 Standard 산출물 생성 |
| Skill 기능 | `submission/.claude/skills/kizzling-campaign-plan/SKILL.md` | 생성 완료 | Challenge 캠페인 기획안 생성 |
| Skill 기능 | `submission/.claude/skills/kizzling-visualize-campaign/SKILL.md` | 생성 완료 | 캠페인 기획안 정적 HTML 시각화 |
| Skill 기능 | `submission/.claude/skills/kizzling-review-submit/SKILL.md` | 생성 완료 | 최종 검수와 제출 요약 |
| Skill 기능 | `submission/.claude/skills/kizzling-quality-audit/SKILL.md` | 생성 완료 | 실행 사이클 마지막 품질 QA |
| Basic 핵심 | `submission/output/email_drafts.csv` | 생성 완료 | 리드별 이메일 초안 제출 파일 |
| Basic 보조 | `submission/output/basic_exception_summary.md` | 생성 완료 | 이메일 결측, 상담 메모 결측·모호, 중복 제외 요약 |
| Basic 보조 | `submission/output/public_link_prep.md` | 생성 완료 | Google Sheet 공개 링크 생성 전 체크 절차 |
| Standard 핵심 | `submission/output/pipeline-usage.md` | 생성 완료 | 새 CSV 재현 파이프라인 사용법 |
| Standard 핵심 | `submission/output/email_draft_sample.md` | 생성 완료 | 파이프라인으로 생성한 이메일 초안 샘플 1부 |
| Standard 보조 | `submission/output/standard_validation_summary.md` | 생성 완료 | Standard 검증 요약 |
| Challenge 핵심 | `submission/output/campaign_plan.md` | 생성 완료 | 후속 캠페인 기획안 샘플 2건 |
| Challenge 보강 | `submission/output/campaign_plan_preview.html` | 생성 완료 | 캠페인 기획안 시각화 미리보기 |
| 검수 보강 | `submission/output/quality_audit_report.md` | 생성 완료 | Basic, Standard, Challenge, 시각화, 금지 범위 통합 QA (구 `review_report.md` 역할 통합, 별도 리포트 없음) |
| 제출 핵심 | `submission/output/submission-summary.md` | 생성 완료 | 평가자용 제출 요약, 요구사항 대응표, 검수 결과 요약 |
| 근거 보강 | `submission/evidence/design-rationale.md` | 생성 완료 | 양식·CTA·review_flag·우선순위 설계 근거 |
| 근거 보강 | `submission/evidence/evaluation-mapping.md` | 생성 완료 | 발제 평가 항목별 확인 파일 |
| 근거 보강 | `submission/evidence/decisions-summary.md` | 생성 완료 | 핵심 의사결정 요약 |
| 근거 보강 | `submission/evidence/campaign-plan-summary.md` | 생성 완료 | 캠페인 기획안 설계 근거 요약 |
| 근거 보강 | `submission/evidence/qa-and-pipeline-summary.md` | 생성 완료 | QA·파이프라인 재현성 근거 요약 |

## 실행 재현 파일 세트

| 파일 | 역할 | 의존 대상 | 생성 대상 |
|---|---|---|---|
| `.claude/skills/kizzling-followup/SKILL.md` | 최종 제출용 스킬 오케스트레이터 | 사용자 요청과 목표 레벨 | 기능별 스킬 호출 순서 |
| `.claude/skills/kizzling-analyze-leads/SKILL.md` | 데이터 분석 스킬 | 사용자 제공 CSV | 분석 handoff |
| `.claude/skills/kizzling-message-strategy/SKILL.md` | 메시지 전략 스킬 | 분석 handoff, 컨텍스트 | 전략 handoff |
| `.claude/skills/kizzling-generate-emails/SKILL.md` | 이메일 생성 스킬 | 분석·전략 handoff | Basic/Standard 산출물 |
| `.claude/skills/kizzling-campaign-plan/SKILL.md` | 캠페인 기획 스킬 | 분석·전략·이메일 산출물 | Challenge 산출물 |
| `.claude/skills/kizzling-visualize-campaign/SKILL.md` | 캠페인 시각화 스킬 | 캠페인 기획안 | HTML 미리보기 |
| `.claude/skills/kizzling-review-submit/SKILL.md` | 검수·제출 스킬 | 산출물 전체 | 검수 리포트, 제출 요약 |
| `.claude/skills/kizzling-quality-audit/SKILL.md` | 품질 QA 스킬 | 산출물 전체 | 품질 QA 리포트 |
| `키즐링/.claude/skills/analyze.md` | 제공 커맨드형 참고 자료 | 원본 CSV | Phase 1 분석 보조 |
| `키즐링/.claude/skills/insight.md` | 제공 커맨드형 참고 자료 | Phase 1, 컨텍스트 | Phase 2 전략 보조 |
| `키즐링/.claude/skills/generate.md` | 제공 커맨드형 참고 자료 | Phase 2 | Phase 3 산출물 보조 |
| `키즐링/.claude/skills/review.md` | 제공 커맨드형 참고 자료 | 산출물 전체 | Phase 6 검수 보조 |
| `키즐링/scripts/generate_basic_email_drafts.py` | 개발·검증 보조 스크립트 | `키즐링/data/leads_sample.csv` | 로컬 검증용 산출물 |

## 요구사항별 확인 경로

### Basic

평가자가 확인할 파일:

1. `submission/output/email_drafts.csv`
2. `submission/output/basic_exception_summary.md`
3. `submission/output/public_link_prep.md`
4. `docs/phases/phase-3-basic-email-drafts.md`

충족해야 하는 항목:

- 컬럼 `lead_id`, `subject`, `body`, `review_flag`
- 본문 250~400자
- 인사 → 상담언급 → 제품연결 → CTA 순서
- 직책별 제목, 소구점, CTA 차별화
- `review_flag`와 이메일 결측·중복 예외 처리
- 공개 링크 제출 준비와 접근 확인 기준

### Standard

평가자가 확인할 파일:

1. `submission/output/pipeline-usage.md`
2. `submission/output/email_draft_sample.md`
3. `submission/output/standard_validation_summary.md`
4. `submission/.claude/skills/kizzling-followup/SKILL.md`
5. `submission/.claude/skills/kizzling-generate-emails/SKILL.md`
6. `docs/phases/phase-4-standard-pipeline.md`

충족해야 하는 항목:

- 새 CSV 입력 시 스킬 체인에 CSV를 제공해 재현 가능
- `정제 → 직책 분기 → 초안 생성 → review_flag`를 기능별 스킬 체인으로 자동 생성
- 파이프라인 사용법
- 파이프라인 생성 이메일 샘플 1부
- 직책별 소구점, CTA, 우선순위별 강도, review_flag 기준의 설계 근거

### Challenge

평가자가 확인할 파일:

1. `submission/output/campaign_plan.md`
2. `submission/output/campaign_plan_preview.html`
3. `docs/phases/phase-5-challenge-campaign.md`
4. `submission/.claude/skills/kizzling-campaign-plan/SKILL.md`
5. `submission/.claude/skills/kizzling-visualize-campaign/SKILL.md`
6. `submission/output/pipeline-usage.md`

충족해야 하는 항목:

- 캠페인 기획안 샘플 1~2건
- 세그먼트 정의
- 근거 리드 건수와 lead_id
- 대표 상담 인용
- 후속 시퀀스
- 우선순위와 판단 근거
- 이메일 양식, review_flag 기준, 우선순위 판단 기준의 설계 근거
- 캠페인 세그먼트와 후속 시퀀스를 한눈에 볼 수 있는 HTML 미리보기

### 최종 검수와 제출

평가자가 확인할 파일:

1. `submission/output/submission-summary.md`
2. `submission/output/quality_audit_report.md`
3. `docs/validation-plan.md`
4. `Worklog.md`
5. `Decisionlog.md`

충족해야 하는 항목:

- 요구사항 대응표
- 제출 파일 목록
- 공개 링크 접근 확인 여부
- 미검증 범위
- 제외 범위 준수 여부
- 품질 QA 최종 판정
- 주요 결정과 문제 해결 기록

## 최종 제출 요약 문서 구조

`submission/output/submission-summary.md`는 Phase 6에서 아래 구조로 작성한다.

```text
# 키즐링 박람회 리드 후속 이메일 자동화 제출 요약

## 1. 제출 개요
## 2. Basic 산출물
## 3. Standard 산출물
## 4. Challenge 산출물
## 5. 실행 방법
## 6. 요구사항 대응표
## 7. 공개 링크
## 8. 검수 결과
## 9. 제외 범위와 미검증 범위
```

## 최종 검수 리포트 구조

별도 `review_report.md` 파일을 두지 않는다. 최종 검수 결과는 `submission/output/quality_audit_report.md`(Phase 7에서 아래 구조로 작성)와 `submission-summary.md`의 "8. 검수 결과" 절로 통합해 제공한다. 중복 리포트를 만들지 않는 것이 설계 의도다.

```text
# 품질 QA 리포트

## 1. 실행 범위
## 2. Basic QA
## 3. Standard QA
## 4. Challenge QA
## 5. 시각화 QA
## 6. 금지 범위 QA
## 7. 남은 미검증 범위
## 8. 최종 판정
```

## 권장 폴더 구조

```text
submission/
  README.md
  .claude/
    skills/
      kizzling-followup/
        SKILL.md
      kizzling-analyze-leads/
        SKILL.md
      kizzling-message-strategy/
        SKILL.md
      kizzling-generate-emails/
        SKILL.md
      kizzling-campaign-plan/
        SKILL.md
      kizzling-visualize-campaign/
        SKILL.md
      kizzling-review-submit/
        SKILL.md
      kizzling-quality-audit/
        SKILL.md
  data/
    leads_sample.csv
  context/
    company-info.md
    industry-news.md
  output/
    email_drafts.csv
    basic_exception_summary.md
    public_link_prep.md
    pipeline-usage.md
    email_draft_sample.md
    standard_validation_summary.md
    campaign_plan.md
    campaign_plan_preview.html
    quality_audit_report.md
    submission-summary.md
  evidence/
    design-rationale.md
    evaluation-mapping.md
    decisions-summary.md
    campaign-plan-summary.md
    qa-and-pipeline-summary.md
```

## 의존 관계 요약

```text
발제와 문제 설명
  → 기준 계약과 Phase 계획
  → 데이터 분석과 메시지 전략
  → 스킬 체인 파이프라인
  → Basic/Standard 산출물
  → Challenge 캠페인 산출물
  → 최종 검수와 제출 요약
```
