# Standard Validation Summary

- 새 CSV 입력 가능성: 동일 스키마 CSV를 `skills/kizzling-followup`이 조율하는 기능별 스킬 체인 입력으로 제공해 재현 가능 (스크립트·assets·코드 의존성 없음)
- 출력 행 수: 49
- 본문 길이 범위: 250~279자 (한국어, 공백 포함 — 250~400 규격 충족)
- `review_flag = Y`: L009, L012, L015, L033, L046
- 중복 제외: L050 (대표 L039)
- 출력 스키마: `lead_id`, `subject`, `body`, `review_flag`
- 파이프라인 샘플: `output/email_draft_sample.md`

## 재현 파이프라인 (스킬 체인)

```text
kizzling-analyze-leads
  -> kizzling-message-strategy
  -> kizzling-generate-emails
  -> kizzling-review-submit
```

## 검증 결과

- 출력 스키마 4컬럼·순서(lead_id, subject, body, review_flag): 통과
- 본문 250~400자 전건 충족(실측 250~279): 통과
- 개인화 4요소 순서(인사 → 상담언급 → 키즐콘 제품연결 → CTA 1개): 통과
- 직책별 제목·소구점·CTA 차별화(원장=무료 데모 신청 / 팀장=기술 도입 미팅 / 사업개발=파트너십 제안서 송부): 통과
- 우선순위별 CTA 강도(상=48시간 내 즉시 / 중=일정 조율·자료 / 하=소개자료·장기 너처링): 통과
- `review_flag` 정확도(상담 메모 결측·모호 + 이메일 결측 = Y): 통과
- 이메일 결측 리드(L009) 연락처 확인 메모 전환, 세일즈 CTA 없음: 통과
- 중복 리드(L050) 제외 기록: 통과
- 스크립트·패딩 의존 제거(고정 인사말·필러 문장 0건): 통과
