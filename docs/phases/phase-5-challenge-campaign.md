# Phase 5 · Challenge 캠페인 자동 생성

## 목표

Standard 파이프라인에 이어 리드 데이터에서 발견한 패턴을 기반으로 후속 캠페인 기획안까지 자동 생성하고, 샘플 1~2건을 제출물로 만든다.

## 입력 자료

- Phase 1 데이터 분석 요약
- Phase 2 메시지 전략
- Phase 4 파이프라인 기준
- `.claude/skills/kizzling-campaign-plan/SKILL.md`
- `키즐링/context/industry-news.md`
- `키즐링/context/company-info.md`

## 수행 계획

1. `kizzling-campaign-plan` 스킬의 입력·출력 계약을 기준으로 캠페인 생성 단계를 정의한다.
2. 리드 패턴을 분석한다.
   - title
   - org_type
   - interest_feature
   - follow_up_priority
   - consultation_note 키워드
3. 캠페인 세그먼트 1~2개를 도출한다.
4. 각 세그먼트의 근거 리드 건수와 lead_id를 정리한다.
5. 대표 상담 인용을 선정한다.
6. 후속 시퀀스를 설계한다.
   - Day0 개인화 초안
   - Day2~3 보강 자료 또는 사례
   - Day7 미팅·데모·제안 후속
7. 우선순위와 판단 근거를 작성한다.
8. 이메일 양식, review_flag 기준, 우선순위 판단 기준의 설계 근거를 함께 설명한다.

## 산출물

- `키즐링/output/campaign_plan.md` 또는 동등한 캠페인 기획안
- 자동 생성 캠페인 샘플 1~2건
- 캠페인 생성 기준 설명
- `.claude/skills/kizzling-campaign-plan/SKILL.md`와의 대응 설명

## 완료 기준

- 캠페인 기획안이 파이프라인의 자동 생성 단계로 포함됐다.
- 캠페인 기획안이 기능별 Skill 체인에서 `kizzling-campaign-plan` 단계로 생성된다.
- 각 샘플에 세그먼트 정의, 근거 리드, 대표 인용, 후속 시퀀스, 우선순위가 있다.
- 영업팀이 바로 실행할 수 있을 만큼 구체적이다.
- `industry-news.md`의 골든타임·개인화·Human-in-the-loop 맥락과 연결된다.

## 검증 기준

- 발제의 Challenge 필수 항목을 모두 충족한다.
- 근거 리드 없이 캠페인 아이디어만 제안하지 않는다.
- follow_up_priority를 새 점수로 재계산하지 않는다.

## 다음 Phase 전달물

- 캠페인 기획안 샘플 1~2건
- 캠페인 생성 기준
- 검수 리포트에 포함할 Challenge 검증 결과

## 리스크와 대응

- 리스크: 캠페인 기획안이 일반론처럼 보일 수 있음.
- 대응: 반드시 lead_id, 건수, 상담 인용을 포함하고, 각 액션을 Day 단위 시퀀스로 작성한다.
