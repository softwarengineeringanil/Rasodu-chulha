# Live order & rider tracking: what it needs

The website itself is static. Order tracking and live rider location cannot run
in the browser alone. They need a backend that enforces access rules. Nothing
in `index.html` shows tracking today: `CONFIG.liveTrackingEnabled` is `false`
and the order flow is WhatsApp only.

## 1. Backend choice
Supabase (Postgres + Auth + Realtime) or Firebase. Either works. Only the
public/anon client key may appear in frontend code. Service-role or admin keys
stay on the server (edge functions) and are never shipped in HTML or JS.

## 2. Tables
- orders: id, order_id (random, e.g. RC-20260928-K7Q2, not sequential), customer_name,
  customer_phone, delivery_address, landmark, quantity, unit_price, total, status,
  rider_id, created_at, updated_at
- riders: id, name, phone (business/relay number), photo, vehicle_type, vehicle_number, active
- rider_locations: rider_id, order_id, lat, lng, accuracy, heading, speed, updated_at
  (one row per active order, overwritten. Do not keep location history.)

Status values: received, confirmed, preparing, ready, rider_assigned, picked_up,
out_for_delivery, delivered, cancelled.

## 3. Security rules (must be enforced server-side)
- Price, total, status and rider assignment are set by the server only. Never trust the browser.
- Compute total on the server as quantity x price. Reject quantity outside 1-20.
- Customers look up an order only with order_id + phone. Use a server function that
  returns that one order. Do not open the tables to public reads.
- Rider location is readable only for the rider's active order, only after that lookup succeeds,
  and is deleted/stopped when status becomes delivered or cancelled.
- Riders and admins sign in (Auth). Riders can read/update only orders assigned to them.
- Never expose a rider's personal number. Use a business or relay number.

## 4. Pages to build once the backend exists
- /track: order ID + phone, then status timeline, rider card, live map (only while tracking is active).
  Show "Last updated X seconds ago". If stale, say so. Never label stale data "Live".
- /rider (mobile-first, large buttons): login, assigned orders, Accept, Start Delivery
  (asks for location permission and starts sharing), Picked Up, Out for Delivery, Delivered
  (stops sharing). Send location on ~30 s or ~50 m movement, whichever comes first (configurable).
  If permission is denied, show the order anyway and explain how to enable location.
- /admin: list orders, confirm, assign rider, update status, cancel.
- Map: OpenStreetMap + Leaflet needs no secret key.

## 5. Order creation
Today the website only opens WhatsApp with the customer's details. To track an order it
must first be created in the backend (server function validates input, generates order_id),
then the order_id is included in the WhatsApp message and shown to the customer.

## 6. Business information needed
Production domain, delivery area, opening hours, rider list, who confirms orders,
whether a delivery fee applies, map provider choice.
