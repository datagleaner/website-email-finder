#!/usr/bin/env bash
# One synchronous call: runs the Actor and returns the dataset rows as JSON.
# APIFY_TOKEN=... ./curl_example.sh
set -euo pipefail
curl -s -X POST \
  "https://api.apify.com/v2/acts/datagleaner~website-contact-details-scraper/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H 'Content-Type: application/json' \
  -d '{"websites": ["stripe.com", "basecamp.com", "https://www.appier.com"], "maxPagesPerSite": 5}'
