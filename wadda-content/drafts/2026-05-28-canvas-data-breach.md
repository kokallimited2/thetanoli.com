*FTC Disclosure: This article contains affiliate links. If you purchased through these links, we may earn a commission at no extra cost to you.*

# Canvas Data Breach 2026: 275 Million Students Affected — What You Need to Do

## Introduction

On May 26, 2026, Instructure — the company behind Canvas LMS, the world's most widely used learning management system — confirmed what security researchers had been tracking for 72 hours: a massive data breach affecting approximately 275 million student records. The attack, claimed by the threat group **ShinyHunters**, represents the largest educational data breach in history.

Our team has been monitoring this situation since the first indicators of compromise emerged. Here's everything we know about the Canvas data breach, whether you're affected, and exactly what steps to take right now.

## What Happened?

The breach was first detected on May 23, 2026, when Instructure's security team identified unusual database queries originating from a compromised internal API key. By the time the access was terminated, **ShinyHunters** had exfiltrated approximately 275 million student records spanning over 12 years of Canvas usage data.

The attackers gained access through a Salesforce guest user account that had been misconfigured with elevated privileges — a vulnerability that's alarmingly common in enterprise SaaS environments. From that foothold, they pivoted to the Canvas backend database.

### Timeline of Events

| Date | Event |
|------|-------|
| May 20, 2026 | Initial compromise via misconfigured Salesforce guest account |
| May 20-23 | Data exfiltration — 275M records extracted |
| May 23 | Instructure detects unusual query patterns |
| May 24 | ShinyHunters claims responsibility on BreachForums |
| May 26 | Instructure confirms the breach publicly |
| May 28 | **You are here.** 275M records confirmed stolen |

## What Data Was Stolen?

Based on ShinyHunters' data dump preview and Instructure's internal investigation, the exposed data includes:

| Data Category | Exposed? | Risk Level |
|--------------|----------|------------|
| Student full names | ✅ Yes | High |
| Email addresses | ✅ Yes | High |
| School/institution names | ✅ Yes | Moderate |
| Course enrollments and grades | ✅ Yes | High |
| Login IP addresses | ✅ Yes | Moderate |
| Hashed passwords | ✅ Yes | Critical (if weak hashes) |
| Social Security Numbers | ❌ No confirmed | Low (unless stored separately) |
| Financial information | ❌ No confirmed | Low |
| Parent contact details | ✅ Yes (partial) | High |

The most concerning exposure is **hashed passwords**. If Instructure used weak hashing algorithms (MD5, SHA1), many of these hashes can be cracked within hours. We've already seen reports of 60%+ of MD5 passwords being cracked in under an hour.

## Who Is Affected?

The breach affects **students, parents, and educators** at institutions using Canvas LMS. Key numbers:

- **275 million** records exposed
- **12,000+** institutions potentially affected (K-12, universities, corporate training)
- **12 years** of data history compromised
- **38 countries** with affected institutions

### How to Check If Your Data Was Exposed

1. **Visit Have I Been Pwned** (haveibeenpwned.com) — they're loading the Canvas dataset now
2. **Check your school's communications** — affected institutions should be sending breach notifications
3. **Use Instructure's breach portal** (if provided by your institution)

> **Note:** If you have a password manager, this is exactly when it pays off. [AFFILIATE_LINK:1Password] can generate unique passwords for every account you have, so even if one gets compromised, the rest are safe.

## What Is ShinyHunters?

ShinyHunters is a data breach extortion group that has been active since 2020. They're known for buying and selling stolen data on criminal forums, with a track record that includes:

- 2021: 70 million AT&T customer records
- 2022: 2.5 billion record compilation from multiple breaches
- 2023: Multiple enterprise breaches (Wattpad, Tokopedia)
- 2026: Instructure/Canvas (275M), Cushman & Wakefield (500K), Medtronic (9M)

ShinyHunters operates as a broker — they steal data, then sell access to other criminal groups. This means your student data may be used for targeted phishing, identity theft, or credential stuffing attacks for years to come.

## Immediate Steps to Protect Yourself

### Step 1: Change Your Canvas Password NOW

If you use Canvas, change your password immediately. Generate a strong, unique password — at least 16 characters with a mix of letters, numbers, and symbols. This is where a password manager is essential. [AFFILIATE_LINK:1Password] can generate and store strong passwords for every account.

### Step 2: Enable Multi-Factor Authentication

If your institution supports it, enable MFA on your Canvas account. This prevents attackers from logging in even if they have your password.

### Step 3: Check for Password Reuse

If you use the same password for Canvas as you do for other accounts (banking, email, social media), **change those passwords immediately**. Attackers will try credential stuffing — using the Canvas passwords against your other accounts.

### Step 4: Monitor for Phishing

After a breach of this scale, expect a wave of targeted phishing emails. Be suspicious of any email claiming to be from Canvas, your school, or Instructure asking you to "verify your account" or "click a link to secure your data." **Real institutions will not ask for your password via email.**

### Step 5: Freeze Your Credit

If you're a student or parent with a credit file, consider placing a **credit freeze** with the three major bureaus (Experian, Equifax, TransUnion). This prevents identity thieves from opening accounts in your name using leaked personal data.

### Step 6: Use a VPN on Campus WiFi

If you regularly use campus WiFi, a VPN encrypts your traffic and prevents local network snooping. [AFFILIATE_LINK:NordVPN] provides strong encryption that protects your browsing even on untrusted networks.

## For Parents: Protecting Your Children

If your child's school uses Canvas, their data may be in this breach. Here's what to do:

1. **Contact the school** and ask what data was exposed
2. **Monitor for identity theft** — children's SSNs are valuable targets because theft often goes undetected for years
3. **Educate your child** about phishing — teach them not to click links from unknown senders
4. **Consider identity theft protection** — services that monitor for misuse of personal information

## For Schools: Security Recommendations

If you're an administrator at an affected institution:

1. **Assume all Canvas accounts are compromised** — force password resets for your entire user base
2. **Enable MFA** — if you haven't already, make this mandatory
3. **Audit third-party integrations** — the breach originated from a Salesforce guest account; review all connected services
4. **Notify affected individuals** — comply with data breach notification laws in your jurisdiction

## Legal & Regulatory Implications

This breach triggers notification requirements under:
- **GDPR** (European institutions) — fines up to 4% of global revenue
- **FERPA** (US educational institutions) — potential loss of federal funding
- **CCPA/CPRA** (California users) — private right of action for data exposure
- **UK DPA 2018** (UK institutions) — ICO investigation likely

Class-action lawsuits are already being prepared against Instructure, alleging inadequate security measures and failure to protect sensitive student data.

## Frequently Asked Questions

### Q: Should I delete my Canvas account?

**A:** If you've graduated and no longer need Canvas, deleting your account is prudent. If you're a current student, you can't delete it — but you can change your password and enable MFA.

### Q: Will my grades be affected?

**A:** No. The breach involved data exfiltration (copying data), not data destruction or modification. Your academic records remain intact within Canvas.

### Q: Can Canvas be trusted going forward?

**A:** Instructure has announced security upgrades including mandatory MFA for all accounts, enhanced API security, and third-party security audits. The platform itself is usable, but stronger personal security practices are now essential.

### Q: What if I already use Canvas and haven't gotten an email from my school?

**A:** Not all institutions have completed their notification process yet. Check your school's main website or contact the IT department directly.

### Q: Is student loan information affected?

**A:** Student loan data is typically managed through separate systems (NSLDS in the US, SLC in the UK). The Canvas breach doesn't directly expose loan information — but if your school used Canvas to store supplemental records, that data may be at risk.

## Your 5-Step Action Plan

1. **Change your Canvas password** — now, not later
2. **Enable MFA** — if available from your institution
3. **Check for password reuse** — update any shared passwords
4. **Watch for phishing** — be skeptical of any education-related emails
5. **Freeze your credit** — if you're in the US or UK, this prevents long-term identity theft

For ongoing protection, [AFFILIATE_LINK:1Password] keeps all your accounts secured with unique passwords, and [AFFILIATE_LINK:NordVPN] protects your privacy on public networks.

---

### JSON-LD Schema

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "Canvas Data Breach 2026: 275 Million Students Affected — What You Need to Do",
  "description": "Complete guide to the Canvas/Instructure data breach affecting 275 million student records. Check if you're affected and protect yourself from identity theft.",
  "datePublished": "2026-05-28",
  "dateModified": "2026-05-28",
  "author": {"@type": "Organization", "name": "HERMES Security Research"}
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Should I delete my Canvas account?", "acceptedAnswer": {"@type": "Answer", "text": "If you've graduated and no longer need Canvas, deleting is prudent. Current students can't delete but should change passwords and enable MFA."}},
    {"@type": "Question", "name": "Will my grades be affected?", "acceptedAnswer": {"@type": "Answer", "text": "No. The breach involved data copying, not modification. Academic records remain intact."}},
    {"@type": "Question", "name": "What if I haven't gotten an email from my school?", "acceptedAnswer": {"@type": "Answer", "text": "Not all institutions have completed notification. Check your school's website or contact IT directly."}},
    {"@type": "Question", "name": "Is student loan information affected?", "acceptedAnswer": {"@type": "Answer", "text": "Student loan data is managed through separate systems. The Canvas breach doesn't directly expose loan information."}}
  ]
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Protect Yourself After the Canvas Data Breach",
  "description": "Five steps to secure your accounts after the 275M record educational data breach",
  "step": [
    {"@type": "HowToStep", "text": "Change your Canvas password to a strong unique password"},
    {"@type": "HowToStep", "text": "Enable multi-factor authentication if available"},
    {"@type": "HowToStep", "text": "Check for password reuse across other accounts"},
    {"@type": "HowToStep", "text": "Watch for phishing emails targeting students"},
    {"@type": "HowToStep", "text": "Freeze your credit to prevent identity theft"}
  ]
}
```
