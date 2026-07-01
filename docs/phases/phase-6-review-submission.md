# Phase 6 · 검수와 제출 패키징

## 목표

Basic, Standard, Challenge 산출물을 발제 채점표 기준으로 검수하고 제출 가능한 형태로 패키징한다.

## 입력 자료

- Phase 3 Basic 산출물
- Phase 4 Standard 파이프라인 산출물
- Phase 5 Challenge 캠페인 산출물
- `docs/validation-plan.md`
- `docs/final-deliverables-structure.md`
- `.claude/skills/kizzling-review-submit/SKILL.md`
- `docs/references/발제.md`

## 수행 계획

1. Basic 검수:
   - 필수 컬럼
   - 직책별 차별화
   - 개인화 4요소
   - 본문 250~400자
   - review_flag
   - 이메일 결측과 중복 처리
2. Standard 검수:
   - 기능별 Skill 체인 재현 절차
   - 스킬 사용법
   - 이메일 초안 샘플 1부
   - 설계 근거
3. Challenge 검수:
   - 캠페인 자동 생성 단계
   - 샘플 1~2건
   - 세그먼트, 근거 리드, 인용, 시퀀스, 우선순위
4. 제출 패키징:
   - `submission/` 폴더 생성
   - Skill 8개, 제공 CSV, 컨텍스트 2개, 직접 생성 output, evidence 요약만 포함
   - `sample-*.html`, `template.md`, `scripts/`, `docs/references/`, `out/` 제외
   - 제출 파일 목록 정리
   - `docs/final-deliverables-structure.md` 기준으로 요구사항별 확인 경로 정리
   - 노션 또는 구글 시트 공개 링크 접근 확인
   - `submission-summary.md` 작성
5. 미검증 범위를 명확히 기록한다.

## 산출물

- `키즐링/output/review_report.md` (Phase 6 시점 작업본. 이후 Phase 7에서 `quality_audit_report.md`로 검수 체크리스트가 통합되며 `submission/` 최종 패키지에는 포함하지 않는다)
- `키즐링/output/submission-summary.md`
- `submission/` 제출 패키지
- 제출 파일 목록
- 미검증 범위

> 참고: 최종 제출 패키지(`submission/output/`)는 별도 `review_report.md`를 두지 않는다. 검수 결과는 `submission-summary.md`의 "검수 결과" 절과 Phase 7의 `quality_audit_report.md`로 통합해 제공한다(중복 리포트 방지).

## 완료 기준

- Basic, Standard, Challenge 검증 항목이 모두 통과하거나 미검증 사유가 명확하다.
- 평가자가 산출물을 어디서 확인해야 하는지 한눈에 알 수 있다.
- 최종 제출 폴더 `submission/`에는 제출 대상 파일만 포함된다.
- 실제 이메일 발송, CRM 연동, 다국어, 리드 스코어링, API 키·외부 발송 연동을 수행하지 않았음이 명확하다.

## 검증 기준

- `docs/validation-plan.md` 체크리스트를 통과한다.
- `.claude/skills/kizzling-review-submit/SKILL.md` 기준으로 품질을 확인한다.
- 문서 간 경로, 용어, 산출물명이 일치한다.

## 다음 Phase 전달물

- 없음. 이 Phase가 최종 제출 전 정리 단계다.

## 리스크와 대응

- 리스크: 산출물은 만들어졌지만 평가자가 찾기 어려울 수 있음.
- 대응: `submission-summary.md`에 파일 경로, 공개 링크, 요구사항 대응표를 포함한다.
