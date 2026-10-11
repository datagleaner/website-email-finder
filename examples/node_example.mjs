// npm install apify-client
// APIFY_TOKEN=... node node_example.mjs stripe.com basecamp.com
import { ApifyClient } from 'apify-client';

const sites = process.argv.slice(2);
if (!sites.length) sites.push('stripe.com', 'basecamp.com', 'https://www.appier.com');

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/website-contact-details-scraper').call({
    websites: sites,
    maxPagesPerSite: 5,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    console.log(item.website, item.status, 'best:', item.bestEmail, 'all:', (item.emails || []).map((e) => e.value));
}
