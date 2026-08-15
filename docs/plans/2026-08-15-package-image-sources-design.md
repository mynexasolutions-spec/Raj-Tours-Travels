# Package Image Sources Design

## Goal

Replace the legacy package image folders used by `/packages?category=domestic`, `/packages?category=international`, and `/packages?category=other` with the approved local image sources.

## Design

- Domestic package cards are discovered from `static/images/domestic`.
- International package cards are discovered from `static/images/international`.
- The Other category contains one card using `static/images/group-departures.webp`.
- Existing package metadata is matched to destination names where possible; unmatched images receive the existing generic fallback metadata.
- The legacy `domestic Tour Packages`, `international Tour Packages`, and `other Tour Packages` folders are no longer referenced. Existing files remain untouched.
- The existing package template, category filtering, image URL generation, and WhatsApp booking links remain unchanged.

## Verification

- Confirm each category page renders only its approved image source.
- Confirm image paths resolve through Flask's static URL helper.
- Confirm the category counts and booking links remain functional.
