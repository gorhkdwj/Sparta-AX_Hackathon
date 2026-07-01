# Sparta_AX_Project

> 스파르타 AX 해커톤 제출 프로젝트 — 키즐링 박람회 리드 맞춤 후속 이메일 자동화.

## 개요

- 목표: 키즐링 과제의 Basic, Standard, Challenge 요구사항을 모두 충족하고 그 이상의 완성도로 제출한다.
- 문제: 박람회 리드 50건의 후속 이메일을 48시간 골든타임 안에 직책별로 개인화해야 한다.
- 핵심 접근: 데이터 분석, 도메인 컨텍스트 반영, 직책별 소구점 설계, 이메일 초안 생성, 캠페인 기획, 검수까지 하나의 재현 가능한 흐름으로 만든다.

## 최우선 기준

- 발제: `docs/references/발제.md`
- 평가 기준: `docs/references/AX 해커톤 평가 기준.md`
- 문제 패키지: `키즐링/problem.md`, `키즐링/CLAUDE.md`
- 필수 컨텍스트:
  - `키즐링/context/company-info.md`
  - `키즐링/context/industry-news.md`

## 목표 산출물

- Basic: `키즐링/output/email_drafts.csv` 또는 `.xlsx`
  - 컬럼: `lead_id, subject, body, review_flag`
  - 본문: 인사 → 상담언급 → 제품연결 → CTA 순서, 한국어 250~400자, 개인화 4요소 포함
  - 제출: 노션 또는 구글 시트 공개 링크 접근 가능 상태
- Standard: 새 리드 CSV에도 재사용 가능한 파이프라인
  - 기준 흐름: `kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails → kizzling-campaign-plan → kizzling-visualize-campaign → kizzling-review-submit → kizzling-quality-audit`
  - Standard 검증 흐름: `kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails → kizzling-review-submit → kizzling-quality-audit`
  - 재현 기준: `정제 → 직책 분기 → 초안 생성 → review_flag`
  - 산출물: 파이프라인 사용법, 파이프라인으로 생성한 이메일 초안 샘플 1부
- Challenge: 리드 패턴 기반 후속 캠페인 기획안
  - 파이프라인이 캠페인 기획안까지 자동 생성
  - 산출물: `키즐링/output/campaign_plan.md` 또는 동등한 제출용 문서
  - 샘플 1~2건에 세그먼트 정의, 근거 리드, 대표 인용, 후속 시퀀스, 우선순위 포함
- 추가 완성도: 캠페인 HTML 미리보기, 품질 QA 리포트, 예외 처리 요약, 제출용 요약 문서
- 최종 제출 패키지: `submission/`

## 프로젝트 구조

- `CLAUDE.md`, `AGENTS.md` — 프로젝트 작업 헌법
- `docs/` — 프로젝트 계획, 기준 계약, 구현 계획, 검증 계획
- `docs/phases/` — Phase별 세부 실행 계획
- `docs/references/` — 발제와 평가 기준 등 원문 자료
- `.claude/skills/kizzling-followup/` — 전체 워크플로 오케스트레이터 스킬
- `.claude/skills/kizzling-*/` — 분석, 전략, 생성, 캠페인, 검수 기능별 스킬
- `키즐링/` — 실제 과제 패키지와 산출물
- `키즐링/data/leads_sample.csv` — 입력 리드 데이터
- `키즐링/context/` — 이메일과 캠페인 생성에 필요한 필수 맥락
- `키즐링/.claude/skills/` — 제공된 기존 커맨드형 파이프라인 참고 자료
- `키즐링/output/` — 제출 산출물 저장 위치
- `submission/` — 최종 제출 전용 패키지

## 실행 흐름 초안

1. `kizzling-analyze-leads`로 `키즐링/data/leads_sample.csv` 분석
2. `kizzling-message-strategy`로 도메인·업계 맥락과 직책별 전략 반영
3. `kizzling-generate-emails`로 `email_drafts.csv/.xlsx`, 예외 요약, 이메일 샘플 생성
4. `kizzling-campaign-plan`으로 리드 패턴 기반 캠페인 기획안 생성
5. `kizzling-visualize-campaign`으로 캠페인 기획안 HTML 미리보기 생성
6. `kizzling-review-submit`으로 검수 리포트와 제출용 요약 작성
7. `kizzling-quality-audit`으로 실행 사이클 마지막 품질 QA 수행
8. 공개 링크 준비와 미검증 범위 정리

## 제외 범위

- 실제 이메일 발송
- CRM 연동
- 다국어 이메일
- 리드 스코어링
- API 키·외부 발송 연동

## 문서

- 작업 규칙: `CLAUDE.md`, `AGENTS.md`
- 작업 이력: `Worklog.md`
- 주요 결정: `Decisionlog.md`
- 문제 해결: `Troubleshootinglog.md`
- 기준 계약: `docs/requirements-contract.md`
- 구현 계획: `docs/implementation-plan.md`
- 검증 계획: `docs/validation-plan.md`
- Phase 계획: `docs/phases/README.md`
- 최종 제출 구조: `docs/final-deliverables-structure.md`
- 제출 패키지 사용 가이드: `submission/README.md`
