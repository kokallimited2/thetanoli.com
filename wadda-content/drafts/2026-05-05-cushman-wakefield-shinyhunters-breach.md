---
title: "Cushman & Wakefield Breach: 500K Records Stolen"
description: "ShinyHunters stole 500,000 Salesforce records from Cushman & Wakefield. Learn how the breach happened and how to protect your enterprise CRM."
date: 2026-05-05
author: HERMES Security Team
category: Enterprise Security
tags: [cushman-wakefield, shinyhunters, salesforce, data-breach, enterprise-security, crm]
status: draft
briefId: HERMES-BRIEF-2026-0505-005
schema: [NewsArticle, FAQPage]
---

<!-- SCHEMA MARKUP SUGGESTION: NewsArticle + FAQPage -->
<!-- Target audience: CISOs, IT managers, business leaders, Salesforce administrators -->

> **🏢 ENTERPRISE SECURITY ALERT — May 5, 2026**
> 
> Global real estate giant Cushman & Wakefield has confirmed a data breach affecting 500,000 Salesforce records. The ShinyHunters group is again behind the attack, exploiting a known Salesforce guest user vulnerability.

---

## Breach Summary

On May 4, 2026, Cushman & Wakefield disclosed that threat actors gained unauthorized access to their Salesforce CRM instance, exfiltrating approximately **500,000 records** containing sensitive commercial real estate data.

### Key Facts:

| Attribute | Details |
|-----------|---------|
| **Victim** | Cushman & Wakefield |
| **Industry** | Commercial Real Estate |
| **Records Exposed** | 500,000 Salesforce records |
| **Threat Actor** | ShinyHunters |
| **Attack Vector** | Salesforce guest user vulnerability |
| **Date Discovered** | May 4, 2026 |
| **Data Types** | Client information, property records, deal data, employee records |

---

## ShinyHunters Campaign Overview

This breach is part of an ongoing ShinyHunters campaign targeting Salesforce instances worldwide. The group has systematically exploited a **guest user access vulnerability** that many organizations have failed to patch or properly configure.

### The Salesforce Guest User Vulnerability:

Salesforce's "guest user" feature allows external users limited access to certain records without authentication. Misconfigurations or unpatched vulnerabilities in this feature can allow escalation to full database access.

**Common misconfigurations exploited:**
- Guest users with read access to sensitive objects
- Overly permissive sharing rules
- Unpatched Salesforce instances running older API versions
- Custom code with insecure guest user handling

### ShinyHunters' Enterprise Targeting Pattern:

| Target Type | Recent Victims | Motivation |
|-------------|---------------|------------|
| Real Estate | Cushman & Wakefield | High-value client data |
| Education | Canvas/Instructure | Mass user databases |
| Healthcare | Medtronic | Medical/financial records |
| Technology | Various SaaS companies | Intellectual property |

---

## Salesforce Security Implications

### Why Salesforce Is a Prime Target:

1. **Centralized Data Hub** — CRMs contain customer, deal, and employee data
2. **API-Rich Environment** — Multiple integration points create attack surfaces
3. **Complex Permissions** — Easy to misconfigure access controls
4. **High Value Data** — Commercial data worth millions on dark web
5. **Third-Party Apps** — AppExchange apps can introduce vulnerabilities

### The Guest User Risk:

Salesforce guest users are designed for public-facing scenarios (customer portals, community pages). However, improper configuration creates serious risks:

**High-Risk Configurations:**
- Guest users with "View All" permissions
- Sharing rules exposing internal records
- Unauthenticated Apex controllers accessing sensitive data
- Community pages displaying non-public information

**Recommended Guest User Restrictions:**
- Minimal object access (only what's absolutely necessary)
- Field-level security on sensitive fields
- Regular access audits
- Enable "Secure Guest User Access" setting

---

## How to Secure Your CRM

### Immediate Actions (Today):

**1. Audit Guest User Permissions**
```
Setup → Users → Guest Users
→ Review each guest user profile
→ Remove unnecessary object permissions
→ Verify field-level security
```

**2. Review Sharing Rules**
```
Setup → Security → Sharing Settings
→ Audit all sharing rules
→ Remove overly permissive rules
→ Verify guest user access is minimal
```

**3. Check API Access**
```
Setup → API → API Usage
→ Review connected apps
→ Revoke unused integrations
→ Verify OAuth scopes are minimal
```

**4. Enable Enhanced Logging**
```
Setup → Event Monitoring
→ Enable Login History tracking
→ Enable Setup Audit Trail
→ Configure real-time event monitoring
```

### Short-Term Actions (This Week):

**5. Implement Multi-Factor Authentication (MFA)**
- Require MFA for all users, including API-only users
- Use Salesforce Authenticator or third-party MFA
- Enforce MFA at the profile level

**6. Conduct Permission Set Audit**
- Review all permission sets and profiles
- Remove redundant or excessive permissions
- Implement principle of least privilege
- Document approved permission architecture

**7. Review Third-Party Apps**
- Audit all AppExchange and custom apps
- Remove unused or unnecessary integrations
- Verify app security certifications
- Review OAuth scopes granted to apps

**8. Enable Field History Tracking**
- Track changes to critical fields
- Monitor for unauthorized modifications
- Set up alerts for suspicious activity

### Long-Term Improvements:

**9. Implement Salesforce Shield**
- Platform Encryption for sensitive data
- Event Monitoring for real-time analytics
- Field Audit Trail for long-term history
- Transaction Security for automated policies

**10. Regular Security Assessments**
- Quarterly permission audits
- Annual penetration testing
- Continuous monitoring with SIEM integration
- Security training for administrators

---

## Enterprise Protection Checklist

### CRM Security:

- [ ] MFA enabled for all users
- [ ] Guest users restricted to minimum permissions
- [ ] Sharing rules audited and documented
- [ ] API access logged and monitored
- [ ] Third-party apps reviewed and approved
- [ ] Field history tracking on sensitive data
- [ ] Regular backup and recovery testing
- [ ] Incident response plan documented

### Broader Enterprise Security:

- [ ] Endpoint Detection and Response (EDR) deployed
- [ ] Network segmentation implemented
- [ ] Privileged Access Management (PAM) in place
- [ ] Data Loss Prevention (DLP) configured
- [ ] Security awareness training completed
- [ ] Vendor risk assessments current
- [ ] Cyber insurance policy reviewed
- [ ] Board-level security reporting established

---

## Industry Impact Analysis

### Commercial Real Estate Sector:

The Cushman & Wakefield breach highlights specific risks for commercial real estate:

**High-Value Data at Risk:**
- Client financial information
- Property valuation data
- Lease terms and negotiations
- Portfolio strategies
- Tenant information

**Regulatory Implications:**
- GDPR compliance for EU clients
- State privacy laws (CCPA, etc.)
- SEC disclosure requirements (if publicly traded)
- Client contract breach notifications

### Cross-Industry Lessons:

1. **CRM Security Is Critical** — Your CRM is a treasure trove. Protect it accordingly.
2. **Guest User Misconfiguration Is Common** — Audit these permissions quarterly.
3. **Third-Party Risk Is Real** — Vendor vulnerabilities become your vulnerabilities.
4. **Incident Response Matters** — Cushman & Wakefield's quick disclosure may limit reputational damage.

---

## Alternative CRM Considerations

If your current CRM security posture concerns you, consider platforms with strong security track records:

**[AFFILIATE_LINK:HubSpot]** — Enterprise-grade CRM with advanced security features including SOC 2 Type II certification, GDPR compliance tools, and comprehensive audit logging. 30% recurring commission for 12 months.

> **FTC Disclosure:** *Some links in this article are affiliate links. We may earn a commission if you purchase through these links, at no extra cost to you.*

---

## Frequently Asked Questions
### Q: Is Salesforce inherently insecure?

**A:** No. Salesforce is highly secure when properly configured. Most breaches result from misconfigurations, weak permissions, or unpatched instances — not Salesforce platform vulnerabilities.

### Q: How do I know if my Salesforce instance is vulnerable?

**A:** Run Salesforce's free Security Health Check:
```
Setup → Security → Health Check
→ Review score and recommendations
→ Prioritize high-risk items
```

### Q: Should I disable guest users entirely?

**A:** If you don't need public-facing community pages or portals, yes. If you do need them, restrict permissions to the absolute minimum required functionality.

### Q: What's the cost of a CRM breach?

**A:** IBM's 2025 Cost of Data Breach Report estimates the average cost at $4.88 million. For enterprise CRMs containing commercial data, costs can exceed $10 million including regulatory fines, legal fees, and reputational damage.

### Q: How often should I audit CRM permissions?

**A:** Quarterly at minimum. Monthly for organizations in regulated industries. After any major configuration change or new integration.

---

## Internal Resources

- [INTERNAL_LINK:small business security fundamentals] — Security basics for smaller organizations
- [INTERNAL_LINK:complete small business cybersecurity guide] — Comprehensive security framework

---

*This guide is updated as new information becomes available. Last updated: May 5, 2026, 06:00 UTC.*

*© 2026 HERMES Security. This content is for educational purposes. For incident response assistance, contact qualified cybersecurity professionals.*
