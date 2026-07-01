---
name: kizzling-visualize-campaign
description: 키즐링 캠페인 기획안을 평가자와 사용자가 한눈에 볼 수 있는 정적 HTML 미리보기로 시각화한다. campaign_plan.md 이후 세그먼트, 근거 리드, 대표 인용, 후속 시퀀스, review_flag 주의 리드, 우선순위 근거를 시각적으로 정리해야 할 때 사용한다.
---

# 키즐링 캠페인 시각화

`campaign_plan.md`를 정적 HTML 미리보기로 변환한다. HTML은 제출 산출물의 이해를 돕는 보조 결과물이며, 이메일 발송·CRM·외부 API·리드 스코어링 기능을 포함하지 않는다.

이 스킬은 별도 스크립트나 템플릿 엔진 없이, 실행할 때마다 아래 지시에 따라 HTML 전체를 새로 작성한다. 실행마다 결과가 크게 달라지지 않도록, 인터랙션이 들어가는 부분은 "재사용 UI 스니펫" 절의 코드를 값만 채워 그대로 재사용한다.

## 입력

다음 자료를 사용한다.

- `campaign_plan.md`
- `email_drafts.csv` — 캠페인 근거 리드에 해당하는 행의 `subject`, `body`를 리드별로 파싱해 상세 토글에 넣는다.
- `basic_exception_summary.md`
- 필요 시 회사/업계 컨텍스트

## 출력

다음 파일 내용을 생성한다.

- `campaign_plan_preview.html`

## 시각화 구성

HTML에는 다음 영역을 포함한다.

- 전체 요약: 캠페인 수, 실질 처리 리드 수, `review_flag` 주의 리드
- 캠페인이 2건 이상이면 전체 요약 카드 바로 다음에 캠페인 비교 요약 표(세그먼트 규모, 우선순위 `상` 비중, 검수 필요 리드, 핵심 리스크를 나란히 비교)
- 캠페인별 세그먼트 카드
- 우선순위 분포 바(상/중/하 비율)와 범례
- 근거 리드 칩 — 클릭하면 해당 리드의 실제 이메일 제목·본문이 펼쳐지는 상세 토글
- 우선순위/검수 필요 리드만 걸러 보는 필터 탭
- 대표 상담 인용
- Day 0, Day 2~3, Day 7 후속 시퀀스를 체크박스 목록으로, 각 항목에 담당 부서 라벨(예: 담당: 마케팅팀) 포함
- 우선순위와 판단 근거
- 리스크·차단요소 박스 — 무엇이 실행을 지연·차단할 수 있는지와 담당 부서의 확인 기한
- 사람 검수 필요 리드 안내
- 인쇄 시 필터 탭이 숨고 카드가 페이지 분할 없이 보이는 인쇄용 스타일

## 재사용 UI 스니펫 (실행마다 값만 채워 그대로 사용, 구조·클래스명·함수명 변경 금지)

### CSS (`<style>` 안에 기존 스타일과 함께 포함)

```css
/* 리드 상세 토글 */
.lead-detail { display:inline-block; margin:2px 3px 2px 0; }
.lead-detail summary { list-style:none; cursor:pointer; }
.lead-detail summary::-webkit-details-marker { display:none; }
.lead-detail summary.lead-chip::after { content:" \25b8"; font-size:10px; color:#999; }
.lead-detail[open] summary.lead-chip::after { content:" \25be"; }
.lead-email { background:#fafbfc; border:1px solid #e9ecef; border-radius:6px; padding:10px 12px; margin:4px 0 6px; font-size:12px; max-width:420px; }
.lead-email .subj { font-weight:700; margin-bottom:4px; }
.lead-email .body { color:#444; }

/* 필터 탭 */
.filter-bar { display:flex; gap:8px; margin:4px 0 10px; flex-wrap:wrap; }
.filter-btn { font-size:12px; font-weight:600; padding:5px 12px; border-radius:14px; border:1px solid #ddd; background:#fff; color:#555; cursor:pointer; }
.filter-btn.active { background:#6c4cf0; color:#fff; border-color:#6c4cf0; }
.lead-detail[hidden] { display:none; }

/* 우선순위 분포 바 */
.priority-bar { display:flex; height:10px; border-radius:5px; overflow:hidden; margin:8px 0 4px; background:#eee; }
.priority-bar .bar-high { background:#e63946; }
.priority-bar .bar-mid { background:#f0a020; }
.priority-bar .bar-low { background:#ccc; }
.bar-legend { font-size:11px; color:#888; }

/* 인쇄 */
@media print {
  body { background:#fff; }
  .filter-bar { display:none; }
  .lead-detail { display:block; }
  .campaign { box-shadow:none; border:1px solid #ddd; page-break-inside:avoid; }
}

/* 캠페인 비교 요약 표 */
.compare-table { width:100%; border-collapse:collapse; margin-bottom:24px; background:#fff; border-radius:10px; overflow:hidden; box-shadow:0 1px 4px rgba(0,0,0,.06); }
.compare-table th, .compare-table td { padding:10px 14px; border-bottom:1px solid #eee; text-align:left; font-size:13px; }
.compare-table th { font-size:11px; text-transform:uppercase; letter-spacing:.5px; color:#888; background:#fafbfc; }

/* 체크리스트형 후속 시퀀스 + 담당 라벨 */
.seq-owner { display:inline-block; font-size:10px; font-weight:700; color:#6c4cf0; background:#f0e6ff; border-radius:4px; padding:1px 6px; margin-bottom:4px; }
.seq-step label { display:flex; gap:6px; align-items:flex-start; cursor:pointer; }
.seq-step input[type=checkbox] { margin-top:3px; }

/* 리스크·차단요소 */
.risk-box { background:#f5f5ff; border:1px solid #d8d8f5; border-radius:8px; padding:12px 14px; font-size:13px; color:#3a3a5c; margin-top:8px; }
```

### JS (`<script>` 하나만 body 끝에 포함, 필터 탭 전용, 그 외 스크립트 추가 금지)

```html
<script>
function filterLeads(groupId, mode, btn) {
  var group = document.getElementById(groupId);
  var items = group.querySelectorAll('.lead-detail');
  items.forEach(function (el) {
    var show = mode === 'all'
      || (mode === 'priority' && el.dataset.priority === '상')
      || (mode === 'flag' && el.dataset.flag === 'Y');
    el.hidden = !show;
  });
  var bar = btn.closest('.filter-bar');
  bar.querySelectorAll('.filter-btn').forEach(function (b) { b.classList.remove('active'); });
  btn.classList.add('active');
}
</script>
```

### 캠페인별 필터 탭 + 리드 목록 HTML 패턴

`{{n}}`은 캠페인 번호(1, 2, ...)로 치환한다. 그룹 id는 캠페인마다 고유해야 한다.

```html
<div class="filter-bar">
  <button class="filter-btn active" onclick="filterLeads('campaign-{{n}}-leads','all',this)">전체</button>
  <button class="filter-btn" onclick="filterLeads('campaign-{{n}}-leads','priority',this)">우선순위 상만</button>
  <button class="filter-btn" onclick="filterLeads('campaign-{{n}}-leads','flag',this)">검수 필요만</button>
</div>
<div id="campaign-{{n}}-leads">
  <details class="lead-detail" data-priority="상" data-flag="N">
    <summary class="lead-chip priority">L021 상</summary>
    <div class="lead-email">
      <div class="subj">제목: (email_drafts.csv의 해당 lead_id subject)</div>
      <div class="body">본문: (email_drafts.csv의 해당 lead_id body)</div>
    </div>
  </details>
  <!-- review_flag=Y 리드는 class="lead-chip flag", data-flag="Y" -->
</div>
```

### 우선순위 분포 바 HTML 패턴

퍼센트는 세그먼트의 실제 상/중/하 리드 수로 매 실행마다 다시 계산한다.

```html
<div class="priority-bar">
  <span class="bar-high" style="width:50%"></span>
  <span class="bar-mid" style="width:41.7%"></span>
  <span class="bar-low" style="width:8.3%"></span>
</div>
<div class="bar-legend">우선순위 분포 — 상 6건 · 중 5건 · 하 1건</div>
```

### 캠페인 비교 요약 표 HTML 패턴 (캠페인이 2건 이상일 때, 전체 요약 카드 바로 다음에 배치)

새로운 점수·순위를 계산하지 않고, `campaign_plan.md`의 캠페인 비교 요약 표에 있는 값만 그대로 옮긴다.

```html
<table class="compare-table">
  <thead>
    <tr><th>캠페인</th><th>세그먼트 규모(실질)</th><th>우선순위 &#39;상&#39; 비중</th><th>검수 필요 리드</th><th>핵심 리스크</th></tr>
  </thead>
  <tbody>
    <tr><td>1. 에듀테크 팀장 대상 대회 운영 자동화 전환</td><td>12건</td><td>6/12 (50%)</td><td>1건</td><td>L033 확인 지연 시 골든타임 이탈</td></tr>
    <tr><td>2. 사업개발 대상 파트너십 제안</td><td>12건(실질 11건)</td><td>5/11 (45.5%)</td><td>1건</td><td>L046 확인 지연 시 골든타임 이탈</td></tr>
  </tbody>
</table>
```

### 체크리스트형 후속 시퀀스 + 담당 라벨 HTML 패턴 (기존 `.seq-step` 안의 `.seq-act`를 아래 구조로 대체)

```html
<div class="seq-step">
  <div class="seq-day">Day 0</div>
  <div class="seq-owner">담당: 마케팅팀</div>
  <label><input type="checkbox"> 팀장용 초안 발송. CTA = 기술 도입 미팅. 우선순위 &#39;상&#39;은 48시간 내 미팅 슬롯 제안.</label>
</div>
```

### 리스크·차단요소 박스 HTML 패턴 (캠페인 카드 안, `.review-note` 바로 아래에 배치)

```html
<div class="risk-box">⚠ 리스크·차단요소: L033은 review_flag=Y라 상담 니즈 확인 전에는 발송을 보류한다. 담당(영업팀)이 접수 후 24시간 내 1차 확인을 마치지 못하면 48시간 골든타임을 넘겨 이 리드는 시퀀스에서 실질적으로 이탈한다.</div>
```

## 작성 규칙

- 정적 HTML 한 파일로 작성한다. 인라인 `<style>`과 위 스니펫의 `<script>` 하나만 허용하고, 그 외 외부 CDN·외부 이미지·추적 스크립트·API 호출은 넣지 않는다.
- 이메일 실제 발송 버튼, CRM 연결 버튼, 점수 산출 UI를 만들지 않는다. 필터·토글은 이미 렌더링된 리드 데이터를 보이거나 숨기는 것뿐이며 서버·외부 호출을 하지 않는다.
- 한국어로 작성한다.
- 상대경로만 사용한다.
- 표와 타임라인은 평가자가 빠르게 스캔할 수 있게 간결하게 만든다.
- 이메일 본문은 `email_drafts.csv`에 있는 내용을 그대로 인용하고 새로 지어내지 않는다.
- 체크박스는 인쇄·화면에서 담당자가 진행 상황을 표시하는 시각적 용도이며, 상태를 저장하거나 서버로 전송하지 않는다(새로고침하면 초기화된다).

## 전달

생성한 HTML 미리보기와 기존 산출물을 `kizzling-quality-audit`으로 넘겨 최종 QA를 수행한다.
