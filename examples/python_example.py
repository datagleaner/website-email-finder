"""Find emails on company websites with the Data Gleaner Actor.

pip install apify-client
APIFY_TOKEN=... python python_example.py stripe.com basecamp.com
"""
import os
import sys

from apify_client import ApifyClient

sites = sys.argv[1:] or ["stripe.com", "basecamp.com", "https://www.appier.com"]
client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("datagleaner/website-contact-details-scraper").call(
    run_input={"websites": sites, "maxPagesPerSite": 5}
)
for item in client.dataset(run.default_dataset_id).iterate_items():
    emails = [e["value"] for e in item.get("emails", [])]
    print(item["website"], item["status"], "best:", item.get("bestEmail"), "all:", emails)
