import json
import os
from typing import List, Dict, Any
from extraction_engine import extract_inspection

# Exact status strings required by the specification
STATUS_COMPLIANT = "compliant:good"
STATUS_VIOLATION = "violation:critical"
STATUS_WARNING   = "warning:warning"

class Poller:
    def __init__(self, status_file: str = "statuses.json"):
        self.status_file = status_file
        self.records = self._load_statuses()
    
    def _load_statuses(self) -> List[Dict[str, Any]]:
        if os.path.exists(self.status_file):
            with open(self.status_file, 'r') as f:
                return json.load(f)
        return []
    
    def _save_statuses(self):
        with open(self.status_file, 'w') as f:
            json.dump(self.records, f, indent=2)
    
    def simulate_fetch_inspection_html(self, restaurant_address: str) -> str:
        """Mock browser: returns hard‑coded HTML for a few demo addresses."""
        if "123 Main St" in restaurant_address:
            return """
            <html>
                <body>
                    <h1>Golden Dragon</h1>
                    <p class="address">123 Main St, Metropolis, CA 90012</p>
                    Date: 2025-03-01
                    <p>Grade: C</p>
                    <ul>
                        <li>Critical: Food temperature abuse</li>
                        <li>Non-Critical: Floors not clean</li>
                    </ul>
                </body>
            </html>
            """
        elif "456 Oak Ave" in restaurant_address:
            return """
            <html>
                <body>
                    <h1>Pizza Planet</h1>
                    <p class="address">456 Oak Ave, Gotham, NY 10001</p>
                    Date: 2025-02-20
                    <p>Grade: B</p>
                    <ul>
                        <li>Non-Critical: Improper labeling</li>
                    </ul>
                </body>
            </html>
            """
        else:
            # Compliant scenario
            return """
            <html>
                <body>
                    <h1>Burger Joint</h1>
                    <p class="address">789 Pine Rd, Star City, IL 60601</p>
                    Date: 2025-03-10
                    <p>Grade: A</p>
                    <ul>
                        <li>Non-Critical: Wall paint chipped</li>
                    </ul>
                </body>
            </html>
            """
    
    def determine_status(self, report: Dict[str, Any]) -> str:
        if report.get("has_critical_violations"):
            return STATUS_VIOLATION
        grade = report.get("grade", "")
        if grade in ("B", "C"):
            return STATUS_WARNING
        return STATUS_COMPLIANT   # Grade A or missing, no critical violations
    
    def process_location(self, address: str) -> Dict[str, Any]:
        html = self.simulate_fetch_inspection_html(address)
        report = extract_inspection(html)
        status = self.determine_status(report)
        record = {
            "title": report["title"],
            "address": address,
            "inspection_date": report["inspection_date"],
            "grade": report["grade"],
            "critical_violations": report["has_critical_violations"],
            "status": status
        }
        # Upsert the record
        existing = next((r for r in self.records if r["address"] == address), None)
        if existing:
            existing.update(record)
        else:
            self.records.append(record)
        return record
    
    def run(self, addresses: List[str]):
        for addr in addresses:
            record = self.process_location(addr)
            print(f"Processed {record['title']} – Status: {record['status']}")
        self._save_statuses()
        print(f"Status records saved to {self.status_file}")
