# Deploy checklist

## 1. Domain (required)
    python3 set-domain.py https://your-real-domain.in
Fills `SITE_URL`, canonical, `og:url`, `og:image`, `twitter:image`, robots.txt and sitemap.xml.

## 2. Social preview image (required)
Add `assets/og-image.jpg` at 1200x630. The photos supplied so far are 360x485 with text baked in, so none suit this.

## 3. Photos (recommended)
Replace the files in `assets/` with larger originals (about 1200 px wide or more). The current ones look soft on big or high-density screens.

## 4. Google Analytics 4 (optional)
1. Create a GA4 property and copy its Measurement ID (looks like `G-XXXXXXXXXX`).
2. In `index.html`, in `SITE_CONFIG`, set `GA_MEASUREMENT_ID: 'G-XXXXXXXXXX'` and `ANALYTICS_ENABLED: true`.
3. Deploy. Visitors see an Allow / No thanks choice; Google loads only after Allow.
4. Verify in GA4 > Admin > DebugView or Reports > Realtime.
Events sent (no personal data): view_menu, begin_order, change_quantity, order_form_start,
whatsapp_order_click (quantity, value), whatsapp_click, phone_order_click, instagram_click, navigation_click.
`whatsapp_order_click` means the customer opened WhatsApp. It is not a purchase and is not sent as one.

## 5. Facts only the owner can supply
Address, opening hours, delivery area, delivery fee, payment methods, cancellation rules.
None are on the site or in the structured data, and nothing was invented.
`terms.html` was not created for that reason. Write it once these policies exist.

## 6. Before going live
- Test the order form and WhatsApp message on a real phone (Android and iPhone).
- Check the site at 320, 375, 414, 768 and 1280 px, and run Lighthouse on the live URL.
- Confirm the FSSAI number in the footer is the one on your licence.
- Have the owner read privacy.html and confirm it matches how you handle WhatsApp chats.
