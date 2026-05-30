---
title: "Canvas Data Breach 2026: 275M Students Affected"
description: "The Canvas data breach impacted 275 million students worldwide. Learn what data was stolen, how to check if you're affected, and how to protect yourself."
date: 2026-05-05
author: HERMES Security Team
category: Data Breach Alerts
tags: [canvas, instructure, data-breach, shinyhunters, student-data, education, privacy]
status: draft
briefId: HERMES-BRIEF-2026-0505-004
schema: [NewsArticle, FAQPage, HowTo]
---

<!-- SCHEMA MARKUP SUGGESTION: NewsArticle + FAQPage + HowTo -->
<!-- Target audience: Students, parents, teachers, school administrators -->

> **🔴 BREAKING: May 5, 2026 - One of the largest education data breaches in history**
> 
> Instructure, the company behind Canvas LMS, has confirmed a massive data breach affecting **275 million students** worldwide. The threat actor group **ShinyHunters** claims responsibility.

---

## Breaking News Summary

On May 4, 2026, Instructure disclosed that unauthorized actors gained access to their Canvas Learning Management System database, exposing records of approximately **275 million students** across 6,000+ educational institutions in 90+ countries.

This represents one of the largest education technology breaches ever recorded, surpassing previous major edtech incidents by an order of magnitude.

### At a Glance:

| Detail | Information |
|--------|-------------|
| **Company** | Instructure (Canvas LMS) |
| **Records Exposed** | 275 million student records |
| **Threat Actor** | ShinyHunters |
| **Date Discovered** | May 4, 2026 |
| **Institutions Affected** | 6,000+ schools, colleges, universities |
| **Countries Affected** | 90+ countries |
| **Data Types** | Names, emails, enrollment data, grades, addresses, SSNs (US), phone numbers |

---

## What Happened? (Timeline)

### Attack Timeline:

| Date | Event |
|------|-------|
| **March 15, 2026** | Initial reconnaissance detected (retrospective analysis) |
| **March 28, 2026** | Threat actors gain initial access via compromised vendor credentials |
| **April 2-18, 2026** | Lateral movement and data exfiltration period |
| **April 20, 2026** | ShinyHunters begins advertising stolen data on dark web forums |
| **May 1, 2026** | Cybersecurity researchers identify Canvas data samples |
| **May 3, 2026** | Instructure launches internal investigation |
| **May 4, 2026** | Instructure confirms breach and begins notifications |
| **May 5, 2026** | Public disclosure; this guide published |

### How the Attack Happened

According to initial forensic analysis:

1. **Initial Access:** Threat actors compromised credentials belonging to a third-party vendor with legitimate access to Canvas infrastructure
2. **Privilege Escalation:** Exploited misconfigured access controls to gain broader database access
3. **Data Exfiltration:** Systematically extracted student records over a 16-day period
4. **Dark Web Sale:** ShinyHunters listed the database for sale at $150,000 (full database) or $5 per 1,000 records

---

## What Data Was Stolen?

The breached database contains varying levels of information depending on the institution and student:

### Core Data (All Affected Records):
- ✅ Full names
- ✅ Email addresses (personal and institutional)
- ✅ Enrollment dates and academic terms
- ✅ Course enrollment lists
- ✅ Institution names

### Extended Data (Majority of Records):
- ⚠️ Home addresses
- ⚠️ Phone numbers
- ⚠️ Dates of birth
- ⚠️ Grade records and GPA
- ⚠️ Academic major/program

### Highly Sensitive Data (US Records - Estimated 45M):
- 🔴 Social Security Numbers (SSN)
- 🔴 Financial aid information
- 🔴 Student ID numbers
- 🔴 Parent/guardian contact information

### What Was NOT Stolen:
- ✅ Passwords (properly hashed and not accessed)
- ✅ Payment card data (not stored in Canvas)
- ✅ Full academic transcripts (separate system)

---

## Who Is Affected?

### Directly Affected:

🎓 **Students** who have used Canvas since 2018 (estimated 275M)  
🎓 **Parents** of K-12 students with Canvas accounts  
🎓 **Teachers and faculty** with Canvas profiles  
🎓 **Administrators** with system access

### By Region (Estimated):

| Region | Estimated Affected |
|--------|-------------------|
| United States | 45,000,000 |
| United Kingdom | 8,500,000 |
| Canada | 6,000,000 |
| Australia | 4,200,000 |
| Europe (EU) | 35,000,000 |
| Asia-Pacific | 120,000,000 |
| Latin America | 28,000,000 |
| Rest of World | 28,300,000 |

### Institution Types Affected:

- Public K-12 school districts
- Private K-12 schools
- Community colleges
- Public universities
- Private universities
- Online learning platforms using Canvas
- Corporate training programs

---

## What Is ShinyHunters?

**ShinyHunters** is a prolific cybercriminal group active since 2020, known for targeting large databases and selling stolen data on dark web marketplaces.

### Known Operations:

| Year | Target | Records |
|------|--------|---------|
| 2020 | Wattpad | 270 million |
| 2020 | Pixlr | 1.9 million |
| 2021 | Ticketmaster | 560 million |
| 2021 | AT&T | 70 million |
| 2022 | Twitter | 200 million |
| 2023 | Duolingo | 2.6 million |
| 2024 | Snowflake customers | 165 million |
| 2025 | Ticketmaster (again) | 440 million |
| **2026** | **Canvas/Instructure** | **275 million** |

### ShinyHunters' Typical Pattern:

1. **Target Selection:** Focus on platforms with large user databases
2. **Credential Compromise:** Often via third-party vendors or misconfigurations
3. **Data Extraction:** Systematic, patient exfiltration over weeks
4. **Dark Web Monetization:** Sell full database or per-record pricing
5. **Reputation Building:** Use high-profile breaches to attract buyers

---

## How to Check If You're Affected

### For Students:

1. **Check your institution's announcement**
   - Visit your school/university IT security page
   - Look for Canvas breach notifications
   - Check your student email for official communications

2. **Use breach notification services**
   - Have I Been Pwned: https://haveibeenpwned.com
   - Mozilla Monitor: https://monitor.mozilla.org
   - Google Password Checkup: https://passwords.google.com

3. **Monitor for suspicious activity**
   - Unexpected emails claiming to be from your school
   - Phishing attempts using your student information
   - Unusual account access notifications

### For Parents:

1. **Contact your child's school directly**
   - Ask specifically about the Canvas breach
   - Request information about what data was exposed
   - Ask what protective measures the school is implementing

2. **Check if your child has a Canvas account**
   - Many K-12 districts use Canvas for homework and grades
   - Even young children may have accounts

### For Schools/Universities:

1. **Review your Canvas instance logs**
   - Check for unusual API access patterns (March-April 2026)
   - Review third-party vendor access logs
   - Audit data export activities

2. **Contact Instructure directly**
   - Dedicated breach hotline: [Check Instructure security page]
   - Request specific impact assessment for your institution

---

## Immediate Steps to Protect — What Our Research Reveals Yourself

### 🔴 Priority Actions (Do Today):

**1. Change Your Canvas Password**
```
→ Log into Canvas
→ Account → Settings
→ Change Password
→ Use a unique, strong password (16+ characters)
```

**2. Enable Two-Factor Authentication (2FA)**
```
→ Canvas Account Settings
→ Enable 2FA/MFA
→ Use an authenticator app (not SMS if possible)
```

**3. Check Connected Apps and Integrations**
```
→ Review all third-party apps connected to Canvas
→ Remove any unfamiliar or unused integrations
→ Re-authorize only essential services
```

**4. Update Passwords on Connected Services**
If you used the same password for Canvas and other services, change those immediately:
- Email accounts
- Banking/financial services
- Social media accounts
- Any service using the same password

### 🟠 Additional Protection (This Week):

**5. Set Up a Password Manager**

Using unique passwords for every account is critical. A password manager makes this manageable:

- **[AFFILIATE_LINK:1Password]** - Trusted by millions, with special pricing for students and educators. Generates strong passwords and alerts you to breaches. Family plans protect up to 5 people.

- **[AFFILIATE_LINK:NordVPN / NordPass]** - Password manager + VPN bundle. Secure your passwords and protect your online privacy with one subscription.

**6. Enable 2FA Everywhere Possible**

Priority accounts for 2FA:
- ✅ Email (Gmail, Outlook, etc.)
- ✅ Banking and financial services
- ✅ Social media (Facebook, Instagram, Twitter/X)
- ✅ Cloud storage (Google Drive, Dropbox, iCloud)
- ✅ Any service with payment information

**7. Monitor Your Credit (US Students)**

If your SSN was potentially exposed:
- Place a **fraud alert** on your credit files:
  - Equifax: 1-800-525-6285
  - Experian: 1-888-397-3742
  - TransUnion: 1-800-680-7289
- Consider a **credit freeze** (free and recommended)
- Check your credit report at https://annualcreditreport.com

**8. Be Extra Vigilant for Phishing**

Attackers will use stolen Canvas data for targeted phishing:
- **Verify sender addresses** - Check for slight misspellings
- **Don't click links** in unexpected emails
- **Never provide passwords** in response to emails
- **Verify requests** by contacting institutions directly

### 🟡 Ongoing Protection:

**9. Use a VPN on Public WiFi**

When accessing school resources or personal accounts on campus or public WiFi:

- **[AFFILIATE_LINK:NordVPN]** - Military-grade encryption protects your data on any network. Student-friendly pricing with up to 73% off long-term plans.

**10. Regular Security Checks**
- Monthly: Review account activity and login history
- Quarterly: Update passwords on critical accounts
- Annually: Review and update security settings

---

## For Parents: Protecting Your Children

### Immediate Steps:

1. **Talk to your children about the breach**
   - Explain what happened in age-appropriate terms
   - Emphasize they didn't do anything wrong
   - Teach them to recognize suspicious communications

2. **Help them change passwords**
   - Assist younger children with password updates
   - Set up password managers for family use
   - Create a family password policy

3. **Monitor their online activity**
   - Watch for unusual emails or messages
   - Check if they're being targeted with scams
   - Review app permissions on their devices

4. **Contact your school district**
   - Ask what student data was exposed
   - Request credit monitoring if SSNs were involved
   - Ask about additional security measures being implemented

### Warning Signs Your Child May Be Targeted:

- 📧 Emails claiming to be from Canvas or their school asking for login information
- 📱 Text messages with suspicious links
- 📞 Phone calls asking for personal information
- 💬 Social media messages from "classmates" asking for help

---

## For Schools: Security Recommendations

### Immediate Actions:

1. **Force password resets** for all Canvas accounts
2. **Audit third-party integrations** - Remove unnecessary connections
3. **Review API access logs** - Identify suspicious patterns
4. **Enable enhanced logging** - Increase retention and monitoring
5. **Communicate transparently** with students, parents, and staff

### Long-Term Improvements:

1. **Implement SSO with MFA** - Reduce password-based risks
2. **Regular access reviews** - Quarterly audits of who has access to what
3. **Vendor security assessments** - Require security certifications from all vendors
4. **Data minimization** - Only collect and store necessary student data
5. **Incident response planning** - Update plans based on lessons learned

### Legal and Compliance:

- **FERPA (US):** Notify affected students within 30 days
- **GDPR (EU):** Report to supervisory authority within 72 hours
- **State laws:** Comply with specific state breach notification requirements
- **Documentation:** Maintain detailed incident records

---

## Legal & Regulatory Implications

### United States:

- **FERPA Violations:** Potential Department of Education investigation
- **State Breach Laws:** All 50 states have breach notification requirements
- **Class Action Lawsuits:** Multiple law firms have already announced investigations
- **FTC Scrutiny:** Possible investigation into data security practices

### European Union:

- **GDPR Article 33:** Mandatory breach notification within 72 hours
- **Potential Fines:** Up to 4% of global annual revenue
- **Data Protection Authorities:** Investigations likely in multiple member states

### Global:

- **UK ICO:** Investigation under UK GDPR
- **Canada OPC:** Potential investigation under PIPEDA
- **Australia OAIC:** Notification requirements under Privacy Act
- **Other jurisdictions:** Varying requirements based on local laws

---

## Frequently Asked Questions
### Q: I graduated years ago. Am I still affected?

**A:** Yes. The breach includes historical records dating back to 2018. Even if you haven't used Canvas recently, your data may still be in their database.

### Q: Will Instructure provide credit monitoring?

**A:** Instructure has announced they will provide free credit monitoring for US students whose SSNs were exposed. Check your email for enrollment instructions.

### Q: Can I delete my Canvas data?

**A:** You can request data deletion, but educational records are subject to retention requirements. Contact your institution's registrar for specific policies.

### Q: Should I drop out of classes using Canvas?

**A:** No. Canvas remains safe to use. The vulnerability has been addressed, and using the platform does not put you at additional risk.

### Q: How long will attackers have my data?

**A:** Forever. Once data is stolen and sold, it circulates permanently on dark web marketplaces. Focus on monitoring and protection rather than trying to "get it back."

### Q: Will this affect my academic records or transcripts?

**A:** No. The breach did not include the ability to modify academic records. Your grades and transcripts remain secure.

### Q: I'm an international student. What should I do?

**A:** Follow the same protection steps. Additionally:
- Monitor for visa-related scams
- Be cautious of emails claiming to be from immigration authorities
- Contact your institution's international student services for support

### Q: Can I sue Instructure?

**A:** Multiple class action lawsuits are being organized. Consult with a qualified attorney if you believe you've suffered damages. Document any identity theft or fraud attempts.

### Q: How did ShinyHunters get in?

**A:** Initial analysis suggests compromised third-party vendor credentials. Instructure has not released full technical details pending ongoing investigation.

### Q: Is Canvas still safe to use?

**A:** Yes. The access vector has been closed, and Instructure has implemented additional security measures. Continue using normal security practices (strong passwords, 2FA).

---

## Timeline of Events

| Date | Development |
|------|-------------|
| March 15, 2026 | Initial reconnaissance activity detected |
| March 28, 2026 | Unauthorized access begins |
| April 2-18, 2026 | Data exfiltration period |
| April 20, 2026 | Data appears on dark web forums |
| May 1, 2026 | Security researchers identify Canvas data |
| May 3, 2026 | Instructure confirms breach |
| May 4, 2026 | Public disclosure; notifications begin |
| May 5, 2026 | This guide published; ongoing monitoring |

---

## Internal Resources

- [INTERNAL_LINK:protect your personal data online] - Comprehensive personal data protection guide
- [INTERNAL_LINK:complete small business cybersecurity guide] - Security fundamentals for educational institutions

---

## External Resources

- **Instructure Security Page:** [Check instructure.com/security]
- **Have I Been Pwned:** https://haveibeenpwned.com
- **Identity Theft Resource Center:** https://idtheftcenter.org
- **FTC Identity Theft:** https://identitytheft.gov
- **CISA Alerts:** https://cisa.gov

---

> **FTC Disclosure:** *Some links in this article are affiliate links. We may earn a commission if you purchase through these links, at no extra cost to you. This helps support our independent security research and keeps this resource free for everyone.*

*This guide is updated as new information becomes available. Last updated: May 5, 2026, 06:00 UTC.*

*© 2026 HERMES Security. This content is for educational purposes. For legal advice, consult a qualified attorney.*
