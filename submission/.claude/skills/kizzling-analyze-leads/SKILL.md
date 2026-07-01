---
name: kizzling-analyze-leads
description: 키즐링 박람회 리드 CSV를 분석하는 1단계 스킬이다. CSV 구조 확인, 직책/기관/관심 기능/후속 우선순위 분포, 이메일 결측, 상담 메모 결측·모호, 중복 리드 처리, review_flag 후보 식별이 필요할 때 사용한다.
---

# 키즐링 리드 분석

제공된 키즐링 리드 CSV를 분석하고, 다음 단계의 메시지 전략 스킬이 바로 사용할 수 있는 간결한 handoff를 만든다. 이 스킬에서는 이메일 문안을 생성하지 않는다.

## 필수 컬럼

다음 컬럼이 있는지 확인한다.

`lead_id`, `name`, `organization`, `org_type`, `title`, `email`, `consultation_note`, `interest_feature`, `follow_up_priority`

## 분석 항목

다음 내용을 보고한다.

- 전체 행 수
- 필수 컬럼 존재 여부
- `title` 분포
- `org_type` 분포
- `interest_feature` 분포
- `follow_up_priority` 분포
- 이메일 결측 행
- 상담 메모 결측 행
- 상담 메모 모호 행
- `lead_id`를 제외한 의미 있는 필드가 모두 같은 완전 중복 행

## 탐지 기준

이메일 결측:

- `email` 값이 비어 있는 경우

상담 메모 결측:

- `consultation_note` 값이 비어 있는 경우
- `consultation_note`가 `상담 메모 없음`, `없음` 또는 이에 준하는 결측 표현인 경우

상담 메모 모호:

- `consultation_note`에 `애매`, `모호`, `구체적 니즈 파악 안 됨` 같은 표현이 있거나, 관심만 있고 구체적 니즈가 없는 경우

중복:

- `name`, `organization`, `title`, `email`, `consultation_note`, `interest_feature`가 모두 같으면 중복으로 본다.
- 첫 번째 `lead_id`를 기준 리드로 유지하고, 이후 중복 리드는 이메일 초안 생성 대상에서 제외한다.

## 출력 형식

다음 형식으로 작성한다.

```text
=== 리드 분석 전달 메모 ===
행 수:
필수 컬럼:
분포:
이메일 결측:
상담 메모 결측:
상담 메모 모호:
중복:
review_flag 후보:
기준/제외 리드 정책:
다음 스킬 참고 사항:
```

다음 스킬: `kizzling-message-strategy`.
