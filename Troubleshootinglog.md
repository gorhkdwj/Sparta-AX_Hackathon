# Troubleshootinglog · Sparta_AX_Project

실제 오류·실패·환경 문제·검증 실패·설계 충돌이 발생하면 기록한다. 같은 문제가 반복되면 새 T-ID를 만들기 전에 기존 T-ID를 먼저 확인한다. (규칙: CLAUDE.md 11절)

## 기록 형식
```
### T-00N · 문제 제목
**발생 상황** / **증상** / **확인된 원인** / **조치** / **재발 방지**
```

---

### T-005 · submission/ 스킬 폴더 경로가 세션 사이에 바뀌어 잘못된 방향으로 수정함
**발생 상황**
- 이전 턴에서 `submission/` 완성물을 조사해 스킬 폴더 실제 경로를 `submission/skills/`(점 없음)로 확인하고, 여러 문서(`README.md`, `evidence/*.md`, `output/submission-summary.md`, `output/quality_audit_report.md` 등)가 이와 다르게 `submission/.claude/skills/`라고 적어놓은 것을 "문서 오류"로 지목해 사용자에게 보고함.
- 사용자가 "수정해줘"라고 요청해 그 보고 내용대로 여러 파일에서 `.claude/skills/` → `skills/`로 고쳤다.

**증상**
- 수정 도중 `submission/skills` 경로로 다시 확인했더니 해당 폴더가 존재하지 않고, 실제로는 `submission/.claude/skills/`에 스킬 8개가 있었다. 즉 직전 턴 사이에 폴더가 `skills/` → `.claude/skills/`로 바뀌어 있었고, 방금 한 수정은 반대 방향(`.claude/skills/` → `skills/`)이라 전부 틀린 상태가 됐다.

**확인된 원인**
- 이 저장소에 `submission/`이 아직 git에 추가되지 않은 상태(`git status`에 `?? submission/`)라 변경 이력을 대조할 수 없었다. 정황상 사용자가 이전 턴과 이번 턴 사이에 폴더명을 직접 `.claude/skills/`로 변경한 것으로 보인다(불확실점: 정확히 언제, 왜 변경했는지는 확인 불가).
- `.claude/skills/`는 Claude Code가 실제로 스킬을 자동 인식하는 경로이므로(이전 대화에서 claude-code-guide 에이전트로 확인함), `submission/skills/`(점 없음)였던 이전 구조는 애초에 `submission/`을 열어 `/kizzling-followup`을 바로 실행할 수 없는 상태였다. 즉 사용자의 폴더명 변경이 맞는 방향이었고, 내가 처음 지목한 "문서 오류"는 사실 실제 경로 쪽이 나중에 올바르게 바뀐 것이었다.

**조치**
- `submission/` 전체를 다시 스캔해 `.claude/skills` 관련 참조 24건(README.md, evidence 3개 파일, output 4개 파일)을 전부 `submission/.claude/skills/`로 재수정.
- 직전 턴에 작성한 `docs/final-deliverables-structure.md`, `docs/validation-plan.md`, `docs/phases/phase-7-quality-visualization.md`의 `submission/skills/` 표기도 `submission/.claude/skills/`로 재수정(권장 폴더 구조 트리 포함).
- Worklog.md, Decisionlog.md에 남아 있는 과거의 `submission/skills/` 언급은 그 시점 기준으로는 사실이었던 역사 기록이라 수정하지 않음.

**재발 방지**
- 대화 중 이전에 확인한 파일 구조를 다시 근거로 쓸 때는, 특히 사용자가 그 사이에 직접 손댔을 가능성이 있는 산출물(작업 폴더, 완성물 등)은 재수정 전에 현재 상태를 다시 `find`/`ls`로 확인한다. "지난 턴에 확인했다"는 이유로 구조를 고정된 사실처럼 취급하지 않는다.
**발생 상황**
- `C:\Users\gorhk\새 폴더`(이 저장소와 무관한 독립 테스트 폴더)에 `.claude/skills`를 복사하고 더미 리드 CSV 16건으로 `kizzling-followup` 전체 체인을 실행한 결과를 원본 `submission/output/email_drafts.csv`(50건, 이미 검수 완료된 제출물)와 대조 검증.

**증상**
- `kizzling-message-strategy/SKILL.md`에 명시된 우선순위별 CTA 강도 규칙(상=48시간 내 즉시행동, 중=편한 일정조율, 하=장기너처링)을 새 실행 결과에서 행 단위로 재검증한 결과, `review_flag=N`인 D009(원장·중 우선순위)에 상 등급 전용 긴급 문구("48시간")가 포함됐고, D012(원장·중 우선순위)는 표준 CTA 문구("무료 데모")가 완전히 빠지고 일반 안내 문구로만 대체됨.
- 자체 생성 `quality_audit_report.md`는 "직책별 제목/CTA 차별화"를 3개 직책 템플릿 단위로만 확인하고 통과 판정했으며, 동일 등급 내 행별 CTA 키워드 존재 여부는 검사하지 않아 이 편차를 놓침.

**확인된 원인**
- PowerShell로 원본 제출물(50건)의 동일 조건(원장·중/하 우선순위, review_flag=N) 리드 11건을 전수 재검사한 결과, "무료 데모" 문구 포함 11/11, 상 전용 긴급 문구("48시간"/"이번 주 안에") 사용 0/11로 규칙이 완전히 지켜졌음을 확인. 반면 새 실행에서는 동일 규칙이 2건에서 흔들림.
- 스크립트가 아닌 Skill(LLM) 기반 파이프라인 특성상, 프로그램적 강제 없이 서술형 규칙만으로는 실행마다 경계 적용에 편차가 생길 수 있음. 이번 결과가 우연한 1회성 편차인지 반복 재현되는 패턴인지는 이번 1회 실행만으로는 확인 불가(불확실점).

**조치**
- 원본 `submission/output/email_drafts.csv`는 이번 발견과 무관하며 이미 검수된 상태 그대로 유지. 수정 대상 아님.
- 새 폴더(`C:\Users\gorhk\새 폴더`)는 이 저장소 밖의 일회성 테스트 산출물이라 별도 수정하지 않음.
- 사용자에게 D009/D012 두 건은 사람이 CTA 문구만 표준으로 다듬으면 되는 경미한 수준이라고 보고.

**재발 방지**
- `kizzling-quality-audit`에 "review_flag=N 리드는 title별 CTA 핵심 키워드(무료 데모/기술 도입 미팅/파트너십 제안서)가 본문에 존재해야 한다"는 프로그램적 grep 체크를 추가하는 방안을 다음 개선 후보로 남김(아직 미구현).

---

### T-003 · PowerShell heredoc 문법으로 Python 검증 명령 실패
**발생 상황**
- 현재 구현 상태 점검 중 `submission/output/email_drafts.csv`를 Python으로 검증하려고 Bash 스타일 heredoc(`<<'PY'`)을 PowerShell에서 실행.

**증상**
- PowerShell이 `<` 연산자를 리디렉션으로 해석해 구문 오류가 발생했고, Python 검증이 실행되지 않음.

**확인된 원인**
- 현재 셸은 PowerShell이며 Bash heredoc 문법을 지원하지 않는다.

**조치**
- 같은 검증을 PowerShell의 `Import-Csv` 기반 명령으로 다시 수행.
- `email_drafts.csv` 49행, 필수 컬럼 4개, 본문 250~297자, `review_flag = Y` 5건, L050 제외를 확인.

**재발 방지**
- PowerShell 환경에서는 Bash heredoc을 사용하지 않는다.
- 짧은 CSV 검증은 `Import-Csv`를 우선 사용하고, Python이 필요하면 PowerShell here-string 또는 파일 기반 실행을 사용한다.

---

### T-002 · Python stdin 실행 시 한글 템플릿 깨짐
**발생 상황**
- Phase 3에서 Python 코드를 PowerShell stdin으로 전달해 `키즐링/output/email_drafts.csv`를 생성.

**증상**
- 파일 경로 또는 제목/본문의 한글 템플릿 일부가 `???` 형태로 변환됨.

**확인된 원인**
- PowerShell과 Python stdin 전달 과정에서 한글 소스 리터럴이 실행 전에 손상됨.

**조치**
- 생성 로직을 `키즐링/scripts/generate_basic_email_drafts.py` 파일로 분리.
- `py -X utf8 키즐링/scripts/generate_basic_email_drafts.py --input 키즐링/data/leads_sample.csv --output-dir 키즐링/output` 명령으로 재생성.
- `???` 패턴 없음, 행 수 49, 본문 길이 250~297자, 검수 플래그 5건을 확인.

**재발 방지**
- 한글 템플릿이 포함된 생성 로직은 stdin 인라인 실행 대신 UTF-8 파일로 저장해 실행한다.
- 보고와 문서에는 사용자 요청에 따라 상대경로만 사용한다.

---

### T-001 · 발제 설명과 실제 CSV의 상담 메모 결측 수량 차이
**발생 상황**
- Phase 1에서 `키즐링/data/leads_sample.csv`를 실제 분석.

**증상**
- 발제 설명에는 상담 메모 결측 2건으로 되어 있으나, 실제 CSV에는 `상담 메모 없음` 2건(L012, L046)과 빈 셀 1건(L015)이 있어 총 3건이 결측 처리 대상.

**확인된 원인**
- 발제 설명과 실제 제공 CSV 사이의 수량 불일치. 실제 데이터에는 사업개발 리드 L046이 `상담 메모 없음`으로 추가 포함되어 있음.

**조치**
- 실제 CSV를 우선 기준으로 채택.
- L012, L015, L046을 상담 메모 결측으로 보고 `review_flag = Y` 처리하기로 결정.
- 관련 결정은 `Decisionlog.md`의 D-003에 기록.

**재발 방지**
- 이후 Phase에서는 발제 설명의 수량보다 실제 CSV 분석 결과를 우선하고, 불일치가 있으면 Troubleshootinglog와 Decisionlog에 남긴다.
