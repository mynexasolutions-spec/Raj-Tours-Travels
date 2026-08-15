# Package Image Sources Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make the three package categories use the approved local domestic, international, and airport departure images.

**Architecture:** Keep the existing package-card rendering and category filtering unchanged. Update the Flask data assembly so domestic and international cards scan their new folders, while the Other category is defined explicitly with the local airport image and existing departure metadata.

**Tech Stack:** Flask, Jinja2, Python standard library, local static assets.

---

### Task 1: Update package image source configuration

**Files:**
- Modify: `app.py:6-132` for package metadata and `app.py:162-193` for card assembly

**Step 1: Inspect current source behavior**

Confirm `get_package_cards` scans the legacy folders and that `PACKAGE_DETAILS` keys are tied to legacy filenames.

**Step 2: Implement the minimal source update**

- Add metadata keyed by destination image stem or filename for the new `domestic` and `international` folders.
- Keep the existing details, price, and WhatsApp booking data for matching destinations.
- Make `get_package_cards` accept the new folder names.
- Build the Other package list explicitly with `images/group-departures.webp`, rather than scanning `other Tour Packages`.
- Preserve generic fallback metadata for any unmatched local destination image.

**Step 3: Verify Python syntax**

Run: `python -m py_compile app.py`

Expected: command exits successfully with no output.

**Step 4: Verify route data with Flask test client**

Run a short Python check using `app.test_client()` and assert that `/packages?category=domestic`, `/packages?category=international`, and `/packages?category=other` return HTTP 200 and contain the expected local static paths.

Expected: all three assertions pass; no legacy `Tour Packages` image path appears in the rendered HTML.

**Step 5: Review the diff and status**

Run: `git diff -- app.py` and `git status --short`

Expected: only the intended application changes are unstaged; user-provided image assets remain untouched and un-staged.

**Step 6: Commit the implementation**

```bash
git add app.py
git commit -m "feat(packages): use local destination images"
```

### Task 2: Verify rendered package pages

**Files:**
- Test: Flask route responses for `/packages?category=domestic`, `/packages?category=international`, and `/packages?category=other`

**Step 1: Check image file existence**

Confirm the image files referenced by the response exist under `static/images`.

**Step 2: Check category isolation**

Confirm each response has the correct active category and does not render the other category's package group as visible.

**Step 3: Check source references**

Confirm domestic responses reference `images/domestic/`, international responses reference `images/international/`, and Other references `images/group-departures.webp`.

**Step 4: Record any limitation**

If no browser or test framework is configured, report route-level verification instead of adding unnecessary test infrastructure.
