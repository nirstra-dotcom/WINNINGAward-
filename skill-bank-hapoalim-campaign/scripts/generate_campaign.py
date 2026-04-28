#!/usr/bin/env python3
import argparse
import json
from dataclasses import dataclass, asdict


@dataclass
class CampaignInput:
    campaign_name: str
    goal: str
    audience: str
    offer: str
    cta: str
    tone: str
    characters: list[str]
    platform: str


def build_master_message(ci: CampaignInput) -> str:
    return (
        f"{ci.campaign_name}: מהלך {ci.goal} לקהל {ci.audience}, "
        f"עם הצעת ערך ברורה ('{ci.offer}') והנעה לפעולה: {ci.cta}."
    )


def build_carousel(ci: CampaignInput) -> list[dict]:
    heads = [
        "הגיע הזמן לפעול",
        "מה מקבלים עכשיו",
        "הדמויות מובילות",
        "ככה מצטרפים",
        "אל תחכו לרגע האחרון",
    ]
    supports = [
        f"{ci.campaign_name} מתחיל עם מסר {ci.tone} שמדבר אל {ci.audience}.",
        f"הטבה מרכזית: {ci.offer}.",
        f"שימור שפה ויזואלית אחידה עם הדמויות: {', '.join(ci.characters)}.",
        f"תהליך פשוט וברור: נכנסים, בודקים זכאות, מבצעים {ci.cta}.",
        "סגירת מסר עם דחיפות חיובית ותזכורת למועד האחרון.",
    ]
    visuals = [
        "רקע אדום דומיננטי, לוגו הבנק, שתי הדמויות במרכז.",
        "קלוז-אפ על מתנה/הטבה, טקסט לבן קצר וברור.",
        "הדמויות בפעולה (מחוות ידיים/חיוך), אלמנט ישראלי ברקע.",
        "אינפוגרפיקה של 3 שלבים פשוטים עם אייקונים.",
        "כפתור CTA גדול, קונטרסט גבוה, מסר סיום חד.",
    ]
    return [
        {"slide": idx + 1, "headline": heads[idx], "support": supports[idx], "visual": visuals[idx]}
        for idx in range(5)
    ]


def build_post_variants(ci: CampaignInput) -> dict:
    short = (
        f"{ci.campaign_name} כבר כאן 🇮🇱\n"
        f"{ci.offer}\n"
        f"{ci.cta} עכשיו."
    )

    medium = (
        f"הבטחנו להתאים את הקמפיין לקהל {ci.audience} – וזה בדיוק מה שעשינו.\n"
        f"במסגרת {ci.campaign_name} מחכה לכם {ci.offer}.\n"
        f"הדמויות שמלוות את המהלך ישמרו על שפה אחידה, קלילה וברורה בכל נכס.\n"
        f"הצעד הבא שלכם: {ci.cta}."
    )

    long = (
        f"{ci.campaign_name} נבנה כדי לייצר {ci.goal} אמיתי בקרב {ci.audience}.\n"
        f"אנחנו פותחים עם מסר {ci.tone}, מציגים קודם את הערך – {ci.offer} – ורק אז מניעים לפעולה.\n"
        f"לאורך הקרוסלה נשמור עקביות עם הדמויות ({', '.join(ci.characters)}) כדי שהמותג יישאר מזוהה, נגיש וזכיר.\n"
        f"לסיום: {ci.cta}."
    )

    return {"short": short, "medium": medium, "long": long}


def build_ad_variants(ci: CampaignInput) -> list[str]:
    return [
        f"{ci.offer} | {ci.cta}",
        f"{ci.campaign_name} באוויר – מצטרפים היום.",
        f"מסר {ci.tone}, ערך ברור, פעולה אחת: {ci.cta}.",
        f"לקהל {ci.audience}: הגיע הזמן להצטרף.",
        f"הדמויות כבר בפנים. אתם באים? {ci.cta}.",
    ]


def build_cta_bank() -> list[str]:
    return [
        "להרשמה מהירה",
        "לפרטים מלאים",
        "בודקים זכאות עכשיו",
        "מצטרפים בדקה",
        "לא מפספסים את ההטבה",
        "מתקדמים לשלב הבא",
        "התחילו כאן",
        "נרשמים כבר היום",
        "נכנסים ובוחרים",
        "לוחצים ומצטרפים",
    ]


def build_image_prompts(ci: CampaignInput) -> list[str]:
    chars = "; ".join(ci.characters)
    base = (
        "Israeli banking ad, dominant red brand background, high contrast Hebrew typography, "
        "friendly confident characters, social media composition"
    )
    return [
        f"{base}, hero shot, characters: {chars}, headline area on right, CTA button zone, {ci.platform}",
        f"{base}, gift reveal moment, energetic facial expressions, campaign title {ci.campaign_name}",
        f"{base}, map/journey visual metaphor, two character interaction, clean logo safe area",
        f"{base}, patriotic visual cues, flag elements, short headline about {ci.offer}",
        f"{base}, final urgency slide, bold CTA '{ci.cta}', accessible typography",
    ]


def build_output(ci: CampaignInput) -> dict:
    return {
        "campaign_input": asdict(ci),
        "master_message": build_master_message(ci),
        "carousel": build_carousel(ci),
        "post_variants": build_post_variants(ci),
        "ad_variants": build_ad_variants(ci),
        "cta_bank": build_cta_bank(),
        "image_prompt_bank": build_image_prompts(ci),
        "compliance_check": [
            "לאמת תאריכים, תנאי זכאות והטבות מול הגורם המשפטי/רגולטורי.",
            "לא לפרסם הבטחות פיננסיות שאינן מאושרות.",
            "להוסיף Alt Text לכל נכס ולבדוק קריאות בניגודיות גבוהה.",
        ],
    }


def to_markdown(payload: dict) -> str:
    lines = []
    lines.append(f"# {payload['campaign_input']['campaign_name']} – Campaign Pack")
    lines.append("")
    lines.append("## Master Message")
    lines.append(payload["master_message"])
    lines.append("")

    lines.append("## Carousel (5 slides)")
    for slide in payload["carousel"]:
        lines.append(f"### Slide {slide['slide']}: {slide['headline']}")
        lines.append(f"- Support: {slide['support']}")
        lines.append(f"- Visual: {slide['visual']}")
    lines.append("")

    lines.append("## Post Variants")
    for name, text in payload["post_variants"].items():
        lines.append(f"### {name}")
        lines.append(text)
        lines.append("")

    lines.append("## Ad Variants")
    for item in payload["ad_variants"]:
        lines.append(f"- {item}")
    lines.append("")

    lines.append("## CTA Bank")
    for item in payload["cta_bank"]:
        lines.append(f"- {item}")
    lines.append("")

    lines.append("## Image Prompt Bank")
    for item in payload["image_prompt_bank"]:
        lines.append(f"- {item}")
    lines.append("")

    lines.append("## Compliance Check")
    for item in payload["compliance_check"]:
        lines.append(f"- {item}")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a Bank Hapoalim style campaign pack")
    parser.add_argument("--campaign-name", default="פועלים ישראלי")
    parser.add_argument("--goal", default="הרשמה")
    parser.add_argument("--audience", default="קהל רחב")
    parser.add_argument("--offer", default="הטבה מיוחדת למצטרפים")
    parser.add_argument("--cta", default="להירשם באתר")
    parser.add_argument("--tone", default="מרגש")
    parser.add_argument("--characters", action="append", default=None)
    parser.add_argument("--platform", default="instagram")
    args = parser.parse_args()

    ci = CampaignInput(
        campaign_name=args.campaign_name,
        goal=args.goal,
        audience=args.audience,
        offer=args.offer,
        cta=args.cta,
        tone=args.tone,
        characters=args.characters or ["מנחה ראשית", "שותפה קומית"],
        platform=args.platform,
    )

    payload = build_output(ci)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    print("\n" + "=" * 60 + "\n")
    print(to_markdown(payload))


if __name__ == "__main__":
    main()
