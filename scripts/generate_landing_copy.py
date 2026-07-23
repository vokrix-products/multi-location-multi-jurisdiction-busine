#!/usr/bin/env python3
"""Generate landing page copy using Claude API."""

CTA_TEXT = "Protect Your Locations"

with open("product-marketing.md") as fm:
    product_name = fm.readline().strip().lstrip("#").strip()
USER_MESSAGE = f"""\
Write conversion-focused landing page copy for {product_name}.\
Include a compelling headline, key benefits, and a strong call-to-action.\
The tone should be authoritative yet accessible.\
"""

def main():
    print(f"Generating landing copy with CTA: {CTA_TEXT}")
    print(f"Message: {USER_MESSAGE.strip()}")

if __name__ == "__main__":
    main()
