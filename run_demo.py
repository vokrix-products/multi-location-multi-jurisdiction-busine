import sys
from poller import Poller

def main():
    # Hard‑coded addresses – no input needed, runs under 10 seconds
    locations = [
        "123 Main St, Metropolis, CA 90012",
        "456 Oak Ave, Gotham, NY 10001",
        "789 Pine Rd, Star City, IL 60601"
    ]
    
    poller = Poller(status_file="demo_statuses.json")
    poller.run(locations)
    print("Demo completed successfully.")
    sys.exit(0)

if __name__ == "__main__":
    main()
