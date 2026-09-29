# Frontend skeleton

This delivery implements slides 2–18 of **Team Aardvark BC Social — Delivery 1 Prototypes**. Slide 1 is the presentation cover. All people, dates, prices, and counts are static examples from the deck.

## Run locally

Use Python 3.10 or newer (verified with Python 3.12):

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py check
python manage.py test frontend
python manage.py runserver
```

Open `http://127.0.0.1:8000/` for the landing page or `/home/` for the application. No migrations, database, account, or login are required. Settings are for local development only.

## Structure and future feature apps

`bcsocial/` contains Django project configuration. `frontend/` currently owns GET-only rendering, fixed examples in `sample_data.py`, and templates/static assets. There are no models, migrations, APIs, POST handlers, sessions, or authentication components.

Templates use feature-owned paths (`accounts/`, `events/`, `marketplace/`, `messaging/`, `clubs/`, `connections/`, `news/`) rather than a flat collection of frontend pages. URL namespaces follow those features. A future app can take its template directory, URL patterns, view functions, and sample data replacement without renaming shared template links.

`core/base.html` owns the document and styles. `core/app_base.html` adds the sidebar and page header. Shared components live in `core/components/`; event, listing, news, directory, and messaging components live with their features. Clubs/community share a directory layout, and the three conversations share a conversation layout.

`static/core/css/styles.css` contains shared tokens followed by labeled feature sections. Move those sections into feature stylesheets as the app grows; no CSS framework beyond Bootstrap is required. Shared artwork currently lives in `static/core/images/`, with original PowerPoint media names for traceability. All 57 embedded media files are preserved byte for byte. Crop rules reproduce selected PowerPoint crop rectangles in CSS without changing the files.

Bootstrap 5.3.3 CSS and its license are vendored in `static/vendor/bootstrap/`. Its unused source-map reference is omitted. No Bootstrap JavaScript, external font requests, build pipeline, or Node dependency is required to run the app.

## Screens

| Slide | URL | Template |
| --- | --- | --- |
| 2 | `/` | `accounts/landing.html` |
| 3 | `/profile/edit/` | `accounts/profile_edit.html` |
| 4 | `/profile/` | `accounts/profile.html` |
| 5 | `/home/` | `core/home.html` |
| 6 | `/clubs/` | `clubs/index.html` |
| 7 | `/community/` | `clubs/community.html` |
| 8 | `/connections/` | `connections/index.html` |
| 9 | `/messages/` | `messaging/inbox.html` |
| 10 | `/messages/individual/` | `messaging/individual.html` |
| 11 | `/messages/club/` | `messaging/club.html` |
| 12 | `/messages/marketplace/` | `messaging/marketplace.html` |
| 13 | `/events/` | `events/index.html` |
| 14 | `/events/fall-concert/` | `events/detail.html` |
| 15 | `/events/new/` | `events/create.html` |
| 16 | `/marketplace/` | `marketplace/index.html` |
| 17 | `/marketplace/new/` | `marketplace/create.html` |
| 18 | `/news/` | `news/index.html` |

## Prototype boundaries and visual differences

- Navigation links open approved screens. The Club and Marketplace labels in the message inbox open their example conversations directly, since those category inbox states are not shown in the deck.
- Sign-in navigates to the static home screen without authentication. Save, Send, Join, RSVP, uploads, posting, favorites, filters, and unshown destinations are disabled. Text inputs and native controls can be edited locally but do not submit, persist, or update previews. Requests tabs and the sidebar Search control have no invented content.
- The forms intentionally use labeled controls without submission forms. Native dropdowns only contain choices represented in the corresponding prototype.
- Fonts follow the deck's Inter/Space Grotesk/Calibri declarations with system fallbacks. Exact glyph shapes and wrapping vary with installed fonts; there are no bundled font files in the presentation.
- The desktop layout follows the deck. Narrow screens stack existing content without adding mobile-only features.
- The deck's example data, including inconsistent year/date wording, remains unchanged.

## Checks

`python manage.py test frontend` verifies all 17 screens, template selection, asset resolution, internal navigation, and rejection of POST requests. `SimpleTestCase` prevents accidental database queries. Browser QA additionally covers static HTTP responses, decoded images, desktop/mobile overflow, and comparison with every corresponding slide.
