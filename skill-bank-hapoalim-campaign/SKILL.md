---
name: bank-hapoalim-campaign-automation
description: Build Hebrew marketing campaign packs for Bank Hapoalim style posts, including carousel slide copy, short ads, long post variants, and generation prompts using predefined brand characters when the user asks for quick promotional content.
---

# Bank Hapoalim Campaign Automation Skill

Use this skill when the user asks to automatically generate:
- Social posts in Hebrew for Bank Hapoalim-style campaigns
- Carousel content (multi-slide post)
- Short paid ads and CTA variants
- Ready-to-paste prompts for image/video generation with recurring characters

## Inputs to collect
When possible, collect these fields (ask only if missing):
1. `campaign_name` (e.g., "פועלים ישראלי")
2. `goal` (registration, awareness, engagement, conversion)
3. `audience` (families, students, small businesses, general public)
4. `offer` (benefit, date range, registration deadline)
5. `cta` (what the user should do)
6. `tone` (warm, exciting, patriotic, practical)
7. `characters` (names/roles of recurring characters to include)
8. `platform` (Instagram/Facebook/TikTok/LinkedIn)

If inputs are missing and the user still wants immediate output, generate a "default campaign pack" with explicit placeholders.

## Output format
Always generate a reusable campaign pack with these sections:
1. **Master Message** – one sentence strategy line
2. **Carousel (5 slides)** – headline + support line + visual direction per slide
3. **Post Variants** – 3 versions (short, medium, long)
4. **Ad Variants** – 5 short paid ad lines
5. **CTA Bank** – 10 CTA options
6. **Image Prompt Bank** – 5 prompts preserving consistent character styling
7. **Compliance Check** – note to verify legal/compliance approval before publishing

## Deterministic generation script
For consistent output, run:

```bash
python3 skill-bank-hapoalim-campaign/scripts/generate_campaign.py \
  --campaign-name "פועלים ישראלי" \
  --goal "הרשמה" \
  --audience "משפחות" \
  --offer "מגנט דגל ישראל במתנה לנרשמים" \
  --cta "להירשם באתר" \
  --tone "מרגש" \
  --characters "דמות 1: מנחה אנרגטית" \
  --characters "דמות 2: חברה קומית" \
  --platform "instagram"
```

The script returns JSON + Markdown so the user can immediately copy for production.

## Brand consistency rules
- Hebrew-first copy.
- Keep energetic but clear language.
- Mention value before CTA.
- Keep carousel slide headlines short (2–6 words).
- Reuse recurring character descriptors to keep visuals consistent.
- Do not claim unverified guarantees or misleading financial promises.

## Safety & quality
- Flag dates, pricing, eligibility, and legal claims as fields that must be approved.
- Avoid sensitive targeting or discriminatory wording.
- Include accessibility recommendation: add alt-text and high contrast checks.
