# 키즐링 제출 패키지

이 폴더는 스파르타 AX 해커톤 키즐링 과제 제출 전용 패키지입니다. 원본 작업 폴더 전체가 아니라, 발제 요구사항을 확인하는 데 필요한 핵심 파일만 포함합니다.

## 처음 사용하는 방법

이 패키지는 박람회에서 받은 리드 CSV를 넣으면 리드별 맞춤 후속 이메일 초안과 후속 캠페인 기획안까지 만들 수 있도록 구성된 Claude Skill 묶음입니다.

실제 이메일을 보내지는 않습니다. 결과물은 사람이 검토한 뒤 발송하기 위한 초안입니다.

### 1. 먼저 열어볼 파일

처음 받았다면 아래 순서로 확인합니다.

```text
README.md
data/leads_sample.csv
.claude/skills/kizzling-followup/SKILL.md
output/email_drafts.csv
output/campaign_plan.md
output/submission-summary.md
```

`README.md`는 전체 제출물 구성, 사용 순서, 금지 범위를 설명합니다.

### 2. 가장 쉬운 실행 요청

Claude Code 또는 Cowork에서 다음처럼 요청합니다.

```text
/kizzling-followup

submission/data/leads_sample.csv를 입력으로 사용해서
Basic, Standard, Challenge 산출물을 모두 생성해줘.
회사 맥락은 submission/context/company-info.md,
업계 맥락은 submission/context/industry-news.md를 참고해줘.
```

`kizzling-followup`은 전체 흐름을 조율하는 오케스트레이터 스킬입니다. 내부적으로 아래 스킬들을 순서대로 연결합니다.

```text
kizzling-analyze-leads
  -> kizzling-message-strategy
  -> kizzling-generate-emails
  -> kizzling-campaign-plan
  -> kizzling-review-submit
```

### 3. 단계별로 실행하는 방법

리드 데이터만 먼저 분석하고 싶을 때:

```text
/kizzling-analyze-leads

submission/data/leads_sample.csv를 분석해서
결측 이메일, 상담 메모 결측/모호 리드, 중복 리드,
직책/기관/관심기능/우선순위 분포를 정리해줘.
```

이메일 초안까지만 만들고 싶을 때:

```text
/kizzling-followup

Basic과 Standard 산출물까지만 생성해줘.
캠페인 기획안은 아직 만들지 않아도 돼.
```

캠페인 기획안까지 만들고 싶을 때:

```text
/kizzling-followup

Basic, Standard, Challenge 전체 산출물을 생성해줘.
특히 후속 캠페인 기획안 1~2건도 포함해줘.
```

최종 검수만 다시 하고 싶을 때:

```text
/kizzling-review-submit

submission/output/ 하위 산출물이
Basic, Standard, Challenge 요구사항을 모두 충족하는지 검수해줘.
```

### 4. 결과물 확인 위치

주요 결과물은 `output/`에서 확인합니다.

| 파일 | 용도 |
|---|---|
| `output/email_drafts.csv` | 리드별 이메일 초안. 컬럼은 `lead_id`, `subject`, `body`, `review_flag` |
| `output/basic_exception_summary.md` | 이메일 결측, 상담 메모 결측/모호, 중복 리드 예외 처리 요약 |
| `output/pipeline-usage.md` | 새 CSV가 들어왔을 때 같은 방식으로 다시 실행하는 방법 |
| `output/email_draft_sample.md` | 파이프라인으로 생성한 대표 이메일 샘플 1부 |
| `output/campaign_plan.md` | Challenge 산출물인 후속 캠페인 기획안 |
| `output/campaign_plan_preview.html` | 캠페인 기획안 정적 HTML 미리보기 |
| `output/submission-summary.md` | Basic, Standard, Challenge 요구사항 대응표와 검수 결과 요약 |
| `output/quality_audit_report.md` | 이메일·캠페인·시각화 통합 품질 QA 결과 (최종 검수 판정 포함) |

### 5. review_flag 읽는 법

`review_flag`는 사람이 꼭 확인해야 하는 리드를 표시합니다.

```text
N = 바로 검토 가능한 일반 초안
Y = 발송 전 사람 검수 필요
```

`Y`가 붙는 대표 상황은 다음과 같습니다.

```text
이메일이 없음
상담 메모가 없음
상담 메모가 모호함
```

`review_flag = Y`는 제외한다는 뜻이 아닙니다. 자동 발송하지 말고 사람이 먼저 확인해야 한다는 뜻입니다.

### 6. 새 CSV로 다시 쓰는 방법

새 리드 CSV는 기존 샘플과 같은 컬럼 구조여야 합니다.

```text
lead_id
name
organization
org_type
title
email
consultation_note
interest_feature
follow_up_priority
```

그다음 이렇게 요청합니다.

```text
/kizzling-followup

새 CSV 파일은 [새 파일 경로]야.
기존 submission/data/leads_sample.csv와 같은 스키마로 보고,
Basic, Standard, Challenge 산출물을 다시 생성해줘.
```

### 7. 한 줄 요약

처음 쓰는 사람은 아래 요청으로 시작하면 됩니다.

```text
/kizzling-followup

submission/data/leads_sample.csv와 submission/context/의 두 문서를 참고해서
키즐링 후속 이메일 자동화의 Basic, Standard, Challenge 산출물을 모두 생성하고 검수해줘.
```

## 빠른 확인

| 구분 | 확인 파일 |
|---|---|
| Basic 이메일 초안 | `output/email_drafts.csv` |
| Basic 예외 처리 | `output/basic_exception_summary.md` |
| Standard Skill 체인 | `.claude/skills/` |
| Standard 사용법 | `output/pipeline-usage.md` |
| Standard 이메일 샘플 | `output/email_draft_sample.md` |
| Challenge 캠페인 기획안 | `output/campaign_plan.md` |
| Challenge 시각화 | `output/campaign_plan_preview.html` |
| 최종 검수·품질 QA | `output/quality_audit_report.md` |
| 제출 요약 | `output/submission-summary.md` |
| 설계 근거 | `evidence/design-rationale.md` |
| 평가 매핑 | `evidence/evaluation-mapping.md` |

## Skill 체인

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

Standard만 확인할 때는 `kizzling-campaign-plan`과 `kizzling-visualize-campaign`을 제외할 수 있습니다. 단 `kizzling-quality-audit`은 항상 마지막에 실행합니다.

## 포함 파일

- `.claude/skills/`: 최종 재현 파이프라인 Skill 8개
- `data/`: 제공 입력 CSV
- `context/`: 회사/업계 맥락
- `output/`: 직접 생성한 제출 산출물
- `evidence/`: 판단, 설계, 평가 대응 요약

## 제외 파일

다음은 최종 제출 패키지에서 제외했습니다.

- `키즐링/scripts/`
- `sample-basic.html`, `sample-standard.html`, `sample-challenge.html`
- `template.md`
- `docs/references/`
- `out/`

## 제약 준수

- 별도 API 키 없음
- 이메일 실제 발송 없음
- SMTP/Gmail API 없음
- CRM 연동 없음
- 다국어 이메일 없음
- 리드 스코어링 없음
- API 키·외부 발송 연동 없음

## 추가 완성도 산출물

- `output/campaign_plan_preview.html`: 캠페인 기획안을 정적 HTML로 시각화한 미리보기입니다.
- `output/quality_audit_report.md`: 이메일 초안, 캠페인 기획안, HTML 시각화, 금지 범위를 한 번에 검수한 QA 리포트입니다.
