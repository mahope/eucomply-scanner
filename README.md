# EUComply Scanner

> **Universal website compliance scanner** — GDPR, DSA, ePrivacy, cookie consent, security headers, and resilience checks. Platform-independent: works on **any URL, any CMS**.

```bash
npx github:mahope/eucomply-scanner https://example.com
```

## Why this exists

Most compliance scanners are tied to WordPress or require installing a plugin on your server. EUComply Scanner works from the **outside** — it fetches your page as a visitor would and analyzes the HTML + HTTP headers. No installation, no server access, no CMS dependency.

**Use it for:**
- Quick compliance health checks on any website
- Pre-acquisition due diligence
- Monitoring competitor compliance
- CI/CD pipeline compliance gates
- GDPR/DSA/ePrivacy audit preparation

> **Professional monitoring?** Get automated weekly re-scans, PDF auditor-ready reports, DPA documents, and multi-page site audits for $79/year.
> [EUComply Pro →](https://auditedwp.pages.dev/pro/)

## Quick start

### Via npx (no install)

```bash
npx github:mahope/eucomply-scanner https://example.com
```

### Install globally

An npm registry release is planned (pending publish access). Until then, the
`npx github:mahope/eucomply-scanner <url>` command above always runs the latest version.


### As a library

```js
import { runScan } from 'eucomply-scanner';

const report = await runScan('https://example.com');
console.log(`Score: ${report.score.pct}%`);
console.log(`Platform: ${report.platform}`);
```

## What it checks

| Check | Description | Why it matters |
|-------|-------------|----------------|
| **Consent Mode v2** | Google Consent Mode v2 implementation | Required since March 2024 for EEA ad personalization |
| **IAB TCF** | Transparency & Consent Framework | Required for programmatic ads in the EEA |
| **Trackers** | Third-party trackers vs consent signals | GDPR Art. 6 — consent before non-essential tracking |
| **SSL/HSTS** | HTTPS + Strict-Transport-Security | Security baseline; HSTS prevents downgrade attacks |
| **Cookies** | Cookie consent platform detection | ePrivacy Directive — consent for non-essential cookies |
| **Forms** | Form markup + privacy policy link | GDPR Art. 13 — privacy notice at point of data collection |
| **Legal** | Privacy policy, imprint, terms, etc. links | GDPR, DSA, EAA — required legal pages |
| **Security headers** | CSP, X-Content-Type-Options, Referrer-Policy | OWASP security best practices |
| **DORA** | Resilience signals (email auth, failover) | DORA Art. 5-7 for financial entities |
| **Platform** | CMS/platform fingerprint (informational) | Know what you're dealing with |

## CLI usage

```bash
# Basic scan (human-readable output)
eucomply-scanner https://example.com

# JSON output for scripting
eucomply-scanner --json https://example.com

# Custom timeout (default: 12s)
eucomply-scanner --timeout 20000 https://slow-site.com
```

### Example output

```
🔍 EUComply Scan Report
   URL:      https://example.com
   Platform: WordPress
   Duration: 843ms
   Score:    5/8 (62%)

 ✅ Google Consent Mode v2 detected
 ✅ IAB TCF detected
 ✅ HTTPS + HSTS OK
 ⚠️ Cookie consent banner found: Cookiebot
    Cookiebot detected — ensure it blocks trackers before consent.
 ❌ Security headers: 2 missing
    Missing: Content-Security-Policy; X-Content-Type-Options
    💡 Add security headers. See https://securityheaders.com for guidance.
```

## API

### `runScan(url, options?)`

Scans a public URL and returns a compliance report.

**Parameters:**
- `url` (string, required) — The URL to scan. Scheme defaults to `https://` if omitted.
- `options.timeout` (number, optional) — Request timeout in ms. Default: `12000`.

**Returns:** A promise resolving to a report object with:
- `url` — The final URL (after redirects)
- `scannedAt` — ISO timestamp
- `durationMs` — Scan duration in milliseconds
- `platform` — Detected CMS/platform (or "Unknown")
- `checks` — Object with individual check results (each: `{ pass, warn, label, detail, fix? }`)
- `score` — `{ passed, total, pct }` summary
- `disclaimer` — Legal disclaimer

### `normalizeUrl(raw)`

Validates and normalizes a URL string. Returns `null` for private/internal/local addresses.

## REST API (free)

A public REST API is available at:

```
GET https://eucomply-scan.mahope-eeb.workers.dev/scan?url=https://example.com
GET https://eucomply-scan.mahope-eeb.workers.dev/stats
```

CORS-enabled for browser use. Rate-limited to 10 requests/minute/IP.

## Pro version

Need more? The Pro version adds:
- **PDF reports** — downloadable compliance reports
- **Continuous monitoring** — weekly automated rescans
- **Multi-page scans** — scan entire sites, not just one URL
- **Priority support** — compliance expert assistance

**[EUComply Pro — $79/year](https://auditedwp.pages.dev/pro/)**

## License

MIT — use it freely in your projects, CI/CD pipelines, and tools.