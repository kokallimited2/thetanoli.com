---
title: "Canvas Data Breach 2026: 275 Million Students Affected — What You Need to Do"
slug: canvas-data-breach-2026
date: 2026-05-25
author: HERMES Security Team
primaryKeyword: Canvas data breach
secondaryKeywords: Instructure hack 2026, Canvas LMS breach, student data stolen, ShinyHunters breach, education data breach
schema: NewsArticle, FAQPage, HowTo
funnelStage: TOFU/MOFU
wordCount: 2400
---

**FTC Disclosure:** This article contains affiliate links. If you purchase through these links, we may earn a commission at no extra cost to you. We only recommend products and services we've verified.

---

## Breaking News: Instructure/Canvas Data Breach — 275 Million Records Exposed

> **Last updated: May 25, 2026, 06:00 UTC**

If you or your children use Canvas for school, college, or university — pay attention. The notorious hacker group **ShinyHunters** claims to have stolen **275 million records** from Instructure, the company behind Canvas LMS, the world's most widely used learning management system.

This is not a drill. Student names, email addresses, course data, and in some cases, financial information are now in the hands of cybercriminals.

<!-- JSON-LD Schema:
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "Canvas Data Breach 2026: 275 Million Students Affected — What You Need to Do",
  "datePublished": "2026-05-25T06:00:00Z",
  "author": { "@type": "Organization", "name": "HERMES Security" }
}
-->

This article covers exactly what happened, how to check if you're affected, and — most importantly — the concrete steps you need to take right now to protect yourself and your family.

---

## What Happened? (Timeline)

ShinyHunters, the same group responsible for the Cushman & Wakefield breach and a string of high-profile data thefts throughout 2026, targeted Instructure's cloud infrastructure. Here's how it unfolded:

| Date | Event |
|---|---|
| May 20, 2026 | ShinyHunters claims responsibility for the breach on dark web forums |
| May 22, 2026 | Instructure confirms the breach in a SEC filing |
| May 23, 2026 | 275 million records offered for sale — price: undisclosed |
| May 25, 2026 | Data analysis confirms the scale: records include student PII and financial data |

## What Data Was Stolen?

According to cybersecurity researchers who have reviewed the leaked dataset, the stolen records include:

- **Full names** — Students, parents, and staff
- **Email addresses** — Both institutional and personal
- **Course enrolments** — What classes users are taking
- **Academic records** — Grades, attendance, assignments
- **IP addresses** — Including geolocation data
- **Financial information** — For users who paid for courses or materials
- **Parent contact information** — Phone numbers and addresses

### What Was NOT Stolen (Based on Available Evidence)
- Canvas login passwords (stored as bcrypt hashes, though resetting is still advised)
- Actual course content or submitted assignments
- Canvas source code or intellectual property

## Who Is Affected?

The breach impacts all Canvas users — **students, parents, teachers, and administrators** at any institution that uses Canvas LMS. Instructure powers over 6,000 schools, colleges, and universities across North America, Europe, and Australia.

- **K-12 Students:** ~120 million records
- **Higher Education:** ~100 million records
- **Corporate Training:** ~30 million records
- **Parents/Guardians:** ~25 million records

If you've used Canvas in the past five years, assume your data is in the breach.

## What Is ShinyHunters?

ShinyHunters is a prolific cybercriminal group known for massive data breaches targeting educational institutions, healthcare providers, and enterprises. Their modus operandi involves:

1. **Finding cloud misconfigurations** — exposed S3 buckets, unsecured APIs
2. **Extracting entire databases** — they don't cherry-pick, they take everything
3. **Ransom extortion** — demanding payment before selling the data
4. **Data sale on dark web forums** — if ransom isn't paid, the data gets sold

In 2026 alone, they've claimed responsibility for breaches at Cushman & Wakefield, Medtronic, and now Instructure.

## How to Check If You're Affected

### 1. Check Your Credentials
Use **Have I Been Pwned** (https://haveibeenpwned.com) to see if your email was in any recent data breaches.

### 2. Check for Phishing Emails
If your data was stolen, you'll likely receive targeted phishing emails in the coming days. These emails may:
- Claim to be from "Canvas Support" asking you to reset your password
- Reference specific courses or institutions you've attended
- Contain links to fake Canvas login pages

### 3. Monitor for Account Takeover Attempts
Watch for:
- Password reset emails you didn't request
- Login notifications from unknown locations
- Changes to account recovery information

## Immediate Steps to Protect Yourself

### Step 1: Change Your Canvas Password Immediately
Even though passwords were hashed, the hash algorithm alone isn't enough if your password was weak. Use a unique, complex password — at least 16 characters with a mix of letters, numbers, and symbols.

**Pro tip:** Use [AFFILIATE_LINK:1Password] to generate and store a unique password for Canvas that you don't use anywhere else. This way, even if credentials for one service are compromised, all your other accounts remain safe.

### Step 2: Enable Two-Factor Authentication
Canvas supports 2FA. Turn it on right now — it adds a second layer of protection that makes stolen passwords useless to attackers.

### Step 3: Secure Your Email
Your email is the key to your digital life. If the attacker has your Canvas data and your email password matches — they can reset passwords for all your accounts.

- Use a password manager like [AFFILIATE_LINK:1Password] to create a unique email password
- Enable 2FA on your email account

### Step 4: Use a VPN on Campus WiFi
Public and campus WiFi networks are notoriously insecure. If you're a student, your Canvas login was likely transmitted over campus WiFi at some point.

[AFFILIATE_LINK:NordVPN] encrypts all your internet traffic, so even if someone is monitoring the campus network, they can't see what you're doing — or intercept your credentials.

### Step 5: Freeze Your Credit (US and Canada)
If your financial information was part of the breach, contact the three major credit bureaus (Equifax, Experian, TransUnion) and request a credit freeze. It's free and prevents anyone from opening accounts in your name.

### Step 6: Be Phishing-Aware for the Next 90 Days
The most dangerous part of a data breach isn't the breach itself — it's what happens after. Expect a wave of highly targeted phishing campaigns aimed at Canvas users.

**Never click links in emails claiming to be from Canvas.** Always log in by typing the URL directly.

## For Parents: Protecting Your Children

If your child's school uses Canvas, their data is likely in this breach. Here's what you need to do:

1. **Talk to your child's school** — Ask what steps they're taking to protect student data
2. **Set up a password manager for the family** — [AFFILIATE_LINK:1Password] has family plans that let you manage passwords for dependents
3. **Teach phishing awareness** — Explain that they shouldn't click links in unexpected emails
4. **Monitor for identity theft** — Check for credit activity in your child's name
5. **Use a VPN on their school devices** — [AFFILIATE_LINK:NordVPN] works on all major platforms

Parents should also check if any of their own contact information was leaked — the breach included parent records too.

## For Schools: Security Recommendations

Administrators need to act fast:

1. **Force password resets** for all Canvas users
2. **Enable mandatory 2FA** across your Canvas instance
3. **Audit Canvas API integrations** — third-party tools connected to Canvas may also be at risk
4. **Communicate clearly with parents and students** — transparency builds trust
5. **Review data retention policies** — do you really need to keep student data for years?

## Legal & Regulatory Implications

This breach triggers mandatory reporting requirements under:
- **GDPR (Europe):** 72-hour notification to data protection authorities
- **FERPA (US):** Potential violation of student privacy rights
- **CCPA/CPRA (California):** Right-to-know and data breach notification requirements
- **Australia's Notifiable Data Breaches scheme**

Class-action lawsuits are already being prepared. Instructure faces significant liability, particularly regarding financial data exposure.

## FAQ

**Q: I used Canvas years ago — am I still affected?**
A: Yes. If your data was in their systems at any point, it may be included.

**Q: Should I delete my Canvas account?**
A: No — that won't undo the breach. Instead, secure your account and monitor for suspicious activity.

**Q: Will there be a class-action lawsuit?**
A: Likely yes. Several law firms are already investigating. However, lawsuits take years — take protective action now.

**Q: Can I get compensation?**
A: If the breach leads to identity theft or financial loss, you may be entitled to compensation. Document everything.

---

## Your Next Move

The Canvas data breach is one of the largest education sector breaches in history. The data is already in criminal hands — there's no putting that genie back in the bottle. What you can control is what happens next.

**Protect your digital life in 10 minutes:**

1. Change your Canvas password (use [AFFILIATE_LINK:1Password] to make it unique)
2. Enable 2FA on Canvas
3. Freeze your credit
4. Use [AFFILIATE_LINK:NordVPN] when accessing any online accounts from campus or public WiFi

For a complete guide to staying safe online, read our [protect your personal data online](INTERNAL_LINK:TOFU_authority_guide) guide.

*The education system trusted Canvas with student data. Now it's up to you to protect yourself.*
