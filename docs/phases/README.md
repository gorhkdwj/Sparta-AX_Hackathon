# Phase 계획 관리

이 폴더는 키즐링 박람회 리드 맞춤 후속 이메일 자동화 과제를 Phase별로 관리한다. 목표는 Basic, Standard, Challenge 요구사항을 빠짐없이 구현하고, 제출자가 전체 진행 상황과 산출물을 한눈에 확인할 수 있게 하는 것이다.

## 전체 구조

| Phase | 문서 | 핵심 목표 | 주요 산출물 |
|---|---|---|---|
| Phase 0 | `phase-0-alignment.md` | 발제 기준과 제출 범위 고정 | 최종 산출물 체크리스트, 범위/금지 범위, 정합성 확인 결과 |
| Phase 1 | `phase-1-data-analysis.md` | 리드 데이터 구조와 예외 케이스 분석 | 데이터 분석 요약, 예외 리드 목록, 세그먼트 후보 |
| Phase 2 | `phase-2-message-strategy.md` | 직책별 메시지·CTA·review_flag 기준 설계 | 메시지 전략, 설계 근거, 이메일 생성 규칙 |
| Phase 3 | `phase-3-basic-email-drafts.md` | Basic 이메일 초안 산출 | `email_drafts.csv`, 예외 요약, 공개 링크 준비 |
| Phase 4 | `phase-4-standard-pipeline.md` | Standard 기능별 Skill 체인 구성 | 스킬 사용법, 이메일 샘플 1부, 재현 기준 |
| Phase 5 | `phase-5-challenge-campaign.md` | Challenge 캠페인 기획안 스킬화 | 캠페인 기획안 샘플 1~2건 |
| Phase 6 | `phase-6-review-submission.md` | 검수와 제출 패키징 | 검수 리포트, 제출 요약, 미검증 범위 |
| Phase 7 | `phase-7-quality-visualization.md` | 추가 완성도 강화 | 캠페인 HTML 미리보기, 품질 QA 리포트, QA 스킬 |

## 진행 원칙

- Phase 0~2는 기준과 설계 단계다. 산출물 품질을 흔들리지 않게 고정한다.
- Phase 3~5는 발제의 Basic, Standard, Challenge와 직접 대응하며, Phase 4 이후 최종 구현 방식은 기능별 `kizzling-*` Skill 체인이다.
- Phase 6은 전체 요구사항이 누락 없이 충족됐는지 검수하고 제출 형태로 정리한다.
- Phase 7은 요구사항 이상의 전달력과 안정성을 위해 캠페인 시각화와 실행 사이클 마지막 QA를 추가한다.
- 각 Phase 완료 시 `Worklog.md`에 변경 파일, 검증 결과, 남은 작업을 남긴다.
- 방향을 바꾸는 결정은 `Decisionlog.md`와 필요 시 `키즐링/decisions.md`에 기록한다.

## Phase 간 전달 흐름

```text
Phase 0 기준 고정
  -> Phase 1 데이터 분석
  -> Phase 2 메시지 전략 설계
  -> Phase 3 Basic 이메일 초안 생성
  -> Phase 4 Standard Skill 체인화
  -> Phase 5 Challenge 캠페인 Skill화
  -> Phase 6 검수와 제출 패키징
  -> Phase 7 시각화와 품질 QA
```

## 공통 문서 형식

각 Phase 문서는 다음 항목을 포함한다.

- 목표
- 입력 자료
- 수행 계획
- 산출물
- 완료 기준
- 검증 기준
- 다음 Phase 전달물
- 리스크와 대응
