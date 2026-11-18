# Langar One website

Static site for [langar.one](https://www.langar.one).

- `docs/` — the built site that GitHub Pages serves. Don't edit by hand.
- `src/` — source: `build.py` (page content and templates), `site.css`, `site.js` (form handling).

To change the site, edit files in `src/`, then run `python3 src/build.py` and commit both folders.

Form submissions: set the Google Form details at the top of `src/site.js`.
