# Basic Exception Summary

- 입력 파일: `data/leads_sample.csv` (해커톤 제공 더미 데이터, 원본 50행)
- 출력 파일: `output/email_drafts.csv` (49행)
- 생성 방식: 스킬 체인 `kizzling-analyze-leads → kizzling-message-strategy → kizzling-generate-emails` (스크립트·외부 assets 비의존)
- 검수 필요 리드 (`review_flag = Y`, 5건): L009, L012, L015, L033, L046
- 중복 제외: L050 (대표 리드 L039 유지)

## 검수 필요 사유

- **이메일 주소 누락 (1건)**: L009 — 발송 불가. 발송용 이메일 대신 연락처 확인용 후속 메모로 전환(세일즈 CTA 없음), 제목에 `[검수 필요]` 표기.
- **상담 메모 누락 (3건)**: L012, L015, L046 — 상담 내용을 지어내지 않고 일반화, 발송 전 담당자 보강 필요.
- **상담 메모 모호 (1건)**: L033 — 구체적 니즈 불명확, 발송 전 담당자 보강 필요.

## 중복 처리

- L050 = L039 (`name`·`organization`·`consultation_note` 등 내용 동일) → L039를 대표로 유지하고 L050은 초안 생성 대상에서 제외. 실질 처리 49건.

## 참고 (데이터 정합)

- 발제 원문 설명은 상담 메모 결측을 2건으로 기술하나, 제공된 `leads_sample.csv`의 실제 결측은 3건(L012·L015·L046)이다. 구현·검수는 실제 CSV를 기준으로 하며, `review_flag = Y`는 상담 메모 결측·모호 4건에 이메일 결측 1건(L009)을 더해 총 5건이다.
