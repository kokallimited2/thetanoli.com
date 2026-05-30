*FTC Disclosure: This article contains affiliate links. If you purchase through these links, we may earn a commission at no extra cost to you.*

# Cushman & Wakefield Breach: 500K Records Stolen by ShinyHunters — Enterprise Security Alert

## Introduction

Real estate giant **Cushman & Wakefield** has confirmed a data breach impacting approximately 500,000 Salesforce records, the latest in a wave of ShinyHunters cyberattacks in May 2026. The breach, which exploited a Salesforce guest user account with excessive privileges, exposed sensitive client data including lease agreements, property valuations, and executive communications.

Our team has analyzed the breach details, the exploit path, and what it means for enterprises running CRM platforms. This is the third ShinyHunters-linked breach this month alone — and it's the second originating from a Salesforce misconfiguration.

## Breach Summary

| Detail | Information |
|--------|-------------|
| **Target** | Cushman & Wakefield (global commercial real estate) |
| **Records** | ~500,000 |
| **Attackers** | ShinyHunters |
| **Entry Vector** | Salesforce guest user account with elevated privileges |
| **Timeline** | Detected May 24, 2026 |
| **Data Type** | Client contracts, lease info, property valuations, exec communications |
| **Status** | Contained — data already for sale on breach forums |

## The ShinyHunters Campaign — May 2026

ShinyHunters is running what appears to be a coordinated campaign against enterprise SaaS platforms in May 2026:

| Target | Records | Entry Vector | Date |
|--------|---------|-------------|------|
| Instructure/Canvas | 275M | Salesforce guest user misconfig | May 26 |
| Cushman & Wakefield | 500K | Salesforce guest user misconfig | May 24 |
| Medtronic | 9M | Third-party access compromise | May 22 |

The pattern is clear: **Salesforce guest user accounts** are being exploited. These accounts are designed for limited, unauthenticated access — but when misconfigured, they become a backdoor into the organization's most sensitive data.

## How the Attack Worked

### The Salesforce Guest User Vulnerability

Salesforce includes a "Guest User" profile for Experience Cloud sites — intended for unauthenticated visitors to view public-facing content. However, when organizations:

1. Create Experience Cloud sites with Guest User access
2. Grant read/write permissions to the Guest User profile
3. Link the Experience Cloud to standard Salesforce objects (Accounts, Opportunities, Contracts)

…the Guest User inherits permissions to read (and sometimes write) those objects. ShinyHunters appears to have automated the scanning of public Salesforce Experience Cloud sites, testing for misconfigured Guest User access.

### Why This Keeps Happening

The Salesforce Guest User vulnerability is not a zero-day — it's a configuration issue that's been documented since 2021. Yet it remains pervasive because:

- **Experience Cloud sites are created rapidly** with default permissions
- **Security reviews rarely include Guest User profiles** — they're considered "low risk"
- **Permissions propagate** when new objects connect to Experience Cloud sites
- **Many orgs don't realize Guest Users can read data** — they assume it's limited to public site pages

## What Data Was Exposed

The Cushman & Wakefield Salesforce instance contained:

- **Client contracts** — names, contact details, lease terms
- **Property valuations** — financial details for commercial properties
- **Executive communications** — internal notes, negotiation strategy documents
- **User account details** — employee names, roles, email addresses
- **Third-party partner data** — vendor contracts and contact info

For commercial real estate clients, this is a goldmine of competitive intelligence. Property valuations and lease terms can be used to undercut pricing. Executive communications reveal negotiation strategies.

## How to Secure Your Salesforce CRM

If your organization uses Salesforce with Experience Cloud (Community Cloud) sites, here's exactly what to check:

### Step 1: Audit Guest User Permissions

```salesforce
In Setup:
1. Go to Users → Profiles
2. Find "[Experience Cloud Site Name] Guest User"
3. Click "View Profile" and audit object-level permissions
4. Remove all read/write permissions that aren't strictly necessary
```

### Step 2: Restrict Guest User Access

- Limit Guest Users to **accessing Experience Cloud only** — use permission sets to restrict API access
- Set "Guest User Record Access" to **"Private"** so they can't see records they didn't create
- Review sharing rules that may grant Guest Users access to standard objects

### Step 3: Enable Enhanced Monitoring

- Enable Salesforce Login Forensics or a third-party monitoring tool
- Set up alerts for unusual query patterns from Guest User sessions
- Review Guest User login history weekly

### Step 4: Consider Alternative CRM Platforms

If your security team is concerned about Salesforce's complex permission model, platforms like [AFFILIATE_LINK:HubSpot] have simpler, more transparent permission structures that reduce misconfiguration risk. HubSpot's object-level permissions are role-based and don't have the Guest User escalation path that Salesforce does.

## Enterprise Protection Checklist

Beyond CRM-specific fixes, every enterprise should implement:

| Control | Priority | Timeline |
|---------|----------|----------|
| Guest/Anonymous user audit | Critical | This week |
| API key rotation | Critical | This week |
| Third-party integration review | High | 30 days |
| Session monitoring for unusual patterns | High | 30 days |
| Zero-trust architecture review | Medium | 90 days |

## Industry Impact Analysis

The Cushman & Wakefield breach has several ripple effects:

**For commercial real estate:** Expect clients to demand security audits from their brokers. Property owners may reconsider sharing sensitive financial data without encryption guarantees.

**For Salesforce customers:** This is the wake-up call for every organization running Experience Cloud. The pattern is now public — expect scanning bots to target every public Salesforce site.

**For the cybersecurity insurance market:** Two Salesforce-originated breaches in one month will trigger premium adjustments for any organization running Salesforce Experience Cloud sites.

**For competitors:** The exposed data gives rivals insight into Cushman & Wakefield's pricing, client relationships, and strategic direction. Lawsuits may follow.

## Frequently Asked Questions

### Q: Is my Salesforce data at risk if I don't use Experience Cloud?

**A:** No. The Guest User vulnerability only applies to organizations running Experience Cloud (Community Cloud) sites. Standard Salesforce instances without public-facing sites are not affected by this specific attack vector.

### Q: Should I disable Guest User access?

**A:** If you don't actively need anonymous access to your Experience Cloud site, disable it. If you do need it, restrict permissions to the absolute minimum — ideally read-only access to a single, dedicated object.

### Q: How did ShinyHunters find these Salesforce Guest User accounts?

**A:** They likely used Shodan or custom scanning to identify public-facing Salesforce Experience Cloud URLs, then tested which ones had misconfigured Guest User permissions. The Guest User profile is publicly documented.

### Q: Is HubSpot immune to similar attacks?

**A:** HubSpot's permission model doesn't have an equivalent "Guest User" escalation path. However, no platform is immune to misconfiguration — HubSpot users should audit API key permissions and third-party app access.

### Q: What should I tell my clients if their data was in this breach?

**A:** Be transparent: confirm what data was exposed (based on your investigation), provide credit monitoring if PII was involved, and share the steps you're taking to prevent recurrence.

## The Bottom Line

The Cushman & Wakefield breach is part of a larger pattern: ShinyHunters has identified Salesforce Experience Cloud misconfiguration as a reliable entry vector, and they're running it at scale. Every organization using Salesforce needs to audit their Guest User permissions today.

For enterprises looking to simplify their CRM security posture, [AFFILIATE_LINK:HubSpot] provides a more secure permission framework out of the box. For those staying on Salesforce, the checklist above is your minimum starting point.

---

### JSON-LD Schema

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "Cushman & Wakefield Breach: 500K Records Stolen by ShinyHunters — Enterprise Security Alert",
  "description": "Complete analysis of the Cushman & Wakefield Salesforce data breach by ShinyHunters. How the attack worked and how to secure your CRM.",
  "datePublished": "2026-05-28",
  "author": {"@type": "Organization", "name": "HERMES Security Research"}
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Is my Salesforce data at risk if I don't use Experience Cloud?", "acceptedAnswer": {"@type": "Answer", "text": "No. The Guest User vulnerability only applies to organizations running Experience Cloud sites with public-facing access."}},
    {"@type": "Question", "name": "Should I disable Guest User access?", "acceptedAnswer": {"@type": "Answer", "text": "If you don't need anonymous access to your Experience Cloud site, disable it. If you do, restrict permissions to the minimum."}},
    {"@type": "Question", "name": "Is HubSpot immune to similar attacks?", "acceptedAnswer": {"@type": "Answer", "text": "HubSpot's permission model doesn't have an equivalent Guest User escalation path, though no platform is immune to all misconfiguration risks."}}
  ]
}
```
