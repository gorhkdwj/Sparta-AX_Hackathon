# Sparta_AX_Project

> 스파르타 AX 해커톤 제출물 — 한 번 끝까지 푼 작업을 재사용 가능한 **Claude Skill**로 도구화한다.

## 개요
- 목적: 작업을 `/스킬명` 한 줄로 재현 가능한 도구로 남긴다.
- 주요 사용자: 사내 동료 (스킬을 가져다 그대로 재사용)
- 최종 산출물: `.claude/skills/<스킬명>/SKILL.md` + 한 번 실행한 결과(입력 → 출력)
- 주제: 미정 (확정 후 갱신)

## 실행 방법
(실제 구현된 기능만 기재한다. 미구현 기능은 쓰지 않는다.)

- 스킬 호출: `/스킬명 <작업 내용>` 또는 자연어로 "○○ 스킬로 ~ 해줘"
- 현재 상태: 운영 체계만 셋업됨. 스킬 본문(`SKILL.md`)은 주제 확정 후 작성 예정.

## 프로젝트 구조
- `.claude/skills/skill-wip/SKILL.md` — 제출물 스킬 (임시 이름, 주제 확정 시 변경)
- `docs/` 기획·기준계약·구현·검증 문서
- `docs/references/` 외부 자료 (제출 가이드 등)
- `out/demo/` 제출용 실행 결과 (입력 → 출력, Git 제외)

## 문서
- 작업 규칙: `CLAUDE.md`
- 작업 이력: `Worklog.md`
- 주요 결정: `Decisionlog.md`
- 문제 해결: `Troubleshootinglog.md`
- 제출 가이드: `docs/references/제출가이드.md`
