"""domains.csv -> contacts.csv with the best email, deliverability, phones and socials.

pip install apify-client
APIFY_TOKEN=... python csv_to_contacts.py [domains.csv] [contacts.csv]

The input needs a column named "domain" (or "website"). Only sites where an email is
found are billed by the Actor; the rest come back as free rows with a status.
"""
import csv
import os
import sys

from apify_client import ApifyClient

src = sys.argv[1] if len(sys.argv) > 1 else "domains.csv"
dst = sys.argv[2] if len(sys.argv) > 2 else "contacts.csv"

with open(src, newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
sites = [(r.get("domain") or r.get("website") or "").strip() for r in rows]
sites = [s for s in sites if s]

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/website-contact-details-scraper").call(
    run_input={"websites": sites, "maxPagesPerSite": 8}
)

SOCIALS = ["linkedin", "twitter", "facebook", "instagram", "youtube"]
fields = ["website", "status", "companyName", "bestEmail", "deliverable", "allEmails", "phones"] + SOCIALS
with open(dst, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for item in client.dataset(run.default_dataset_id).iterate_items():
        row = {
            "website": item["website"],
            "status": item["status"],
            "companyName": item.get("companyName") or "",
            "bestEmail": item.get("bestEmail") or "",
            "deliverable": item.get("bestEmailDeliverable"),
            "allEmails": "; ".join(item.get("emailList") or []),
            "phones": "; ".join(item.get("phoneList") or []),
        }
        for s in SOCIALS:
            row[s] = "; ".join(item.get(s) or [])
        w.writerow(row)
print(f"wrote {dst} ({len(sites)} sites)")
