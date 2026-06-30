# Decisionlog · Sparta_AX_Project

방향을 바꾸거나 이후 작업에 영향을 주는 **중요한 결정만** 기록한다. 사소한 수정은 Worklog에만 남긴다. (규칙: CLAUDE.md 11절)

## 기록 형식
```
### D-00N · 결정 제목
**상황** / **검토한 선택지** / **결정** / **근거** / **영향** / **재검토 조건**
```

---

### D-001 · 폴더 구조를 '스킬 제출형'으로 조정
**상황**
- 해커톤 제출물이 일반 앱이 아니라 Claude Skill(`.claude/skills/<이름>/SKILL.md`) 하나.

**검토한 선택지**
- (A) project-setup 표준 구조(src/tests/tools 포함) 그대로
- (B) 스킬 중심 구조 — src/tests/tools 생략, `.claude/skills/` + docs + out/demo

**결정**
- (B) 채택. 임시 스킬 이름 `skill-wip` 사용.

**근거**
- 산출물이 스킬 한 개라 일반 코드 트리는 과함. 제출 가이드가 요구하는 SKILL.md + 실행결과 형식에 맞춤.

**영향**
- 최상위 src/tests/tools 미생성. 보조 스크립트 필요 시 스킬 폴더 내부 scripts/로.

**재검토 조건**
- 스킬이 별도 실행 코드/테스트를 크게 동반하게 되면 구조 재검토.
