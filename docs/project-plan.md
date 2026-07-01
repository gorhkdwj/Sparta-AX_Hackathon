# 프로젝트 기획 · Sparta_AX_Project

## 문제 정의

키즐링 영업팀은 교육 박람회에서 수집한 리드 50건을 48시간 골든타임 안에 후속해야 한다. 하지만 현재는 담당자 1인이 리드별 이메일을 수작업으로 작성하고, 직책별 관심사와 부스 상담 맥락이 충분히 반영되지 않아 전환 기회를 놓칠 위험이 크다.

이 프로젝트는 `leads_sample.csv`를 기반으로 직책별 소구점이 반영된 개인화 이메일 초안을 만들고, 새 리드에도 재사용 가능한 파이프라인과 후속 캠페인 기획안까지 만드는 것을 목표로 한다.

## 목표와 성공 기준

- Basic 요구사항 100% 충족:
  - 리드별 이메일 초안 생성
  - 직책별 제목·소구점·CTA 차별화
  - 개인화 4요소 포함
  - `review_flag`와 이메일 결측·중복 예외 처리
  - 노션 또는 구글 시트 공개 링크 제출 준비와 접근 확인
- Standard 요구사항 100% 충족:
  - 새 CSV에도 재현 가능한 파이프라인 구성
  - `정제 → 직책 분기 → 초안 생성 → review_flag` 동일 스키마 재생성
  - 직책별 소구점, CTA, 우선순위별 강도, review_flag 기준 직접 설계
  - 마케팅·영업 관점의 설계 근거 1~2줄 설명
  - 파이프라인으로 생성한 이메일 초안 샘플 1부 제출
  - 채택 방식인 기능별 Skill 체인의 간단한 사용법 제공
- Challenge 요구사항 100% 충족:
  - 리드 패턴 기반 후속 캠페인 기획안까지 자동 생성
  - 후속 캠페인 기획안 샘플 1~2건 제출
  - 세그먼트, 근거 리드 건수와 인용, 후속 시퀀스, 우선순위 포함
  - 이메일 양식, review_flag 기준, 우선순위 판단 기준의 설계 근거 설명
- 추가 구현 완료 (Phase 7, 발제 요구사항 이상의 완성도):
  - 제출용 요약(`submission-summary.md`)에 검수 결과를 통합해 평가자가 빠르게 품질을 확인하게 한다. 별도 `review_report.md`는 두지 않고 `quality_audit_report.md` 하나로 통합했다.
  - 캠페인 기획안을 정적 HTML로 시각화해 세그먼트와 후속 시퀀스를 빠르게 이해하게 한다(`kizzling-visualize-campaign`).
  - 매 실행 사이클 마지막에 QA 스킬(`kizzling-quality-audit`)을 실행해 이메일·캠페인·시각화 산출물을 함께 점검한다.
  - 최종 제출 전용 폴더 `submission/`에 핵심 Skill, 데이터, 컨텍스트, output, evidence를 묶는다.

## 범위

- 포함:
  - `키즐링/data/leads_sample.csv` 분석
  - `키즐링/context/company-info.md`, `industry-news.md` 반영
  - `.claude/skills/kizzling-followup/SKILL.md`와 기능별 `kizzling-*` 스킬 체인 구성
  - `email_drafts.csv/.xlsx` 생성
  - 재현 파이프라인 정리와 간단한 사용법
  - 파이프라인 생성 이메일 초안 샘플 1부
  - 자동 생성되는 캠페인 기획안과 샘플 1~2건
  - 캠페인 기획안 HTML 미리보기
  - 실행 사이클 마지막 품질 QA 리포트
  - 검수 리포트와 의사결정 기록
- 제외:
  - 실제 이메일 발송
  - CRM 연동
  - 다국어 이메일
  - 리드 스코어링
  - API 키·외부 발송 연동

## 주요 사용자와 사용 시나리오

- 주요 사용자: 키즐링 영업·마케팅 담당자
- 사용 시나리오:
  - 박람회 종료 직후 리드 CSV를 넣는다.
  - 직책별로 개인화된 후속 이메일 초안을 일괄 생성한다.
  - 검토가 필요한 리드는 `review_flag`로 분리한다.
  - 우선순위와 세그먼트별 후속 캠페인 시퀀스를 확인한다.

## 산출물

- `키즐링/output/email_drafts.csv` 또는 `.xlsx`
- `.claude/skills/kizzling-followup/SKILL.md` 최종 오케스트레이터 Skill
- `.claude/skills/kizzling-analyze-leads/SKILL.md`
- `.claude/skills/kizzling-message-strategy/SKILL.md`
- `.claude/skills/kizzling-generate-emails/SKILL.md`
- `.claude/skills/kizzling-campaign-plan/SKILL.md`
- `.claude/skills/kizzling-visualize-campaign/SKILL.md`
- `.claude/skills/kizzling-review-submit/SKILL.md`
- `.claude/skills/kizzling-quality-audit/SKILL.md`
- 노션 또는 구글 시트 공개 링크 제출 준비 메모
- `키즐링/output/pipeline-usage.md` 또는 동등한 파이프라인 사용법
- `키즐링/output/email_draft_sample.md` 또는 제출용 이메일 초안 샘플 1부
- `키즐링/output/campaign_plan.md` 또는 동등한 자동 생성 캠페인 기획안 샘플 1~2건
- `키즐링/output/campaign_plan_preview.html` 캠페인 기획안 HTML 미리보기
- `키즐링/output/review_report.md` 검수 리포트
- `키즐링/output/quality_audit_report.md` 품질 QA 리포트
- `키즐링/output/submission-summary.md` 제출용 요약 문서
- `submission/` 최종 제출 패키지
- `키즐링/decisions.md`와 루트 `Decisionlog.md`의 주요 결정 기록

## 일정·마일스톤

| 단계 | 목표 | 완료 조건 |
|---|---|---|
| S1 | 기준 문서 정비 | 루트 문서가 발제 기준과 일치 |
| S2 | 데이터·컨텍스트 분석 | 리드 분포, 결측, 중복, 도메인 맥락 확인 |
| S3 | 전략 설계 | 직책별 소구점·CTA·review_flag·우선순위 기준 확정 |
| S4 | Basic 산출물 생성 | `email_drafts.csv/.xlsx` 생성 |
| S5 | Standard 파이프라인 정리 | 새 CSV 재사용 흐름과 사용법, 이메일 샘플 1부 완성 |
| S6 | Challenge 캠페인 자동 생성 | 자동 생성 캠페인 기획안 샘플 1~2건 완성 |
| S7 | 검수·제출 패키징 | 채점 기준 통과 여부와 제출 파일 확인 |
| S7-1 | 시각화·품질 QA 확장 | 캠페인 HTML 미리보기와 매 실행 사이클 마지막 통합 QA 완성 (Phase 7) |

세부 Phase별 실행 계획은 `docs/phases/README.md`에서 관리한다.
최종 제출 패키지의 파일 구조와 요구사항별 확인 경로는 `docs/final-deliverables-structure.md`에서 관리한다.

| Phase | 대응 단계 | 문서 |
|---|---|---|
| Phase 0 | 기준 정렬 | `docs/phases/phase-0-alignment.md` |
| Phase 1 | 데이터 분석 | `docs/phases/phase-1-data-analysis.md` |
| Phase 2 | 메시지 전략 | `docs/phases/phase-2-message-strategy.md` |
| Phase 3 | Basic 산출물 | `docs/phases/phase-3-basic-email-drafts.md` |
| Phase 4 | Standard 파이프라인 | `docs/phases/phase-4-standard-pipeline.md` |
| Phase 5 | Challenge 캠페인 | `docs/phases/phase-5-challenge-campaign.md` |
| Phase 6 | 검수·제출 | `docs/phases/phase-6-review-submission.md` |
| Phase 7 | 시각화·품질 QA | `docs/phases/phase-7-quality-visualization.md` |

## 리스크와 대응

- 이메일 본문이 일반적일 위험: `company-info.md`의 키즐콘 기능과 직책별 소구점을 필수 반영한다.
- 캠페인 기획안이 근거 없이 보일 위험: 실제 리드 건수·인용과 `industry-news.md`의 업계 맥락을 함께 연결한다.
- 자동 생성 품질 편차: `kizzling-review-submit` 기준과 별도 검수 리포트로 누락을 잡는다.
- 개인정보·발송 위험: 실제 발송 금지, 초안 생성과 사람 검토까지로 범위를 제한한다.
