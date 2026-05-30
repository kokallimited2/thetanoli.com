# Property Search Engine — Deployment Steps

## Prerequisites
- PropertyData API key (sign up at propertydata.co.uk, free 14-day trial)
- Cloudflare account (email: docateeque@gmail.com)
- Node.js installed

## Step 1: Copy Files to Your Machine

The project is at `~/property-search-engine/` on Folio.
Copy it to your machine, or pull from GitHub once the repo is set up.

## Step 2: Install Dependencies

```bash
cd ~/property-search-engine
npm install
```

## Step 3: Set Up Cloudflare

### Option A — Cloudflare Workers + Pages (Recommended)

1. Go to https://dash.cloudflare.com → Workers & Pages
2. Click "Create Application" → "Worker"
3. Name it `property-search-engine`
4. Deploy the default worker first to create the project
5. Then, use the dashboard to edit the worker code:
   - Copy the content of `src/worker.js` into the Cloudflare Worker editor
   - Upload `public/index.html` as a static asset
6. Set environment variable:
   - Settings → Variables → Add `PROPERTYDATA_API_KEY` = your key
7. Add route: set up so `/property-search/*` goes to the worker

### Option B — Wrangler CLI

```bash
cd ~/property-search-engine
npx wrangler login
npx wrangler deploy
npx wrangler secret put PROPERTYDATA_API_KEY
```

## Step 4: Test

1. Go to `https://property-search-engine.your-subdomain.workers.dev/`
2. Click "Check API" button to verify connection
3. Enter a postcode (e.g., OX3 9DW) and select a strategy
4. Click Search

## Step 5: Connect to thetanoli.com (Optional)

1. In Cloudflare Dashboard → Workers & Pages → property-search-engine
2. Triggers → Custom Domain
3. Enter `thetanoli.com/property-search/*`
4. Update the DNS record if needed

## Notes

- The frontend API calls go to `/api/*` (same origin) by default
- If you host the frontend separately from the worker, update `API_BASE` in `public/index.html`
- The system costs ~5 API credits per search
- At API 2k plan (£28/mo): ~400 searches/month
- No database needed — everything is live API calls
