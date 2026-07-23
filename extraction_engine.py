import re
from typing import Dict, Any

def extract_inspection(html: str) -> Dict[str, Any]:
    """
    Parse inspection HTML and return structured data.
    The 'title' field is the restaurant name – the primary entity tracked by the operator.
    """
    # Title = restaurant name
    name_match = re.search(r'<h1>(.*?)</h1>', html)
    title = name_match.group(1).strip() if name_match else "Unknown"
    
    # Address
    addr_match = re.search(r'<p class="address">(.*?)</p>', html)
    address = addr_match.group(1).strip() if addr_match else ""
    
    # Inspection date
    date_match = re.search(r'Date:\s*(\d{4}-\d{2}-\d{2})', html)
    inspection_date = date_match.group(1) if date_match else ""
    
    # Grade
    grade_match = re.search(r'Grade:\s*([A-C])', html)
    grade = grade_match.group(1) if grade_match else ""
    
    # Violations
    violations = []
    has_critical = False
    viol_pattern = re.findall(r'<li>(Critical|Non-Critical):\s*(.*?)</li>', html)
    for severity, desc in viol_pattern:
        is_crit = (severity == "Critical")
        violations.append({"description": desc.strip(), "critical": is_crit})
        if is_crit:
            has_critical = True
    
    return {
        "title": title,
        "address": address,
        "inspection_date": inspection_date,
        "grade": grade,
        "violations": violations,
        "has_critical_violations": has_critical
    }
