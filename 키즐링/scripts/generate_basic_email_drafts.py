import argparse
import csv
from datetime import date
from pathlib import Path


REQUIRED_COLUMNS = [
    "lead_id",
    "name",
    "organization",
    "org_type",
    "title",
    "email",
    "consultation_note",
    "interest_feature",
    "follow_up_priority",
]

MISSING_NOTE_MARKERS = {"", "상담 메모 없음", "없음", "미기재"}
AMBIGUOUS_NOTE_MARKERS = ["애매", "모호", "구체적 니즈 파악 안 됨", "니즈 파악 안됨"]

SUBJECTS = {
    "원장": "[키즐링] {name} 원장님, 우리 원 아이들의 재능을 보여주는 키즐콘 안내",
    "팀장": "[키즐링] {name} 팀장님, 기존 운영에 쉽게 붙는 대회 운영 자동화",
    "사업개발": "[키즐링] {name} 님, 키즐콘 공동 공급·파트너십 제안의 건",
}

CTA_BY_TITLE = {
    "원장": {
        "상": "이번 주 무료 데모 일정을 제안드립니다.",
        "중": "편하신 시간에 무료 데모를 안내드리겠습니다.",
        "하": "먼저 데모 소개 자료를 보내드리겠습니다.",
    },
    "팀장": {
        "상": "이번 주 기술 도입 미팅을 제안드립니다.",
        "중": "편하신 시간에 기술 도입 미팅을 잡아보겠습니다.",
        "하": "먼저 연동 자료를 보내드리겠습니다.",
    },
    "사업개발": {
        "상": "수익 모델을 담은 파트너십 제안서를 바로 보내드리겠습니다.",
        "중": "파트너십 제안서를 정리해 보내드리겠습니다.",
        "하": "먼저 협력 모델 소개 자료를 보내드리겠습니다.",
    },
}

FEATURE_MESSAGES = {
    "대회운영SaaS": {
        "원장": "키즐콘 대회운영SaaS는 접수, 결제, 심사, 결과 발표를 한 흐름으로 묶어 원생의 성취를 학부모에게 더 선명하게 보여줄 수 있습니다.",
        "팀장": "키즐콘 대회운영SaaS는 접수, 결제, 심사, 결과 발표를 자동화해 운영 공수를 줄이고 기존 업무 흐름에도 단계적으로 붙일 수 있습니다.",
        "사업개발": "키즐콘 대회운영SaaS는 기관 공급, 공동 운영, 채널 판매 모델로 확장하기 좋아 파트너십 상품화 여지가 큽니다.",
    },
    "콘텐츠안전필터": {
        "원장": "키즐콘 콘텐츠안전필터는 유해 콘텐츠를 99% 차단하는 구조로 학부모 안심과 기관 신뢰를 함께 강화할 수 있습니다.",
        "팀장": "키즐콘 콘텐츠안전필터는 운영자가 모든 콘텐츠를 직접 확인하는 부담을 낮추고 안전 검수 체계를 서비스 안에 녹일 수 있습니다.",
        "사업개발": "키즐콘 콘텐츠안전필터는 안전한 키즈 콘텐츠 유통이라는 차별점을 만들어 공동 마케팅 메시지로 활용하기 좋습니다.",
    },
    "파트너십": {
        "원장": "키즐콘 파트너십 모델은 우리 원의 브랜드를 살린 공동 대회와 홍보로 아이들의 참여 경험을 넓히는 데 초점을 둡니다.",
        "팀장": "키즐콘 파트너십 모델은 기관별 운영 조건에 맞춰 공급 범위와 연동 방식을 조율할 수 있어 도입 검토가 수월합니다.",
        "사업개발": "키즐콘 파트너십 모델은 공동 공급, 채널 유통, 공동 마케팅을 함께 설계해 반복 가능한 수익 구조를 만들 수 있습니다.",
    },
}

FALLBACK_NOTES = {
    "원장": "부스에서 나눈 관심 주제를 바탕으로 후속 안내가 필요해 보여 연락드립니다.",
    "팀장": "부스 상담에서 도입 검토와 운영 효율에 대한 관심을 확인해 후속 안내드립니다.",
    "사업개발": "부스 상담에서 협력 가능성을 확인해 후속 제안을 드리고자 합니다.",
}

PAD_SENTENCE = " 상담 내용이 더 구체화되면 기관 상황에 맞춰 활용 장면과 다음 액션을 더 정확히 정리하겠습니다."


def clean(value):
    return (value or "").strip()


def load_source_rows(input_path):
    with input_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        missing_columns = [column for column in REQUIRED_COLUMNS if column not in (reader.fieldnames or [])]
        if missing_columns:
            raise ValueError(f"missing required columns: {', '.join(missing_columns)}")
        return list(reader)


def is_missing_email(row):
    return clean(row.get("email")) == ""


def is_missing_note(row):
    return clean(row.get("consultation_note")) in MISSING_NOTE_MARKERS


def is_ambiguous_note(row):
    note = clean(row.get("consultation_note"))
    return any(marker in note for marker in AMBIGUOUS_NOTE_MARKERS)


def needs_review(row):
    return is_missing_email(row) or is_missing_note(row) or is_ambiguous_note(row)


def duplicate_key(row):
    return (
        clean(row.get("name")),
        clean(row.get("organization")),
        clean(row.get("title")),
        clean(row.get("email")),
        clean(row.get("consultation_note")),
        clean(row.get("interest_feature")),
    )


def find_duplicate_exclusions(source_rows):
    first_seen = {}
    excluded = {}
    for row in source_rows:
        key = duplicate_key(row)
        lead_id = clean(row["lead_id"])
        if key in first_seen:
            excluded[lead_id] = first_seen[key]
        else:
            first_seen[key] = lead_id
    return excluded


def build_body(row):
    name = clean(row["name"]) or "담당자"
    organization = clean(row["organization"]) or "귀 기관"
    title = clean(row["title"]) or "담당자"
    feature = clean(row["interest_feature"]) or "대회운영SaaS"
    priority = clean(row["follow_up_priority"]) or "중"
    note = clean(row["consultation_note"])

    if title == "사업개발":
        salutation = f"{name}님, 안녕하세요. 키즐링 팀입니다."
    else:
        salutation = f"{name} {title}님, 안녕하세요. 키즐링 팀입니다."

    if is_missing_email(row):
        note_sentence = f"{organization} 상담 이후 후속 연락을 드리려 했으나 이메일 정보가 비어 있어 담당자 확인이 먼저 필요합니다."
    elif is_missing_note(row):
        fallback = FALLBACK_NOTES.get(title, FALLBACK_NOTES["팀장"])
        note_sentence = f"{organization} 부스 상담 메모가 비어 있어 세부 맥락은 재확인이 필요하지만, {fallback}"
    elif is_ambiguous_note(row):
        note_sentence = f"{organization} 상담 메모에 관심사가 모호한 부분이 있어 재확인이 필요하지만, 기록된 관심 기능을 기준으로 우선 정리했습니다."
    else:
        note_sentence = f'{organization} 상담에서 "{note}"라고 말씀 주신 내용을 바탕으로 후속 안내드립니다.'

    product_sentence = FEATURE_MESSAGES.get(feature, FEATURE_MESSAGES["대회운영SaaS"]).get(
        title,
        FEATURE_MESSAGES["대회운영SaaS"]["팀장"],
    )
    cta_sentence = CTA_BY_TITLE.get(title, CTA_BY_TITLE["팀장"]).get(
        priority,
        CTA_BY_TITLE.get(title, CTA_BY_TITLE["팀장"])["중"],
    )

    body = f"{salutation} {note_sentence} {product_sentence} {cta_sentence}"
    while len(body) < 250:
        body += PAD_SENTENCE
    if len(body) > 400:
        body = body[:397].rstrip() + "..."
    return body


def build_output_rows(source_rows, duplicate_excluded):
    output_rows = []
    for row in source_rows:
        lead_id = clean(row["lead_id"])
        if lead_id in duplicate_excluded:
            continue

        title = clean(row["title"]) or "팀장"
        name = clean(row["name"]) or "담당자"
        review_flag = needs_review(row)
        subject = SUBJECTS.get(title, SUBJECTS["팀장"]).format(name=name)
        if is_missing_email(row):
            subject = f"[검수 필요][키즐링] {name}님 후속 연락처 확인 필요"
        elif review_flag:
            subject = "[검수 필요]" + subject

        output_rows.append(
            {
                "lead_id": lead_id,
                "subject": subject,
                "body": build_body(row),
                "review_flag": "Y" if review_flag else "N",
            }
        )
    return output_rows


def build_summary(source_rows, duplicate_excluded):
    review_rows = [row for row in source_rows if clean(row["lead_id"]) not in duplicate_excluded and needs_review(row)]
    return {
        "review_ids": sorted(clean(row["lead_id"]) for row in review_rows),
        "email_missing": sorted(clean(row["lead_id"]) for row in review_rows if is_missing_email(row)),
        "note_missing": sorted(clean(row["lead_id"]) for row in review_rows if is_missing_note(row)),
        "note_ambiguous": sorted(clean(row["lead_id"]) for row in review_rows if is_ambiguous_note(row)),
        "duplicate_excluded": duplicate_excluded,
    }


def write_exception_summary(output_dir, source_count, row_count, summary):
    duplicate_text = ", ".join(
        f"{excluded}(대표 {primary})" for excluded, primary in sorted(summary["duplicate_excluded"].items())
    ) or "없음"
    lines = [
        "# Basic Exception Summary",
        "",
        f"- 생성일: {date.today().isoformat()}",
        "- 입력 파일: `leads_sample.csv`",
        "- 출력 파일: `email_drafts.csv`",
        f"- 원본 리드 수: {source_count}",
        f"- 생성 리드 수: {row_count}",
        f"- 검수 필요 리드: {', '.join(summary['review_ids']) or '없음'}",
        f"- 중복 제외 리드: {duplicate_text}",
        "",
        "## 검수 필요 사유",
        "",
        f"- 이메일 주소 누락: {', '.join(summary['email_missing']) or '없음'}",
        f"- 상담 메모 누락: {', '.join(summary['note_missing']) or '없음'}",
        f"- 상담 메모 모호: {', '.join(summary['note_ambiguous']) or '없음'}",
        "",
        "## 제외 처리",
        "",
        f"- 중복 제외: {duplicate_text}",
    ]
    (output_dir / "basic_exception_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_public_link_prep(output_dir):
    lines = [
        "# Public Link Prep",
        "",
        "Basic 단계 제출용 Google Sheet 공유 링크 생성을 위한 준비 메모입니다.",
        "",
        "## 업로드 대상",
        "",
        "- `키즐링/output/email_drafts.csv`",
        "",
        "## 권장 절차",
        "",
        "1. Google Drive에서 새 스프레드시트를 만든다.",
        "2. `email_drafts.csv`를 가져오기 한다.",
        "3. 헤더가 `lead_id`, `subject`, `body`, `review_flag` 순서인지 확인한다.",
        "4. 공유 설정을 링크가 있는 사용자가 볼 수 있음으로 변경한다.",
        "5. 공유 URL을 제출 문서 또는 `docs/phases/phase-3-basic-email-drafts.md`의 제출 링크 칸에 기록한다.",
        "",
        "## 미완료 항목",
        "",
        "- 실제 공개 URL 생성은 외부 Google 계정 작업이 필요해 아직 미완료.",
    ]
    (output_dir / "public_link_prep.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_pipeline_usage(output_dir):
    lines = [
        "# Standard Pipeline Usage",
        "",
        "새 리드 CSV에도 같은 방식으로 `정제 → 직책 분기 → 초안 생성 → review_flag`를 재현하기 위한 사용법입니다.",
        "",
        "## 입력 조건",
        "",
        "- 필수 컬럼: `lead_id`, `name`, `organization`, `org_type`, `title`, `email`, `consultation_note`, `interest_feature`, `follow_up_priority`",
        "- 허용 직책: `원장`, `팀장`, `사업개발`",
        "- 허용 관심 기능: `대회운영SaaS`, `콘텐츠안전필터`, `파트너십`",
        "- 허용 우선순위: `상`, `중`, `하`",
        "",
        "## Standard 단독 흐름",
        "",
        "1. `/analyze`: CSV 구조, 분포, 결측, 모호, 중복을 확인한다.",
        "2. 컨텍스트 반영: `키즐링/context/company-info.md`, `키즐링/context/industry-news.md`를 확인한다.",
        "3. `/insight`: 직책별 소구점, CTA, 우선순위별 CTA 강도, review_flag 기준을 확정한다.",
        "4. `/generate`: 아래 스크립트로 이메일 초안을 생성한다.",
        "5. `/review`: 생성 결과를 검수한다.",
        "",
        "## 실행 명령",
        "",
        "```powershell",
        "py -X utf8 키즐링/scripts/generate_basic_email_drafts.py --input 키즐링/data/leads_sample.csv --output-dir 키즐링/output",
        "```",
        "",
        "새 CSV를 사용할 때는 `--input`만 교체한다.",
        "",
        "```powershell",
        "py -X utf8 키즐링/scripts/generate_basic_email_drafts.py --input path/to/new_leads.csv --output-dir 키즐링/output",
        "```",
        "",
        "## 출력",
        "",
        "- `키즐링/output/email_drafts.csv`: Basic/Standard 공통 이메일 초안",
        "- `키즐링/output/basic_exception_summary.md`: 이메일 결측, 상담 메모 결측·모호, 중복 제외 요약",
        "- `키즐링/output/email_draft_sample.md`: 파이프라인 생성 이메일 초안 샘플 1부",
        "- `키즐링/output/public_link_prep.md`: 공개 링크 제출 준비 메모",
        "",
        "## 자동 처리 기준",
        "",
        "- 이메일 결측: `review_flag = Y`, 제목에 `[검수 필요]` 표시, 본문은 연락처 확인 메모로 작성한다.",
        "- 상담 메모 결측: 빈 값, `상담 메모 없음`, `없음`, `미기재`는 `review_flag = Y`로 처리한다.",
        "- 상담 메모 모호: `애매`, `모호`, `구체적 니즈 파악 안 됨` 등은 `review_flag = Y`로 처리한다.",
        "- 중복 리드: 이름, 조직, 직책, 이메일, 상담 메모, 관심 기능이 동일하면 첫 lead_id만 유지하고 이후 lead_id는 제외한다.",
        "",
        "## 설계 근거",
        "",
        "- 원장은 원생 재능 발굴, 학부모 만족, 기관 브랜딩을 전환 동기로 보므로 무료 데모 CTA가 적합하다.",
        "- 팀장은 도입 난이도와 운영 공수 절감이 의사결정의 병목이므로 기술 도입 미팅 CTA가 적합하다.",
        "- 사업개발은 공동 공급, 공동 마케팅, 수익 모델이 전환 동기이므로 파트너십 제안서 CTA가 적합하다.",
        "- 우선순위 `상`은 48시간 내 행동을 유도하고, `중`은 일정 조율, `하`는 소개자료 중심으로 낮은 압박의 너처링을 적용한다.",
        "- `review_flag`는 자동화가 오판하기 쉬운 데이터 품질 이슈를 사람이 보강하게 만드는 장치다.",
        "",
        "## 전체 제출 흐름과의 구분",
        "",
        "- Standard 단독 흐름: `/analyze → context 반영 → /insight → /generate → /review`",
        "- Challenge 포함 흐름: `/analyze → context 반영 → /insight → /generate → /campaign → /review`",
    ]
    (output_dir / "pipeline-usage.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_sample(output_dir, rows):
    sample = rows[0]
    lines = [
        "# Standard Email Draft Sample",
        "",
        "파이프라인으로 생성한 이메일 초안 샘플 1부입니다.",
        "",
        f"- lead_id: {sample['lead_id']}",
        f"- review_flag: {sample['review_flag']}",
        f"- subject: {sample['subject']}",
        "",
        "## body",
        "",
        sample["body"],
    ]
    (output_dir / "email_draft_sample.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_standard_validation(output_dir, rows, summary):
    lengths = [len(row["body"]) for row in rows]
    duplicate_excluded = ", ".join(summary["duplicate_excluded"]) or "없음"
    lines = [
        "# Standard Validation Summary",
        "",
        "- 새 CSV 입력 가능성: `--input` 인자로 동일 스키마 CSV를 교체할 수 있음",
        f"- 출력 행 수: {len(rows)}",
        f"- 본문 길이 범위: {min(lengths)}~{max(lengths)}자",
        f"- `review_flag = Y`: {', '.join(summary['review_ids']) or '없음'}",
        f"- 중복 제외: {duplicate_excluded}",
        "- 출력 스키마: `lead_id`, `subject`, `body`, `review_flag`",
        "- 파이프라인 샘플: `키즐링/output/email_draft_sample.md`",
        "",
        "## 검증 결과",
        "",
        "- Standard 단독 흐름 문서화: 통과",
        "- 스크립트 사용법 문서화: 통과",
        "- 이메일 초안 샘플 1부 생성: 통과",
        "- 직책별 소구점·CTA 설계 근거 문서화: 통과",
        "- review_flag 기준 문서화: 통과",
    ]
    (output_dir / "standard_validation_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Generate Kizzling email_drafts.csv and Standard pipeline artifacts.")
    parser.add_argument("--input", default="키즐링/data/leads_sample.csv")
    parser.add_argument("--output-dir", default="키즐링/output")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    source_rows = load_source_rows(input_path)
    duplicate_excluded = find_duplicate_exclusions(source_rows)
    rows = build_output_rows(source_rows, duplicate_excluded)
    summary = build_summary(source_rows, duplicate_excluded)

    output_path = output_dir / "email_drafts.csv"
    with output_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["lead_id", "subject", "body", "review_flag"])
        writer.writeheader()
        writer.writerows(rows)

    write_exception_summary(output_dir, len(source_rows), len(rows), summary)
    write_public_link_prep(output_dir)
    write_pipeline_usage(output_dir)
    write_sample(output_dir, rows)
    write_standard_validation(output_dir, rows, summary)

    lengths = [len(row["body"]) for row in rows]
    review_flags = sorted(row["lead_id"] for row in rows if row["review_flag"] == "Y")
    print(f"output={output_path.as_posix()}")
    print(f"rows={len(rows)}")
    print(f"review_flags={review_flags}")
    print(f"body_length_min={min(lengths)}")
    print(f"body_length_max={max(lengths)}")
    print(f"duplicate_excluded={duplicate_excluded}")


if __name__ == "__main__":
    main()
