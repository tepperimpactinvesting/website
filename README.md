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
1. Repo Settings -> Pages -> Deploy from branch `main`, folder `/ (root)`.
2. Custom domain: the `CNAME` file already contains `tepperimpactinvestingclub.com`. At your domain registrar add four A records to `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` and a `www` CNAME to `<your-github-username>.github.io`. Then tick "Enforce HTTPS" in Pages settings.

Note: the in-page "upload tile" editor only works inside Claude; on GitHub, add photos by editing `assets/` and rebuilding.
