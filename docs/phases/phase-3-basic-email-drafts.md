# Phase 3 · Basic 이메일 초안 생성

## 목표

발제의 Basic 요구사항을 충족하는 `email_drafts.csv/.xlsx`를 생성한다.

## 입력 자료

- `키즐링/data/leads_sample.csv`
- Phase 1 데이터 분석 요약
- Phase 2 메시지 전략
- `.claude/skills/kizzling-generate-emails/SKILL.md`
- `.claude/skills/kizzling-review-submit/SKILL.md`
- 제공 참고 자료: `키즐링/.claude/skills/generate.md`
- `키즐링/output/template.md`

## 수행 계획

1. 리드별 처리 대상을 확정한다.
2. 각 리드에 대해 직책별 제목을 생성한다.
3. 각 본문을 250~400자 한국어로 작성한다.
4. 본문에 4요소를 순서대로 포함한다.
   - 맞춤 인사
   - 부스 상담내용 언급
   - 직책별 소구점과 키즐콘 기능 연결
   - CTA 1개
5. 상담 메모 결측·모호 리드는 `review_flag = Y`로 표시한다.
6. 이메일 없는 리드는 `review_flag = Y`와 발송 불가 후속 메모로 전환한다.
7. 중복 리드는 한 건으로 처리하고 기준 lead_id와 제외 lead_id를 기록한다.
8. `email_drafts.csv` 또는 `.xlsx`를 `키즐링/output/`에 저장한다.
9. 노션 또는 구글 시트 공개 링크로 옮길 수 있는 제출 구조를 유지한다.

## 산출물

- `키즐링/output/email_drafts.csv`
- `키즐링/output/basic_exception_summary.md`
- `키즐링/output/public_link_prep.md`
- `.claude/skills/kizzling-followup/SKILL.md`

## 실행 결과

- 최종 생성 기준: `.claude/skills/kizzling-followup/SKILL.md`가 호출하는 기능별 Skill 체인 워크플로
- 로컬 검증 보조: `키즐링/scripts/generate_basic_email_drafts.py`를 사용했으나 최종 제출 파이프라인의 필수 의존성은 아니다.
- 원본 리드 수: 50
- 생성 행 수: 49
- 중복 제외: L050. L039를 대표 행으로 유지.
- `review_flag = Y`: L009, L012, L015, L033, L046
- 본문 길이 범위: 250~297자
- 산출물 인코딩: UTF-8 BOM CSV
- 공개 링크: 미생성. `키즐링/output/public_link_prep.md` 절차에 따라 Google Sheet 업로드 후 기록 필요.

## 완료 기준

- 컬럼이 `lead_id, subject, body, review_flag`다.
- 직책별 제목, 소구점, CTA가 차별화됐다.
- 모든 본문이 250~400자다.
- 개인화 4요소가 순서대로 포함됐다.
- review_flag와 예외 처리가 정확하다.

## 검증 기준

- `.claude/skills/kizzling-review-submit/SKILL.md`의 Basic 체크리스트를 통과한다.
- 이메일 결측, 상담 메모 결측·모호, 중복 리드 처리가 별도로 확인된다.
- 공개 링크 제출 전 접근 확인 항목이 남아 있다.

## 검증 결과

- 컬럼 순서 확인: `lead_id`, `subject`, `body`, `review_flag`
- 행 수 확인: 49행
- 본문 길이 확인: 모든 행 250~400자 범위 충족
- 검수 플래그 확인: L009, L012, L015, L033, L046만 `Y`
- 중복 처리 확인: L050은 `email_drafts.csv`에 포함되지 않음
- 한글 깨짐 확인: `???` 패턴 없음
- 미검증 범위: 실제 Google Sheet 공개 링크 접근성

## 다음 Phase 전달물

- Basic 이메일 초안 산출물
- 예외 처리 요약
- Standard 파이프라인 검증에 사용할 샘플

## 리스크와 대응

- 리스크: 이메일 없는 리드를 일반 이메일 초안처럼 처리할 수 있음.
- 대응: 이메일 결측은 `review_flag = Y`와 발송 불가 후속 메모로 고정한다.

## 상태

- 완료: Basic 이메일 초안 CSV 생성과 로컬 검증
- 다음 단계: Phase 4 Standard 재현 파이프라인 구성
