import time
import os
import sys
import requests

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_SERVICE_KEY = os.environ["SUPABASE_SERVICE_KEY"]
PRODUCT_ID = os.environ["PRODUCT_ID"]
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]

HEADERS = {
    "apikey": SUPABASE_SERVICE_KEY,
    "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
    "Content-Type": "application/json"
}

def poll():
    # poll for process_upload jobs with status=pending
    pass  # placeholder for actual processing logic

if __name__ == "__main__":
    while True:
        poll()
        time.sleep(60)
