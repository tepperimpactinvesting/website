# Tepper Impact Investing Club website

Single-page, multi-view site (hash routing: `#home`, `#about`, `#member-program`, `#contact`, ...). Plain HTML/CSS/JS, no framework.

## Edit
- All page content, styles and scripts live in `src/template.html`.
- Event calendar data: search for `var EV=` (date, title, type, optional time, optional location).
- Links (Slack, forms, socials): search for `var L=` and the `href=` values.
- Photos / headshots / logos: replace files in `assets/` (keep file names), then rebuild.

## Build
```
python3 build.py
```
This writes `index.html` (self-contained, images embedded). Commit it.

## Host free on GitHub Pages
1. Repo Settings -> Pages -> Source: **GitHub Actions**. The included workflow (`.github/workflows/pages.yml`) rebuilds `index.html` and deploys on every push to `main`, so editors only need to change `src/template.html` or `assets/`. (Alternative: Source = Deploy from branch `main`, folder `/ (root)`, and commit the built `index.html` yourself.)
2. Custom domain (optional): set it in Settings -> Pages -> Custom domain. With the GitHub Actions source, the domain is stored in that setting, so no `CNAME` file is needed in the repo (and removing the domain won't leave the repo broken). At your registrar add four A records to `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` and a `www` CNAME to `<your-github-username>.github.io`. Then tick "Enforce HTTPS".

Note: the in-page "upload tile" editor only works inside Claude; on GitHub, add photos by editing `assets/` and rebuilding.
