# International Destinations and Events Navigation Design

## Goal

Add Bhutan and Sri Lanka to the home page's Beyond Borders section and make the existing events page discoverable.

## Design

- Add Bhutan and Sri Lanka cards to the existing international destinations grid in `templates/pages/index.html`.
- Use the tracked local assets `images/international/baku.webp` for Bhutan and `images/international/sri-lanka.webp` for Sri Lanka.
- Add an Events link pointing to the existing `events` Flask route in both desktop and mobile navigation.
- Preserve the existing destination card markup, reveal animations, responsive grid, and `/events` page implementation.

## Verification

- Confirm the home page contains Bhutan and Sri Lanka with local image paths.
- Confirm desktop and mobile navigation contain links resolving to `/events`.
- Confirm `/events` still returns HTTP 200.
- Run template/rendering and Python syntax checks where available.
