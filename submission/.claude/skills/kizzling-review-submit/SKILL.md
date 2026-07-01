---
name: kizzling-review-submit
description: 키즐링 해커톤 제출물을 최종 검수하고 패키징한다. Basic, Standard, Challenge 요구사항 검증, 캠페인 시각화 확인, 요구사항 매핑, 제출 요약, 공개 링크 준비, 미검증 범위, 금지 범위 확인이 필요할 때 사용한다. 상세 QA 체크리스트는 `kizzling-quality-audit`이 담당한다.
---

# 키즐링 최종 검수와 제출 정리

키즐링 산출물을 Basic, Standard, Challenge 요구사항에 맞춰 검수하고 최종 제출용 handoff를 만든다.

## Basic 검수

다음을 확인한다.

- `email_drafts.csv` 컬럼이 정확히 `lead_id`, `subject`, `body`, `review_flag`인지
- 모든 본문이 한국어 250~400자인지
- 본문 순서가 인사 → 상담언급 → 제품연결 → CTA인지
- 제목이 직책별로 다른지
- CTA가 직책별로 다른지
- `review_flag`가 정확한지
- 이메일 결측 행을 발송 준비 완료 상태로 취급하지 않았는지
- 중복 제외가 문서화되었는지

## Standard 검수

다음을 확인한다.

- 같은 스키마의 새 CSV에도 재사용 가능한 파이프라인인지
- 파이프라인이 Skill 기반이며 스크립트, assets, 코드 의존성을 요구하지 않는지
- 스킬 체인이 문서화되었는지
- 파이프라인으로 생성한 이메일 샘플 1부가 있는지
- 직책별 소구점, CTA 규칙, 우선순위별 강도, review_flag 근거가 설명되었는지

## Challenge 검수

다음을 확인한다.

- 캠페인 기획안 샘플이 1~2건인지
- 각 샘플에 세그먼트 정의가 있는지
- 각 샘플에 리드 수와 `lead_id`가 있는지
- 각 샘플에 대표 상담 인용이 있는지
- 각 샘플에 후속 시퀀스가 있는지
- 각 샘플에 우선순위와 근거가 있는지
- 각 샘플에 담당자 액션이 있는지

## 시각화 확인

`campaign_plan_preview.html`이 있으면 다음을 확인한다.

- 캠페인 세그먼트와 후속 시퀀스가 쉽게 읽히는지
- 근거 리드와 `review_flag` 주의 리드가 표시되는지
- 실제 발송, CRM 연결, 리드 스코어링 기능이 들어가지 않았는지

## 제외 범위 확인

다음을 확인한다.

- 실제 이메일 발송 없음
- CRM 연동 없음
- 다국어 이메일 생성 없음
- 제공된 `follow_up_priority` 외 리드 스코어링 없음
- 실제 고객 데이터 없음

## 출력

다음 내용을 생성한다.

- `submission-summary.md` 내용
- `public_link_prep.md` 내용 (구글 시트/노션 공개 링크 업로드 절차와 완료 상태)
- 요구사항별 확인 파일 매핑
- 남은 미검증 범위

위 Basic/Standard/Challenge/시각화/제외 범위 확인 결과의 상세 체크리스트는 별도 리포트로 만들지 않고, `kizzling-quality-audit`이 만드는 `quality_audit_report.md` 하나로 통합한다.
