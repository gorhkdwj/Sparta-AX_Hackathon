# /analyze — 리드 데이터 파악

## 목적
`data/leads_sample.csv`를 읽어 이메일 초안 생성 전 전체 현황과 데이터 품질을 파악한다.

## 실행 단계

### 1. CSV 파일 읽기
```
data/leads_sample.csv 파일을 읽고 전체 50행(헤더 제외)을 확인한다.
컬럼: lead_id, name, organization, org_type, title, email, consultation_note, interest_feature, follow_up_priority
```

### 2. 직책(title) 분포 집계
```
직책 분포:
- 원장: N명
- 팀장: N명
- 사업개발: N명
(스펙 기준: 원장 20 / 팀장 18 / 사업개발 12 = 50)
```

### 3. 관심제품(interest_feature)·기관유형(org_type)·우선순위 분포
```
interest_feature: 대회운영SaaS N / 콘텐츠안전필터 N / 파트너십 N
org_type: 학원 N / 학교 N / 에듀테크기업 N / 공공기관 N
follow_up_priority: 상 N / 중 N / 하 N
```

### 4. 이메일 결측 확인 (필수 예외 처리)
email 컬럼이 비어있는 행을 찾아 목록화:
```
이메일 결측 리드 (발송 불가):
- lead_id: [이름] / [소속기관] / [직책] → 별도 후속 메모 전환
```

### 5. 상담 메모(consultation_note) 결측·모호 확인 (review_flag 대상)
consultation_note가 비었거나 "상담 메모 없음" 또는 니즈 파악이 안 되는 행을 목록화:
```
상담 메모 결측/모호 리드 (review_flag = Y):
- lead_id: [이름] / [직책] / 사유(결측 or 모호)
```

### 6. 완전 중복 리드 확인
lead_id만 다르고 name·organization·consultation_note가 동일한 행을 탐지:
```
중복 리드: lead_id A = lead_id B (내용 완전 동일) → 한 건으로 처리
```

### 7. 분석 요약 출력
```
=== 분석 요약 ===
전체 리드: 50건 (중복 1건 → 실질 49건)
직책: 원장 N / 팀장 N / 사업개발 N
이메일 발송 가능: N건 / 발송 불가: N건
review_flag = Y 예상: N건 (상담 메모 결측·모호)
높은 우선순위(상): N건 — 48시간 내 우선 처리 대상
```

## 출력 형식
분석 결과를 대화창에 출력한다. 별도 파일 저장 불필요.

## 다음 단계
→ /insight 실행: 직책별 소구점 전략 수립
