# HERMES Content Library — For Wadda Khan

This is the complete content library from Folio's HERMES Content Agent pipeline. All 117 article drafts, templates, data files, and reports are here for you to use in your own publishing workflow.

## Contents

```
wadda-content/
├── README.md              ← You are here
├── HANDOFF.md             ← Full skill handoff + memory transfer
├── drafts/                ← 117 SEO-optimised article drafts (.md)
│   ├── 2026-05-27-*      (43 articles — VPN, hosting, cybersecurity, SaaS)
│   ├── 2026-05-28-*      (11 articles — cybersecurity news, breaches)
│   ├── 2026-05-29-*      (5 articles — malware, convertkit, norton)
│   └── 2026-05-30-*      (4 articles — 1password, liquid web, cyberghost)
├── data/
│   ├── content-briefs.json        # Keyword briefs from SEO Agent
│   ├── affiliate-programs.json    # All affiliate programs with IDs
│   ├── keyword-database.json      # Full keyword research DB
│   └── reactive-content-queue.json # Reactive content queue
├── templates/
│   ├── best-of-template.md
│   └── comparison-template.md
└── reports/               ← HTML daily reports from the content runs
```

## What To Do With It

1. **Publish the drafts** — each is a full SEO-optimised article with affiliate link placeholders. Replace `[AFFILIATE_LINK:name]` with your actual affiliate URLs.
2. **Use the briefs** — `content-briefs.json` has the SEO keyword research. Generate more articles from the same briefs.
3. **Use the skill** — see `HANDOFF.md` for the full `hermes-content-agent-workflow` skill that powers this pipeline.
4. **Categories covered**: VPNs, Password Managers, Web Hosting, Cybersecurity News, Ecommerce (Shopify), SaaS tools, Antivirus

## Technical Notes

- All articles include FTC disclosure and HPASCA framework
- Word counts: 1500-3000 words each
- Articles have internal links using slug format — replace or remove as needed
- JSON-LD schema blocks at the end of each article

---

*Handed off from Folio (Khan Lala) — 30 May 2026*
