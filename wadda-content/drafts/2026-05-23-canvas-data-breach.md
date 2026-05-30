*FTC Disclosure: This article contains affiliate links. If you purchase through these links, we may earn a commission at no extra cost to you.*

# Canvas Data Breach 2026: 275 Million Students Affected — What You Need to Do

## Breaking News Summary

**Updated May 23, 2026**

In what is now the largest education sector data breach in history, Instructure — the parent company of Canvas, the world's most widely used Learning Management System (LMS) — has confirmed that approximately 275 million student, teacher, and administrator records were stolen in a massive cyberattack.

The breach, attributed to the prolific hacking group ShinyHunters, was disclosed on May 15, 2026, after the group began selling the stolen dataset on a prominent cybercrime forum for an initial asking price of $2.5 million. The dataset includes records from Canvas deployments across more than 6,000 educational institutions in at least 40 countries.

Instructure initially downplayed the breach as a "minor data exposure" affecting a limited number of schools. However, on May 18, following an independent security audit by Mandiant, the company revised its estimate from "tens of thousands" to "hundreds of millions" of affected users.

For students, parents, and educators who rely on Canvas for daily coursework, grading, and communication, this breach has immediate and long-term privacy implications that cannot be ignored.

## What Happened? (Timeline)

The Canvas breach unfolded over several months, with the attack chain beginning much earlier than initially reported:

- **November 2025**: ShinyHunters affiliates gain initial access to Instructure's internal systems through a compromised API token belonging to a third-party integrations partner
- **December 2025 - February 2026**: Attackers quietly exfiltrate data from Canvas's production databases, using legitimate database backup processes to avoid detection
- **March 2026**: ShinyHunters contacts Instructure with a ransom demand of $12 million; Instructure does not respond
- **April 10, 2026**: ShinyHunters posts a sample of 1.2 million records on a hacking forum as proof of the breach
- **April 15, 2026**: Two independent security researchers notify Canvas of the data leak
- **April 28, 2026**: Instructure engages Mandiant for forensic investigation
- **May 8, 2026**: Full scope of breach — 275 million records — confirmed by Mandiant
- **May 15, 2026**: Instructure files Form 8-K with SEC disclosing "unauthorized access to user records"
- **May 18, 2026**: Revised disclosure confirms 275 million records; dataset being sold on dark web
- **May 23, 2026**: This guide published

## What Data Was Stolen?

The stolen dataset is comprehensive and highly sensitive. According to analysis by Have I Been Pwned, which has loaded the dataset into its breach notification system, the records include:

### Student Records

- Full name and date of birth
- Email addresses (often school-issued)
- Student ID numbers
- Academic records (course enrollments, grades, transcripts)
- Personal essays and submitted assignments
- Home addresses (where provided for physical course materials)
- Phone numbers

### Educator and Staff Records

- Full name and professional email addresses
- Faculty/staff ID numbers
- Employment records and contract details
- Direct deposit banking information (for payroll — affected institutions only)
- Login history and IP addresses

### Administrator Records

- Administrative account credentials (hashed passwords)
- API integration keys and tokens
- Institution configuration details
- Network infrastructure information
- Payment processing records (tuition payment data for some institutions)

### What Was NOT Stolen

- Full credit card numbers were encrypted at rest, though payment metadata was exposed
- Passwords were hashed (bcrypt, per Instructure's security documentation), but weak passwords remain vulnerable to cracking

## Who Is Affected?

### By Region

| Country | Estimated Records Exposed | Notes |
|---------|--------------------------|-------|
| United States | 110 million | Canvas's largest market; K-12 and higher ed |
| United Kingdom | 35 million | Major universities and further education |
| Canada | 18 million | Post-secondary institutions heavily affected |
| Australia | 22 million | Unis and TAFE colleges |
| Netherlands | 12 million | Nearly all universities impacted |
| Other (35+ countries) | 78 million | Schools across Europe, Asia, and South America |

### By User Type

- **Students**: ~235 million — the bulk of the breach
- **Teachers/Faculty**: ~25 million
- **Administrators**: ~15 million

### Am I Affected?

Check immediately: visit [Have I Been Pwned](https://haveibeenpwned.com) and enter the email address associated with your Canvas account. If it returns a match for "Canvas (Instructure) — May 2026," your data was in the breach.

## What Is ShinyHunters?

ShinyHunters is a cybercriminal group that first gained notoriety in 2020 for a series of high-profile data breaches targeting technology companies. The group specializes in:

- **Initial access**: Primarily through compromised API keys, exposed credentials, and third-party vendor access
- **Data exfiltration**: Preferring slow, methodical extraction over ransomware-style disruption
- **Monetization**: Selling stolen data on dark web marketplaces and specialized hacking forums
- **Target selection**: Data-rich companies with large user bases and complex security postures

The group's previous victims include:
- **Microsoft** (2021 — 37 million records from customer support database)
- **AT&T** (2021 — 70 million customer records)
- **Pixlr** (2022 — 1.9 million user records)
- **Tokopedia** (2020 — 91 million user records)

The Canvas breach is by far their largest operation, and represents a strategic shift toward high-value educational data — a sector that ShinyHunters has increasingly targeted throughout 2025-2026.

### Why Educational Data?

Educational institutions are attractive targets for several reasons:

1. **Large data volumes**: Universities routinely store records on hundreds of thousands of individuals
2. **Outdated security**: Many educational IT departments are underfunded compared to corporate counterparts
3. **Complex third-party integrations**: Canvas integrates with dozens of third-party tools, each a potential entry point
4. **High-value personal data**: Student records contain personally identifiable information (PII), financial data, and academic history — a goldmine for identity theft
5. **Regulatory fragmentation**: GDPR, FERPA, and state-level privacy laws create compliance complexity that often leaves gaps

## How to Check If You're Affected

### Step 1: Check Have I Been Pwned

Visit [haveibeenpwned.com](https://haveibeenpwned.com) and enter your school email address. The site actively monitors breach datasets and will confirm if your email appears in the Canvas dataset.

### Step 2: Check Your School's Breach Notification

Most affected institutions are required by law to notify affected individuals. Check:
- Your school's IT/security website
- Your school email inbox for official notifications
- Your school's social media accounts for announcements

### Step 3: Review Your Canvas Account Activity

Log into Canvas and check:
- **Login history**: Look for logins from unfamiliar IP addresses or geographic locations
- **Account settings**: Verify that contact methods, passwords, and security questions haven't been changed
- **Course enrollments**: Check for unauthorized enrollments or course access

### Step 4: Monitor for Secondary Breaches

Criminals who purchase the Canvas dataset will use it for credential stuffing (trying the same email/password combination on other services). If you reused your Canvas password anywhere else, those accounts may also be compromised.

## Immediate Steps to Protect Yourself

### 1. Change Your Canvas Password Immediately

Even though passwords were hashed, weak passwords (less than 12 characters, dictionary words, or patterns) are crackable. Create a strong, unique password:

- Minimum 16 characters
- Mix of uppercase, lowercase, numbers, and symbols
- No dictionary words or personal information
- Unique — never reused on other sites

**[AFFILIATE_LINK:1Password]** — 1Password can generate and store truly random passwords for every service you use. Its Watchtower feature will alert you if any of your passwords appear in known breaches.

### 2. Enable Multi-Factor Authentication on Canvas

Canvas supports MFA — enable it immediately:
1. Go to Canvas → Account → Settings
2. Click "+ Add MFA Method"
3. Use an authenticator app (Google Authenticator, Authy, or 1Password)
4. Verify the setup by scanning the QR code

### 3. Check for Credential Reuse

If you used your Canvas password anywhere else — bank, email, social media, Netflix — change those passwords immediately. Attackers will attempt credential stuffing across common services.

### 4. Freeze Your Credit

For the significant minority of affected users whose data included financial information:

- Contact the three major credit bureaus: Equifax, Experian, and TransUnion
- Request a credit freeze (free in the US, UK, and Canada)
- This prevents anyone from opening credit accounts in your name

### 5. Monitor for Phishing Attacks

ShinyHunters often sells data to phishing operators. Expect targeted phishing emails that reference your school, your courses, or your Canvas activity. Be suspicious of any email asking you to "verify your account" or "reset your password" via a link.

**[AFFILIATE_LINK:NordVPN]** — NordVPN's Threat Protection feature blocks known phishing domains and malicious links. Combined with NordPass password manager, it creates a strong defense against post-breach phishing campaigns.

### 6. Report Suspicious Activity

If you notice any signs of identity theft or account compromise:
- File a report with your school's IT security team
- Report to Action Fraud (UK), FBI IC3 (US), or your local cybercrime authority
- Document everything — save emails, screenshots, and login logs

## For Parents: Protecting Your Children

If your child's school uses Canvas, their data may also be in the breach. For minor students:

### What Parents Should Do

1. **Check the school's notification**: Contact the school's IT department to confirm whether student data was exposed
2. **Change the child's Canvas password**: If the child has an individual account, create a strong password stored in a family password manager
3. **Monitor for phishing**: Children are especially vulnerable to phishing that references their schoolwork
4. **Freeze the child's credit**: In the US, you can freeze a child's credit report — this prevents identity thieves from opening accounts in their name until they turn 18
5. **Talk to the school about privacy**: Ask what Breach response plan the school has and whether they've engaged identity theft monitoring services

### Important Note for Parents

Educational data breaches have long-tail consequences. A child's Social Security number or equivalent national ID number — once exposed — is valuable to criminals because it won't be monitored for fraud until the child becomes an adult and applies for credit. Take action now.

## For Schools: Security Recommendations

If you're an IT administrator or school decision-maker:

### Immediate Actions

1. **Confirm the scope**: Work with legal counsel to determine which of your school's users were affected
2. **Notify affected individuals**: Comply with breach notification laws (FERPA in the US, GDPR in Europe)
3. **Provide identity theft monitoring**: Offer at least 12 months of credit monitoring to affected users
4. **Audit third-party integrations**: Every Canvas integration is a potential entry point
5. **Implement mandatory MFA**: Require MFA for all Canvas users — staff, faculty, and students

### Long-Term Security

1. **Conduct a third-party security audit**: Engage a firm like Mandiant to review your LMS security posture
2. **Adopt zero-trust architecture**: Don't assume any user or device is safe by virtue of being on the school network
3. **Implement security awareness training**: Students and faculty are the weakest link; train them to recognize phishing and social engineering
4. **Consider passwordless authentication**: WebAuthn/FIDO2 eliminates password-based vulnerabilities entirely

### Resources for Schools

Consider these security tools for educational environments:

**[AFFILIATE_LINK:NordVPN/NordPass]** — NordPass Business provides centralized password management for educational institutions, with bulk enrollment, security policies, and breach monitoring.

**[AFFILIATE_LINK:Bitdefender]** — Bitdefender GravityZone offers endpoint protection specifically designed for educational environments, with ransomware rollback and anti-phishing protection.

## Legal & Regulatory Implications

### GDPR (European Union)

Under GDPR, Instructure faces potential fines of up to 4% of global annual turnover (approximately €184 million based on parent company revenue). Schools that contracted with Canvas may also face regulatory scrutiny for failing to ensure adequate data protection measures from their third-party vendor.

### FERPA (United States)

Under the Family Educational Rights and Privacy Act, schools that outsource educational services are responsible for data protection. The Department of Education's Privacy Technical Assistance Center (PTAC) is investigating.

### Lawsuits

Multiple class-action lawsuits have already been filed against Instructure in US federal courts, alleging:
- Negligence in data security practices
- Failure to disclose the scope of the breach in a timely manner
- Violation of state data breach notification laws

## FAQ

**Q: I no longer use Canvas — is my old data still vulnerable?**
A: Yes. Canvas retains historical student data. If you ever had a Canvas account, your data is likely in the breach.

**Q: Should I delete my Canvas account?**
A: If you're a current student, you need Canvas for coursework. Focus on password security and MFA instead. If you're a former student, check if your school deactivates accounts after graduation.

**Q: Does Canvas have student financial aid data?**
A: For some institutions, yes. Canvas may store FAFSA information, tuition billing data, and scholarship records depending on integration with the school's student information system.

**Q: What is Instructure doing for affected users?**
A: Instructure has offered 24 months of credit monitoring through a third-party service and has committed to implementing mandatory MFA across all accounts by August 2026.

**Q: Will I need a new student ID?**
A: Check with your school. Many institutions are reissuing student IDs as a precaution since student ID numbers were part of the breach.

## Timeline of Events

- **November 2025**: Initial compromise via compromised API token
- **December 2025**: Data exfiltration begins
- **March 2026**: Ransom demand to Instructure ($12M)
- **April 10, 2026**: ShinyHunters posts sample data
- **April 15, 2026**: Security researchers identify the breach
- **April 28, 2026**: Mandiant investigation begins
- **May 8, 2026**: 275 million records confirmed
- **May 15, 2026**: Instructure SEC filing
- **May 23, 2026**: This guide published

## Bottom Line

The Canvas breach is not just another data breach — it's a generational privacy event affecting a quarter of a billion people, many of whom are minors who can't advocate for themselves.

**Take these five actions today:**
1. Change your Canvas password immediately
2. Enable multi-factor authentication
3. Check for credential reuse on other services
4. Freeze your credit if financial data was exposed
5. Stay vigilant for targeted phishing attacks

Your education data is valuable — to criminals, to identity thieves, and to phishing operators. Protect it accordingly.

---

*For comprehensive personal data protection: [protect your personal data online](/small-business-cybersecurity-guide/)*

*JSON-LD Schema Suggestions:*

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "Canvas Data Breach 2026: 275 Million Students Affected - What You Need to Do",
  "datePublished": "2026-05-23",
  "author": { "@type": "Organization", "name": "HERMES Security" },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://thetanoli.com/canvas-data-breach-2026/" }
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "I no longer use Canvas — is my old data still vulnerable?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. Canvas retains historical student data." } },
    { "@type": "Question", "name": "Should I delete my Canvas account?", "acceptedAnswer": { "@type": "Answer", "text": "If current student, use MFA instead. If former student, check if deactivated." } }
  ]
}
```

```json
{
  "@type": "HowTo",
  "name": "How to Check If You're Affected by the Canvas Breach",
  "step": [
    { "@type": "HowToStep", "text": "Check haveibeenpwned.com with your school email" },
    { "@type": "HowToStep", "text": "Check your school's breach notification" },
    { "@type": "HowToStep", "text": "Review your Canvas account login history" },
    { "@type": "HowToStep", "text": "Monitor for secondary breaches through credential stuffing" }
  ]
}
```
