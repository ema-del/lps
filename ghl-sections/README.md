# Pacow Growth funnel — GHL sections

Paste these into GHL's page builder as separate custom-code blocks, **in this
order**. Section 1 must be pasted first — it defines `pacowModal()`, which
every later section's CTA button calls.

| # | File | Purpose |
|---|------|---------|
| 1 | `section-1-hero.html` | Hero, VSL, and the branded modal wrapping the GHL survey |
| 2 | `section-2-social-proof.html` | Partner logo spotlight + expandable grid |
| 3 | `section-3-who-this-is-for.html` | Qualifier: who this is / isn't for |
| 4 | `section-4-how-it-works.html` | Interactive 3-phase "how it works" player |
| 4b | `section-4b-what-you-get.html` | "What you get" recap checklist |
| 5 | `section-5-key-stats.html` | $5M+ / 4-7x / 98% stat bar |
| 6 | `section-6-testimonials.html` | Video testimonials + text wall |
| 6b | `section-6b-screenshot-marquee.html` | Auto-scrolling proof-screenshot marquee |
| 7 | `section-7-guarantee.html` | No-Results, No-Pay guarantee |
| 8 | `section-8-faq.html` | FAQ accordion |
| 9 | `section-9-footer.html` | Final CTA, footer, legal + earnings disclaimer |

## What changed in this pass

1. **Survey swapped.** The qualifier survey embedded in Section 1's modal now
   points at the new GHL survey widget `DoZBheo9WrIzRWMZ64lk`
   (`https://links.pacowmedia.com/widget/survey/DoZBheo9WrIzRWMZ64lk`),
   replacing the old `Gc4KkJN6IoGNjaCZO256` widget. The iframe now also
   carries `data-cookie-consent="true" data-cookie-consent-provider="auto"`.
   Every reference to the old ID (comment, `id` attribute, `src`, and the
   `pacowModal('open')` bridge JS that re-triggers the iframe `src`) was
   updated together — grep for `DoZBheo9WrIzRWMZ64lk` if you ever need to
   swap it again.

2. **"How It Works" rewritten in a Matt Shiver-style narrative** (Section 4).
   Same interactive 3-phase tab/player UI and the same real Pacow
   deliverables, but each phase now reads like a plain "here's exactly what
   happens" walkthrough (Phase 1: foundations before we spend a dollar;
   Phase 2: ads made + launched together, live within 14 days; Phase 3:
   weekly optimization + unlimited free ad rewrites for 90 days, ending in
   "you're not dependent on us or any agency ever again").

3. **New "What You Get" section** (4b), styled to match Pacow's light-section
   design system, mirroring the bullet-checklist format from Matt Shiver's
   page — but built entirely from Pacow's own stated deliverables (audit,
   ad production, funnel build, 1:1 launch, 90 days of coaching, unlimited
   rewrites, GrowthOS™ + Slack, training library + Skool access). Drop it
   in right after Section 4.

4. **Footer disclaimer added** (Section 9). Kept the existing footer as-is
   (CTA, logo, copyright, Terms/Privacy links) and added a
   Matt-Shiver-style "Results and Earnings Disclaimer" block underneath,
   rewritten for Pacow's actual business (a paid-ads agency, not an income
   program) and the platforms Pacow runs ads on (Meta/Instagram, Google/
   YouTube) rather than copying Matt Shiver's fitness-coaching disclaimer
   verbatim.

Everything else (social proof, who-this-is-for, key stats, testimonials,
marquee, guarantee, FAQ) is unchanged from the original page content.

## Follow-up pass

5. **CTA copy changed.** Every button across every section now reads
   **"Book a Free Strategy Call"** (was "Apply to see if you qualify"). It
   still calls the same `pacowModal('open')` bridge, so the button opens the
   same qualifier survey — only the label changed.
6. **"Watch this" line added above the hero video** (Section 1), Matt
   Shiver-style: *"Watch this free training, then book your free Strategy
   Call"*, styled as a small purple line with a play icon, sitting between
   the subhead and the VSL.
