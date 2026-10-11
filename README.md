# website-email-finder

Find the contact emails, phone numbers and social profiles of a list of company websites, from Python, Node.js, curl or a CSV file. Give it domains, get back the best email to contact first (company inbox, sales, or a named person ahead of support, press or HR), whether its domain can receive mail, E.164 phones, social links and contact forms.

> Disclosure: these examples call the [Data Gleaner](https://datagleaner.github.io) Actor [`website-contact-details-scraper`](https://apify.com/datagleaner/website-contact-details-scraper) on Apify, which we publish. It is pay per result: US$0.002 per site where an email is found; sites without an email are free. Apify's free-tier credit covers small runs. You need an Apify API token (`APIFY_TOKEN`).

Actor page: https://apify.com/datagleaner/website-contact-details-scraper
More Data Gleaner scrapers: https://datagleaner.github.io

## Setup

Get a token from Apify (Settings > API & Integrations) and export it:

```bash
export APIFY_TOKEN=your_token
```

## Examples

| File | What it does |
| --- | --- |
| `examples/python_example.py` | Python with `apify-client` (`pip install apify-client`) |
| `examples/node_example.mjs` | Node.js with `apify-client` (`npm install apify-client`) |
| `examples/curl_example.sh` | One `run-sync-get-dataset-items` HTTP call, JSON out |
| `examples/csv_to_contacts.py` | `domains.csv` in, `contacts.csv` out |

```bash
python examples/python_example.py stripe.com basecamp.com
node examples/node_example.mjs stripe.com basecamp.com
./examples/curl_example.sh
python examples/csv_to_contacts.py examples/domains.csv contacts.csv
```

Output columns of the CSV script: `website, status, companyName, bestEmail, deliverable, allEmails, phones, linkedin, twitter, facebook, instagram, youtube`.

## Useful input and output fields

Input: `websites` (domains or URLs), `maxPagesPerSite` (1-30, default 8), `defaultCountry` (ISO code for local phone numbers), `respectRobotsTxt`.

Per site: `status` (`ok`, `noContacts`, `invalidUrl`, `unreachable`, `blockedByRobots`, `error`), `bestEmail`, `bestEmailDeliverable`, `emails` (each with the page it was found on), `phones`, `socials`, `contactForms`, `addresses`, `companyName`.

Limits: pages are fetched without JavaScript rendering, so sites that need scripts or block non-browser clients may return nothing. Only addresses a site publishes itself are returned. Use them in line with the law and the site's terms where you operate (for example GDPR and CAN-SPAM for outreach).

## License

MIT. See `LICENSE`.
