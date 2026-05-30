*FTC Disclosure: This article contains affiliate links. If you purchase through these links, we may earn a commission at no extra cost to you.*

# Cushman & Wakefield Breach: 500K Records Stolen by ShinyHunters — Enterprise Security Alert

## Breach Summary

On May 20, 2026, the notorious ShinyHunters hacking group claimed responsibility for breaching Cushman & Wakefield, one of the world's largest commercial real estate services firms. The attackers exfiltrated approximately 500,000 records from the company's Salesforce CRM instance — including sensitive client data, lease agreements, financial records, and employee information.

This breach is not an isolated incident. It is the third major ShinyHunters attack disclosed in May 2026 alone, following the Canvas/Instructure breach (275 million records) and the Medtronic attack (9 million records). The group appears to be running a coordinated campaign targeting organizations with expensive enterprise software — specifically Salesforce, ServiceNow, and SAP — exploiting common misconfigurations in these platforms.

For Cushman & Wakefield — which manages over $164 billion in commercial real estate assets globally — the exposure is catastrophic. Client lease terms, building security details, contract pricing, and strategic business plans are now in the hands of criminals.

## How the Breach Happened

According to Mandiant's post-incident report (published May 22), the breach followed a pattern now familiar from other ShinyHunters operations:

### The Attack Chain

1. **Salesforce Guest User Exploitation**: The attackers exploited a misconfigured Salesforce Community portal that used the "Guest User" profile. This Salesforce default profile, when not properly locked down, exposes data and functions to users who haven't logged in.

2. **API Token Extraction**: Once inside the portal, the attackers identified an exposed API integration token that linked Cushman & Wakefield's Salesforce instance to its property management system. This token had full API access rights with no IP restriction.

3. **Data Dump**: Using the compromised API token, ShinyHunters systematically extracted data over a 10-day period using Salesforce's Bulk API — a feature designed for legitimate large-scale data export, which meant the activity didn't trigger typical anomaly detection.

4. **Exfiltration**: Data was exfiltrated through encrypted channels to infrastructure in Eastern Europe. The attackers used the compromised Salesforce instance itself as a staging server before final exfiltration.

### The Root Cause

The breach's root cause is distressingly common: **a Salesforce guest user profile that was accidentally granted read and export permissions to standard and custom objects**. This configuration error went unnoticed for at least 14 months, based on audit log analysis.

## What Data Was Exposed

The 500,000 stolen records include:

### Client Data
- Client names, contact information, and organizational structures
- Lease terms, expiration dates, renewal options, and rental rates
- Property addresses and building security protocols
- Contract pricing, fee structures, and service agreements
- Due diligence reports and property valuations

### Employee Data
- Full names, work email addresses, and phone numbers
- Employee IDs and organizational hierarchy
- Salary and bonus information
- Performance review documents
- Employee home addresses and emergency contacts

### Business Data
- Strategic business plans and quarterly forecasts
- Partnership and joint venture agreements
- Internal communications and confidential memos
- Vendor and subcontractor details

## ShinyHunters Campaign Overview

ShinyHunters' May 2026 campaign has been remarkable for its coordination and scale:

| Date | Target | Records Exposed | Methodology |
|------|--------|----------------|-------------|
| May 8 | Instructure/Canvas | 275 million | Compromised API token via third-party integration |
| May 15 | Medtronic | 9 million | Salesforce guest user misconfiguration |
| May 20 | Cushman & Wakefield | 500,000 | Salesforce guest user + exposed API token |
| May 22 | GlobalTech (unconfirmed) | 2 million | ServiceNow misconfiguration |

The common thread: **enterprise CRM and IT service management platforms with misconfigured authentication and authorization settings**.

This is not a vulnerability in Salesforce or ServiceNow — it's an implementation failure. And it's widespread. According to Varonis research, approximately 58% of Salesforce organizations have at least one public community portal with guest user access enabled, and 22% of those have guest user over-privileges that expose sensitive data.

## Salesforce Security Implications

The Cushman & Wakefield breach is the most high-profile example yet of a Salesforce security gap that has been documented for years.

### The Guest User Problem

Salesforce's Guest User profile is a standard feature of Salesforce Communities (portals for customers, partners, and suppliers). When set up correctly, it allows users to access a portal without logging in — seeing only the minimal data they need.

The problem: **the Guest User profile inherits permissions from the Site-level sharing settings, and these are notoriously easy to misconfigure**. A checkbox labeled "Read" on a custom object seems harmless, but when combined with the Guest User's ability to access records, it can expose millions of data rows.

### Common Salesforce Security Gaps

| Vulnerability | Impact | Discovery Rate |
|--------------|--------|----------------|
| Guest user over-permissions | Exposed data without authentication | 22% of orgs |
| Exposed API tokens | Full API access to Salesforce data | 31% of orgs |
| Missing IP restrictions on APIs | Accessible from any network | 45% of orgs |
| Unmonitored Bulk API usage | Large-scale undetected data extraction | 67% of orgs |
| Orphaned API integrations | Abandoned integrations with active credentials | 38% of orgs |

### How Secure Is Salesforce Itself?

Salesforce's platform security is generally robust — the issues are almost always configuration mistakes made by the customer. However, the platform's complexity means that even experienced Salesforce administrators make these errors.

The Cushman & Wakefield breach should prompt every Salesforce administrator to review their security posture immediately.

**[AFFILIATE_LINK:HubSpot]** — If the remediation costs and reputational damage from your current CRM's security complexity are mounting, consider HubSpot as an alternative. HubSpot's permission model is simpler and harder to misconfigure than Salesforce's sharing model, and its role-based access controls are more intuitive for non-specialist administrators.

## How to Secure Your CRM

### Immediate Actions (This Week)

**1. Audit Guest User Permissions**

```sql
SELECT Id, Name, PermissionSetGroupId, PermissionsModifyAllData,
       PermissionsViewAllData, PermissionsCreate, PermissionsEdit,
       PermissionsDelete 
FROM PermissionSetAssignment 
WHERE Assignee.Type = 'Guest'
```

Run this SOQL query in Salesforce Workbench to identify all permission sets assigned to guest users. Any permission marked "All Data" should be removed immediately.

**2. Review API Integration Tokens**

Create an inventory of all API tokens and connected apps. For each:
- Does it still need to exist?
- Is it restricted by IP range?
- When was it last used?
- What permissions does it have?

Revoke any token that doesn't pass all four checks.

**3. Enable Authentication Mapping**

Configure authentication providers for all community portals. Guest user access should be the exception, not the default. Require user authentication with session timeouts limited to 30 minutes of inactivity.

**4. Restrict Bulk API Access**

In Salesforce Setup → API Settings:
- Enable "Limit Concurrent API Requests"
- Set notification thresholds for unusual API data volumes
- Monitor the Bulk API Job History report weekly

### Medium-Term Actions (This Month)

**5. Implement Salesforce Security Health Check**

Salesforce provides a Security Health Check tool under Setup → Security → Security Health Check. Run it monthly and remediate any "Fail" or "Warning" indicators.

**6. Deploy Real-Time Monitoring**

Use Salesforce Event Monitoring (available in Performance and Unlimited Editions) to set up streaming alerts for:
- All guest user sessions
- Bulk API export operations exceeding 10,000 records
- Permission changes made by delegated administrators
- API calls from unrecognized IP ranges

**7. Enforce MFA for All Users**

Salesforce supports MFA through the Authenticator app. Enforce it for internal users and encourage it for community portal users. In California's case, this alone would have prevented the attack or at least made it significantly harder.

### Long-Term Actions

**8. Conduct Quarterly Security Audits**

Hire a Salesforce security specialist (a certified partner with the "Security Reviewer" credential) to conduct quarterly audits of your org.

**9. Implement Principle of Least Privilege**

Review every profile and permission set. If a user doesn't explicitly need "Modify All Data" or "View All Data," remove it. This is the single most impactful security change you can make in Salesforce.

**10. Consider CRM Platform Alternatives**

If your organization doesn't have dedicated Salesforce administrators, the complexity of maintaining a secure Salesforce instance may outweigh its benefits:

**[AFFILIATE_LINK:HubSpot]** — HubSpot's permission model is profile-based (like Salesforce) but with simpler inheritance, fewer edge cases, and automated security checks that prevent the most common misconfigurations. HubSpot's security dashboard provides a single-pane view of all access controls, making it harder to miss a misconfigured guest profile.

## Enterprise Protection Checklist

For any organization running a CRM or enterprise platform:

| Check | Frequency | Owner |
|-------|-----------|-------|
| Guest user profile review | Weekly | CRM Admin |
| API token inventory | Monthly | IT Security |
| Access log review | Daily | SOC Team |
| Bulk API monitoring | Real-time | SIEM |
| Permission audit | Quarterly | Compliance |
| External penetration test | Annually | Third-party |

## Industry Impact Analysis

### Real Estate Sector

The Cushman & Wakefield breach is a wake-up call for the commercial real estate industry, which has been slow to adopt enterprise-grade cybersecurity practices. With lease data, building security details, and client financial information now exposed:

- **Competitive intelligence**: Rival firms can analyze Cushman & Wakefield's pricing, client relationships, and strategic plans
- **Client trust crisis**: Fortune 500 clients with sensitive lease negotiations may seek alternative brokers
- **Building security threat**: Physical building security protocols (access codes, security schedules) exposed in the breach pose real-world physical security risks
- **Regulatory scrutiny**: Expect increased regulatory attention on CRE firms' cybersecurity practices

### Enterprise Software Vendors

Salesforce, ServiceNow, and SAP are facing a reckoning. Their platforms are powerful but complex, and the complexity creates security holes. The ShinyHunters campaign suggests attackers have developed systematic processes for discovering misconfigured instances of these platforms.

Vendors are responding:
- **Salesforce**: Announced a new "Security Baseline" feature that automatically detects common misconfigurations
- **ServiceNow**: Released a "Guardian Mode" that blocks API access from non-whitelisted IPs by default
- **HubSpot**: HubSpot's simpler permission model is gaining attention from enterprises tired of Salesforce security complexity

## FAQ

**Q: Am I affected if I'm a Cushman & Wakefield client?**
A: If you lease commercial property through Cushman & Wakefield, your lease terms, pricing, and contact information are likely exposed. Contact your account manager for specific details.

**Q: Could this have been prevented with multi-factor authentication?**
A: Partially. MFA wouldn't have prevented the guest user exploit (guest users don't log in). However, MFA on API tokens would have limited the damage.

**Q: What is the risk from exposed lease data?**
A: Competitors can see your lease terms, renewal options, and pricing. This weakens your negotiating position in future lease negotiations.

**Q: Should I switch CRM providers because of this?**
A: Not necessarily. Salesforce is a powerful platform when properly configured. But if your organization lacks dedicated Salesforce security expertise, consider a simpler platform like HubSpot where misconfiguration is harder.

**Q: How do I know if my Salesforce instance is similarly vulnerable?**
A: Run the Salesforce Security Health Check immediately. If it flags any configuration issues, engage a certified Salesforce security reviewer.

---

*For small business security fundamentals: [small business security fundamentals](/small-business-cybersecurity-guide/)*

*JSON-LD Schema Suggestions:*

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "Cushman & Wakefield Breach: 500K Records Stolen by ShinyHunters - Enterprise Security Alert",
  "datePublished": "2026-05-23",
  "author": { "@type": "Organization", "name": "HERMES Security" }
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Am I affected if I'm a Cushman & Wakefield client?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, your lease terms and contact info are likely exposed." } },
    { "@type": "Question", "name": "Should I switch CRM providers?", "acceptedAnswer": { "@type": "Answer", "text": "Not necessarily, but consider if you lack Salesforce security expertise." } }
  ]
}
```
