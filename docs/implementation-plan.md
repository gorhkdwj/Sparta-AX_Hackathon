# 구현 계획 · 키즐링 리드 후속 이메일 자동화

> 처음부터 전체를 한 번에 달리지 않되, 최종 목표는 Basic, Standard, Challenge 전 요구사항 충족이다.

## 단계 개요

| 단계 | 목표 | 완료 조건 | 검증 방법 | 의존/연결 |
|---|---|---|---|---|
| S1 | 구조 문서 정비 | 루트 문서가 발제 기준과 일치 | `rg`로 이전 골격 문구 확인 | - |
| S2 | 데이터 분석 | 50건 분포, 결측, 모호, 중복 확인 | `kizzling-analyze-leads` 기준으로 수량 대조 | S1 |
| S3 | 컨텍스트 반영 | 회사·업계 맥락을 생성 규칙에 반영 | 소구점·CTA·금지 원칙 대조 | S2 |
| S4 | 전략 설계 | 직책별 소구점, CTA, review_flag, 우선순위 기준 확정 | `requirements-contract.md`와 decisions 기록 확인 | S3 |
| S5 | Basic 산출물 생성 | `email_drafts.csv/.xlsx` 생성 | 개인화 4요소, 250~400자, 예외 처리 검사 | S4 |
| S6 | Standard 스킬 체인화 | 새 CSV 재사용 절차, 사용법, 이메일 샘플 1부 완성 | 기능별 Skill 체인과 Basic 출력 재현성 확인 | S5 |
| S7 | Challenge 캠페인 스킬화 | 캠페인 기획안 샘플 1~2건 자동 생성 | 근거 리드·인용·시퀀스·우선순위 확인 | S6 |
| S7-1 | 시각화·품질 QA 확장 (Phase 7) | 캠페인 HTML 미리보기와 매 실행 사이클 마지막 통합 QA 완성 | `kizzling-visualize-campaign`, `kizzling-quality-audit` 산출물 확인 | S7 |
| S8 | 최종 검수·제출 패키징 | 검수 리포트와 제출 요약 완료 | 발제 채점표와 산출물 대조 | S7-1 |

## S2 · 데이터 분석

- 왜 필요한가: 이메일 초안 생성 전 데이터 품질과 분포를 알아야 예외 처리와 캠페인 세그먼트를 정할 수 있다.
- 입력: `키즐링/data/leads_sample.csv`
- 수행:
  - 전체 행 수와 컬럼 확인
  - title, org_type, interest_feature, follow_up_priority 분포 집계
  - 이메일 결측 확인
  - 상담 메모 결측·모호 확인
  - 완전 중복 리드 확인
- 완료 조건: 분석 요약에 전체 리드, 실질 처리 건수, review_flag 예상 건수, 중복 정보가 포함된다.
- 검증 방법: `.claude/skills/kizzling-analyze-leads/SKILL.md` 기준과 대조한다.

## S3 · 컨텍스트 반영

- 왜 필요한가: 이메일이 단순 템플릿이 아니라 키즐링·키즐콘 맥락에 맞아야 한다.
- 필수 참고:
  - `키즐링/context/company-info.md`
  - `키즐링/context/industry-news.md`
- 반영 항목:
  - 키즐콘 기능: 대회 접수, 결제, 심사, 결과발표, 콘텐츠 안전 필터
  - 직책별 소구점과 CTA
  - 48시간 골든타임
  - AI 개인화와 Human-in-the-loop
  - 데이터 품질 이슈와 수신 동의 주의
- 완료 조건: 생성 규칙과 캠페인 근거에 위 맥락이 반영된다.

## S4 · 전략 설계

- 왜 필요한가: Standard와 Challenge는 “본인 설계”가 평가 대상이다.
- 수행:
  - 원장, 팀장, 사업개발별 제목·소구점·CTA 설계
  - `follow_up_priority`별 CTA 강도 설계
  - `review_flag` 기준 확정
  - 이메일 결측과 중복 처리 원칙 확정
- 완료 조건: `키즐링/decisions.md` 또는 `Decisionlog.md`에 주요 판단이 기록된다.
- 검증 방법: `.claude/skills/kizzling-message-strategy/SKILL.md`와 발제 채점표 대조.

## S5 · Basic 산출물 생성

- 왜 필요한가: 모든 상위 단계의 기반은 리드별 이메일 초안이다.
- 출력: `키즐링/output/email_drafts.csv` 또는 `.xlsx`
- 생성 규칙:
  - 컬럼은 `lead_id, subject, body, review_flag`
  - body는 250~400자
  - body는 인사 → 상담언급 → 제품연결 → CTA 순서
  - 개인화 4요소 포함
  - CTA는 1개만 사용
  - 직책별 제목·본문 톤 차별화
  - 직책별 CTA 고정: 원장=무료 데모 신청, 팀장=기술 도입 미팅, 사업개발=파트너십 제안서 송부
  - 결측·모호 상담 메모는 `review_flag = Y`
  - 이메일 없는 리드는 `review_flag = Y`와 발송 불가 후속 메모로 처리
  - 중복 리드는 한 건으로 처리하고 기준 lead_id와 제외 lead_id 기록
- 제출 준비:
  - 노션 페이지 또는 구글 시트 공개 링크로 옮길 수 있는 구조를 유지
  - 공개 링크 접근 가능 여부를 최종 검수 항목으로 둠
- 검증 방법: `.claude/skills/kizzling-generate-emails/SKILL.md`, `.claude/skills/kizzling-review-submit/SKILL.md` 기준으로 검사.

## S6 · Standard 스킬 체인화

- 왜 필요한가: 1회성 초안이 아니라 새 박람회 리드에도 재사용 가능해야 한다.
- 기본 흐름:
  - Standard: `kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails → kizzling-review-submit → kizzling-quality-audit`
  - Challenge 포함: `kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails → kizzling-campaign-plan → kizzling-visualize-campaign → kizzling-review-submit → kizzling-quality-audit`
- 구현 선택:
  - 최종 제출 파이프라인은 `.claude/skills/kizzling-followup/SKILL.md`가 기능별 `kizzling-*` 스킬을 순차 호출하는 구조로 둔다.
  - 별도 `py`, assets, 외부 API는 최종 필수 의존성으로 두지 않는다.
  - 기존 `키즐링/.claude/skills/*.md`와 `키즐링/scripts/`는 참고·검증 보조물로만 취급한다.
- 필수 산출:
  - 스킬 체인 사용법: `키즐링/output/pipeline-usage.md` 또는 동등 문서
  - 파이프라인으로 생성한 이메일 초안 샘플 1부
  - 직책별 소구점·CTA·우선순위별 강도 설계 근거 1~2줄
  - `정제 → 직책 분기 → 초안 생성 → review_flag`가 동일 품질로 재생성된다는 설명
- 완료 조건: 새 CSV 입력 시 어떤 스킬 체인으로 동일 스키마의 이메일 초안과 review_flag를 만드는지 문서화되어 있고, 전체 제출 흐름에서는 캠페인 기획안까지 이어진다.

## S7 · Challenge 캠페인 스킬화

- 왜 필요한가: Challenge는 이메일 초안 이후의 데이터 기반 후속 전략을 **자동 생성**하는 것이 핵심이다.
- 추가 스킬: `kizzling-campaign-plan`
- 수행:
  - `kizzling-analyze-leads` 결과에서 title, org_type, interest_feature, follow_up_priority 패턴 확인
  - `kizzling-message-strategy`의 소구점·CTA·우선순위 기준을 캠페인 생성 기준으로 재사용
  - 리드 패턴에서 세그먼트 1~2개 도출
  - 세그먼트별 근거 lead_id와 대표 상담 인용 정리
  - Day0, Day2~3, Day7 등 후속 시퀀스 설계
  - 우선순위와 판단 근거 작성
  - `industry-news.md`의 골든타임·개인화 효과·리드 너처링 맥락 연결
- 출력:
  - `키즐링/output/campaign_plan.md` 또는 동등한 제출용 캠페인 기획안
  - 샘플 1~2건. 각 샘플은 `세그먼트 정의 / 근거 리드(건수·인용) / 후속 시퀀스 / 우선순위`를 포함
- 완료 조건: 새 CSV에도 같은 기준으로 캠페인 기획안 샘플을 자동 생성할 수 있고, 영업팀이 바로 실행 가능한 수준이다.

## S7-1 · 시각화와 품질 QA 확장 (Phase 7)

- 왜 필요한가: Basic, Standard, Challenge 요구사항을 채운 뒤에도, 평가자가 캠페인 기획안을 더 빠르게 이해하고 사용자가 반복 실행 결과를 매번 안전하게 검수할 수 있어야 발제 요구사항 이상의 완성도가 된다.
- 추가 스킬: `kizzling-visualize-campaign`, `kizzling-quality-audit`
- 수행:
  - `kizzling-visualize-campaign`으로 캠페인 기획안을 세그먼트, 근거 리드, 대표 인용, Day 0/2~3/7 후속 시퀀스, 검수 필요 리드를 포함한 정적 HTML 미리보기로 변환
  - `kizzling-quality-audit`을 매 실행 사이클 마지막 단계로 고정해 이메일만 생성한 경우에도, 캠페인·시각화까지 생성한 경우에도 항상 실행
  - 기존에 `kizzling-review-submit`이 만들던 `review_report.md`와 QA 체크리스트가 중복이라 `quality_audit_report.md` 하나로 통합하고, `review-submit`은 `submission-summary.md`와 `public_link_prep.md`만 만들도록 역할을 조정
- 완료 조건: 최종 스킬 체인이 8개(`kizzling-followup` 포함)이고, 전체 흐름이 분석 → 전략 → 이메일 생성 → 캠페인 → 시각화 → 검수 → QA 순서로 설명된다.

## S8 · 최종 검수·제출 패키징

- 왜 필요한가: 평가자가 요구사항 충족 여부를 빠르게 확인할 수 있어야 한다.
- 수행:
  - 검수 리포트 작성
  - 예외 처리 요약 작성
  - Standard 이메일 초안 샘플 1부 확인
  - Challenge 캠페인 기획안 샘플 1~2건 확인
  - 제출용 요약 작성
  - 공개 링크 제출 흐름 정리
  - 문서 간 경로·용어·산출물명 정합성 확인
- 완료 조건: Basic, Standard, Challenge 채점 항목별 통과 여부가 명확히 보인다.
