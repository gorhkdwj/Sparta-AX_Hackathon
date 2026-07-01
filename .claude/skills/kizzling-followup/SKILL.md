---
name: kizzling-followup
description: 키즐링 박람회 리드 후속 이메일 자동화의 전체 워크플로를 기능별 스킬 체인으로 조율한다. Basic, Standard, Challenge 제출물을 한 번에 만들거나 검수해야 할 때 사용한다. 리드 분석, 메시지 전략, 개인화 이메일 초안, review_flag 처리, 재사용 파이프라인 문서, 캠페인 기획안, 캠페인 시각화, 최종 검수와 품질 QA를 순서대로 연결한다.
---

# 키즐링 후속 이메일 오케스트레이터

키즐링 과제의 전체 흐름을 기능별 스킬 순서에 따라 실행한다. 이 스킬은 최상위 라우터이며, 별도 스크립트, assets, API, CRM, 이메일 발송 기능을 요구하지 않는다.

## 스킬 체인

다음 스킬을 단계별로 호출한다.

1. `kizzling-analyze-leads`
2. `kizzling-message-strategy`
3. `kizzling-generate-emails`
4. `kizzling-campaign-plan`
5. `kizzling-visualize-campaign`
6. `kizzling-review-submit`
7. `kizzling-quality-audit`

Basic만 필요하면 1~3단계를 실행한 뒤 6~7단계의 Basic 검수와 QA를 수행한다.
Standard는 1~3단계에서 재사용 파이프라인 설명과 이메일 샘플을 만들고, 6~7단계에서 검수와 QA를 수행한다.
Challenge는 1~7단계를 모두 실행한다.
캠페인 시각화가 필요 없으면 5단계를 건너뛰되, 7단계 QA는 항상 마지막에 실행한다.

## 입력

다음 입력을 요구한다.

- 리드 CSV: `lead_id`, `name`, `organization`, `org_type`, `title`, `email`, `consultation_note`, `interest_feature`, `follow_up_priority`
- 키즐링 회사 맥락과 업계 맥락: 사용자가 제공하거나 작업공간에 있는 자료를 사용한다.

## 단계별 계약

### 1단계 출력: 리드 분석

반드시 다음 내용을 만든다.

- 전체 행 수와 필수 컬럼 확인
- `title`, `org_type`, `interest_feature`, `follow_up_priority` 분포
- 이메일 결측 리드
- 상담 메모 결측 또는 모호 리드
- 중복 그룹과 유지/제외할 `lead_id`

결과를 `kizzling-message-strategy`로 넘긴다.

### 2단계 출력: 메시지 전략

반드시 다음 내용을 만든다.

- 직책별 소구점
- 제목 패턴
- CTA 매핑
- 우선순위별 CTA 강도
- `review_flag` 기준
- 중복과 이메일 결측 처리 정책

결과를 `kizzling-generate-emails`로 넘긴다.

### 3단계 출력: 이메일 초안 패키지

반드시 다음 내용을 만든다.

- 정확히 `lead_id`, `subject`, `body`, `review_flag` 컬럼만 가진 `email_drafts.csv`
- Basic 예외 처리 요약
- Standard 파이프라인 사용법
- 이메일 초안 샘플 1부

Challenge가 요청되면 `kizzling-campaign-plan`으로 넘기고, 아니면 `kizzling-review-submit`과 `kizzling-quality-audit`으로 넘긴다.

### 4단계 출력: 캠페인 기획안

캠페인 기획안 1~2건을 만들고, 각 기획안에 다음 내용을 포함한다.

- 세그먼트 정의
- 리드 수와 `lead_id`
- 대표 상담 인용
- 후속 시퀀스
- 우선순위와 근거
- 담당자 실행 액션

결과를 `kizzling-visualize-campaign`으로 넘긴다. 시각화가 필요 없으면 `kizzling-review-submit`으로 넘긴다.

### 5단계 출력: 캠페인 시각화

요청되었거나 Challenge 완성도 보강이 필요하면 다음 내용을 가진 정적 HTML을 만든다.

- 캠페인별 세그먼트 요약
- 근거 리드와 대표 인용
- Day 0, Day 2~3, Day 7 후속 시퀀스
- `review_flag` 또는 사람 검수 필요 리드 표시
- 우선순위 근거 요약

결과를 `kizzling-review-submit`으로 넘긴다.

### 6단계 출력: 최종 검수

반드시 다음 내용을 만든다.

- 요구사항별 검수 결과
- 제출 요약
- 남은 미검증 항목
- 제외 범위 확인: 실제 발송 없음, CRM 없음, 리드 스코어링 없음, 다국어 없음, API 키 없음

결과를 `kizzling-quality-audit`으로 넘긴다.

### 7단계 출력: 품질 QA

매 실행 사이클 마지막에 반드시 수행한다.

- 이메일 초안만 만든 경우 Basic/Standard QA를 수행한다.
- 캠페인 기획안이 있으면 Challenge QA를 포함한다.
- HTML 시각화가 있으면 시각화 QA를 포함한다.
- 최종 금지 범위와 제출 구조를 다시 확인한다.

## 규칙

- 이메일을 실제로 발송하지 않는다.
- CRM에 연결하지 않는다.
- 외부 스크립트를 최종 필수 의존성으로 두지 않는다.
- 결측 또는 모호한 상담 메모에 구체적인 내용을 지어내지 않는다.
- 제공된 `follow_up_priority` 외의 리드 점수를 새로 만들지 않는다.
- 경로와 제출 참조는 상대경로로 작성한다.
