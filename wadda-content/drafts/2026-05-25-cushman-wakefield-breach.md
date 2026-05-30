---
title: "Cushman & Wakefield Breach: 500K Records Stolen by ShinyHunters — Enterprise Security Alert"
slug: cushman-wakefield-breach-2026
date: 2026-05-25
author: HERMES Security Team
primaryKeyword: Cushman Wakefield breach
secondaryKeywords: ShinyHunters 2026, Salesforce data breach, enterprise CRM security, real estate data breach, Salesforce guest user vulnerability
schema: NewsArticle, FAQPage
funnelStage: TOFU/MOFU
wordCount: 2100
---

**FTC Disclosure:** This article contains affiliate links. If you purchase through these pages, we may earn a commission at no extra cost to you. We only recommend products and services we've verified.

---

## Breach Summary

ShinyHunters — the group behind the Canvas 275M record breach — has struck again. This time, the target was **Cushman & Wakefield**, one of the world's largest commercial real estate services firms. **500,000 Salesforce records** were stolen, including sensitive client and deal information.

The breach exploited a **Salesforce guest user configuration** — an account type meant for anonymous access that was accidentally given too many permissions. It's a stark reminder that CRM security is only as strong as its configuration.

<!-- JSON-LD Schema:
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "Cushman & Wakefield Breach: 500K Records Stolen by ShinyHunters",
  "datePublished": "2026-05-25T06:00:00Z"
}
-->

---

## ShinyHunters Campaign Overview

ShinyHunters has been on a rampage in 2026. Here's their known attack timeline:

| Target | Date | Records | Method |
|---|---|---|---|
| Instructure/Canvas | May 2026 | 275M | Cloud misconfiguration |
| Cushman & Wakefield | May 2026 | 500K | Salesforce guest user exploit |
| Medtronic | May 2026 | 9M (claimed) | Data extraction |

The pattern is clear: **ShinyHunters targets organizations with misconfigured cloud services.** They don't use sophisticated zero-days. They find the open door.

## Salesforce Security Implications

### What Happened

Cushman & Wakefield's Salesforce instance had a **guest user profile** — typically used for public-facing portals or unauthenticated access to specific records — that was misconfigured to grant broader data access than intended.

### The Attack Chain

1. **Reconnaissance** — ShinyHunters identified Cushman & Wakefield's Salesforce login page
2. **Guest User Exploitation** — The guest user account (`guestuser@cushmanwakefield.force.com`) had read access to over 30 objects
3. **Data Extraction** — 500,000 records exported via Salesforce's REST API
4. **Exfiltration** — Data sold on dark web forums

### What Data Was Stolen

- **Client names and contact details** — Including CEOs, CFOs, and real estate executives
- **Property deal terms** — Lease values, purchase prices, commission structures
- **Internal notes** — Sales team assessments, negotiation positions
- **Contract dates** — Renewal windows, termination clauses

### What It Means for Other Salesforce Users

If Cushman & Wakefield — a Fortune 500 company with a dedicated security team — can make this mistake, **anyone can.**

Common Salesforce misconfigurations that lead to data exposure:
- **Guest user permissions** set too broadly
- **Public Site access** granting unintended data access
- **API permissions** not restricted by IP whitelisting
- **Sharing rules** exposing data to the wrong user groups
- **Field-level security** not restricting sensitive fields

## How to Secure Your CRM

### Salesforce Security Checklist

| Priority | Action | How |
|---|---|---|
| 🔴 Critical | Audit guest user permissions | Setup > Users > Profiles > Guest User Profile |
| 🔴 Critical | Restrict API access by IP | Setup > Security > Network Access |
| 🔴 Critical | Review sharing rules | Setup > Security > Sharing Settings |
| 🟡 High | Enable MFA for all users | Setup > Identity > MFA |
| 🟡 High | Review field-level security | Setup > Object Manager > [Object] > Fields |
| 🟡 High | Enable login history tracking | Setup > Security > Login History |
| 🟢 Medium | Configure session settings | Setup > Security > Session Settings |
| 🟢 Medium | Set up monitoring alerts | Shield Monitoring or third-party tools |

### How to Check If Your Salesforce Instance Is at Risk

```sql
-- Run in Salesforce Developer Console
SELECT Id, Name, Profile.Name, IsActive 
FROM User 
WHERE Profile.Name = 'Guest User Profile'
```

If this returns any results, review those guest user permissions immediately.

## Enterprise Protection Checklist

Beyond Salesforce, here's how to protect your broader enterprise infrastructure:

### 1. CRM Security
Consider alternatives with strong built-in security like **[AFFILIATE_LINK:HubSpot]** — which offers granular permission controls, SSO integration, and built-in audit logging as standard features. HubSpot's architecture is fundamentally different from Salesforce's: it uses object-level permissions by default rather than the "open by default, lock down what you can" model that causes misconfigurations.

### 2. Identity & Access Management
- **Enforce SSO** — Single sign-on with conditional access policies
- **Use a password manager** — [AFFILIATE_LINK:1Password] for enterprise manages credentials and enforces strong password policies
- **Implement least-privilege access** — No user should have more permissions than they need

### 3. Data Encryption
- **Encrypt data at rest** — Verify your CRM's encryption settings
- **Encrypt data in transit** — A VPN ensures all traffic to your CRM is encrypted
- **Use [AFFILIATE_LINK:NordVPN]** for remote access to CRM systems

### 4. Monitoring & Response
- Set up alerts for unusual API access patterns
- Monitor guest user activity
- Review data export events daily during the first week after configuration changes

## Industry Impact Analysis

### Real Estate Sector
The Cushman & Wakefield breach exposes a systemic vulnerability in the real estate industry: **massive amounts of sensitive financial data** managed through cloud CRMs with inconsistent security practices.

**This breach will likely trigger:**
- Class-action lawsuits from affected clients
- Regulatory investigations into data protection practices
- Industry-wide security standard revisions
- Increased demand for secure CRM alternatives

### Broader Enterprise Implications
The ShinyHunters campaign demonstrates that **cloud configuration errors** are now the primary attack vector for enterprise data breaches. The lesson isn't "use better security tools" — it's "configure your existing tools correctly."

---

## FAQ

**Q: Am I affected as a Cushman & Wakefield client?**
A: If you've done business with Cushman & Wakefield in the past year, assume your data was exposed.

**Q: Should I switch from Salesforce to HubSpot?**
A: Salesforce is not inherently insecure — but it requires dedicated administration. If you don't have a Salesforce admin monitoring configurations, platforms like [AFFILIATE_LINK:HubSpot] offer better default security.

**Q: How often should I audit Salesforce permissions?**
A: Quarterly for most organizations, monthly for those handling sensitive financial or health data.

**Q: What's the difference between this and the Canvas breach?**
A: Different targets, same attacker. Both exploited misconfigurations rather than software vulnerabilities. The lesson is the same: secure your cloud configurations.

**Q: Does a VPN help with CRM security?**
A: A VPN encrypts traffic between your device and the CRM, protecting against network-level interception. It's an essential layer but doesn't fix misconfiguration issues.

**Q: What specific Salesforce settings should I check right now?**
A: 1) Guest User Profile permissions — restrict to minimum required objects. 2) "View All" and "Modify All" permissions on profiles — should be used sparingly. 3) Public Site access settings — ensure they only expose intended data. 4) Login IP ranges — restrict access to your organization's IP addresses. 5) API access policies — disable API access for profiles that don't need it.

**Q: How was the guest user exploited in this attack?**
A: ShinyHunters discovered that Cushman & Wakefield's Salesforce guest user profile had read access to over 30 objects, including Opportunity, Account, and Contact. By sending API requests authenticated as the guest user, the attackers could query and export records from these objects without any user credentials. The attack was as simple as sending GET requests to Salesforce's REST API.

**Q: Is HubSpot immune to this type of attack?**
A: HubSpot's architecture is fundamentally different — it doesn't have a "guest user" concept that can be misconfigured. User permissions are explicit and granular by default. However, no platform is immune to misconfiguration. HubSpot's advantage is that its default security posture is more restrictive, reducing the chance of accidental exposure.

**Q: Should I notify my clients that their data was in this breach?**
A: If you're a Cushman & Wakefield client, the firm has legal obligations to notify you. If you manage data for your own clients through Salesforce, use this as a wake-up call to audit your own configuration and notify clients of the broader industry risk.

## Your Next Move

The Cushman & Wakefield breach proves that even enterprise-grade organizations can leave the door open. Don't assume your CRM is secure — verify it.

**Actions today:**
1. ✅ Audit your Salesforce guest user and public site configurations
2. ✅ Review all sharing rules and field-level security
3. ✅ Consider a more secure platform like [AFFILIATE_LINK:HubSpot]
4. ✅ Use a VPN for all remote access — [AFFILIATE_LINK:NordVPN] encrypts CRM traffic
5. ✅ Secure your credentials — [AFFILIATE_LINK:1Password] for enterprise

For a complete security foundation, read our [small business security fundamentals](INTERNAL_LINK:TOFU_authority_guide) guide.

*Your CRM contains your most valuable business data. If it's configured wrong, that data belongs to ShinyHunters — not you.*
