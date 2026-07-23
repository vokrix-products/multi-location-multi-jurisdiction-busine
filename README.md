# Multi-Location Health Inspection Violation Auto-Monitor

## Product
Automated backend that extracts restaurant inspection results from HTML, determines compliance status, and persists records. Designed for food service operators managing 3–20 locations across multiple jurisdictions.

## Archetype
Restaurant / Food Service Operator Tier – tracks inspection violations and critical flags across a portfolio of locations, enabling proactive remediation before fines or closures.

## What the Poller Expects (Input)
- **Address list** – a collection of restaurant addresses as strings (e.g. `\"123 Main St, Metropolis, CA 90012\"`)
- **Inspection HTML** – per address, the poller calls `simulate_fetch_inspection_html(address)` which returns hard-coded HTML; in production this would be replaced with real web scraping or API integration
\`\`\`python
poller = Poller()
poller.run([\"123 Main St\", \"456 Oak Ave\"])
\`\`\`

## Statuses
| Condition | Status |
|-----------|--------|
| No critical violations, grade A (or none) | `compliant:good` |
| Any critical violation present | `violation:critical` |
| No critical violations, grade B or C | `warning:warning` |

## Files
- `extraction_engine.py` – parses restaurant name (title), address, date, grade, violations
- `poller.py` – fetches, extracts, determines status, persists to JSON
- `run_demo.py` – zero-argument demo with 3 hard-coded locations
- `run_tests.py` – unit tests for extraction and status logic
Dashboard: https://multi-location-multi-jurisdiction-busine.vokrix.co
Vercel Project: multi-location-multi-jurisdiction-busine
Railway Service: 893e7380-0faf-4d09-a57e-f7d7af6ecc0e

Billing: price_1TwKcg2c9uGCcgMSpk3yHHU0

Landing: https://vokrix.co/multi-location-multi-jurisdiction-busine

Outreach: active
