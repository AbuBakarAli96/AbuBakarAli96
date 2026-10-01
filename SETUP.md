# Setup & Maintenance Guide

This repository is a **GitHub profile README**. GitHub shows `README.md` on your profile page only when the repository name is **exactly your username**.

## 1. Folder structure and where each file goes

```
AbuBakarAli96/                      <- repo name MUST be AbuBakarAli96
├── README.md                       <- shown on your profile
├── LICENSE                         <- MIT
├── assets/
│   ├── banner.svg                  <- hero banner (animated gradient, neural net, graph line)
│   ├── typing.svg                  <- typing animation (6 roles)
│   ├── divider.svg                 <- animated wave divider (used between sections)
│   ├── profile.svg                 <- Data -> Code -> Intelligence -> Product pipeline
│   ├── coding.svg                  <- animated code window
│   ├── learning.svg                <- "Currently Learning" chips
│   ├── dsa-path.svg                <- DSA learning path
│   ├── roadmap.svg                 <- Data Science roadmap
│   ├── building.svg                <- "Building in Public" status card
│   └── footer.svg                  <- animated wave footer
├── scripts/
│   └── generate_typing.py          <- regenerate typing.svg after editing roles
├── docs/
│   └── SETUP.md                    <- this file (not shown on your profile)
└── .github/workflows/
    └── snake.yml                   <- contribution snake generator
```

## 2. Publish it

1. On GitHub, create a **public** repository named `AbuBakarAli96` (tick "Add a README" only if you plan to overwrite it).
2. Upload everything from this folder, keeping the structure above (make sure `.github/workflows/snake.yml` keeps its exact path).
3. Commit to the `main` branch.
4. Open `https://github.com/AbuBakarAli96`. The README should appear at the top of your profile.

Using git:

```bash
git init
git add .
git commit -m "Add profile README"
git branch -M main
git remote add origin https://github.com/AbuBakarAli96/AbuBakarAli96.git
git push -u origin main
```

## 3. Enable the contribution snake

The snake is **not live until the workflow has run once**. It is commented out in `README.md` on purpose so you never show a broken image.

1. Repo **Settings → Actions → General → Workflow permissions** → choose **Read and write permissions** → Save.
2. Go to the **Actions** tab → **Generate Snake Animation** → **Run workflow**.
3. Wait for the green check. A new branch called `output` now contains `github-contribution-grid-snake.svg` and `github-contribution-grid-snake-dark.svg`.
4. Verify by opening:
   `https://raw.githubusercontent.com/AbuBakarAli96/AbuBakarAli96/output/github-contribution-grid-snake.svg`
5. In `README.md`, find the snake block (search for `SNAKE ANIMATION`). Remove the comment opener line just above the `<div align="center">` and the comment closer line right after the closing `</div>`. Commit.

The workflow re-runs every 12 hours automatically. If a run fails, check that step 1 was saved.

## 4. Replace placeholder project URLs

Placeholders look like this in `README.md`:

```html
<!-- repo-url: bakarcode -->
<kbd>Repo · add link</kbd>
```

Replace the `<kbd>...</kbd>` with a real link:

```html
<a href="https://github.com/AbuBakarAli96/YOUR-REPO">View Project →</a>
```

Same pattern for demos (`live-url: ...` markers):

```html
<a href="https://your-demo-url.com">Live demo →</a>
```

Markers to search for: `bakarcode`, `edunova`, `rescue-route`, `cursor-control`, `tixora-ai` (repo), plus `live-url` markers on BakarCode, Excel Crop Care, EduNova and Tixora AI.
Already linked: Excel Crop Care and Excel Crop Group App.

## 5. Customize colors

| Role | Hex | Used for |
|---|---|---|
| Background | `#05070d` / `#0b1020` | banner, cards |
| Card fill | `#0d1424` / `#0d1117` | nodes, stat cards |
| Cyan | `#22d3ee` | highlights, glows |
| Electric blue | `#3b82f6` | lines, arrows |
| Purple | `#a855f7` | gradient end, final nodes |

- **SVGs:** find and replace the hex values in `assets/*.svg` (or edit `C, B, P` at the top of `scripts/generate_typing.py` for the typing animation).
- **Stat cards in README:** change `bg_color`, `title_color`, `icon_color`, `ring_color`, `fire` and `background` parameters in the image URLs.
- **Badges:** change `logoColor=` values and the `111827` background color in the shields.io URLs.

## 6. Change the typing roles

Edit `ROLES` in `scripts/generate_typing.py`, then run:

```bash
python3 scripts/generate_typing.py
```

Commit the updated `assets/typing.svg`. No extra packages needed.

## 7. Maintain the README

- **Add a project:** copy one `<td>` card in the Featured Projects table; keep two cards per row.
- **Update status:** `assets/building.svg` shows each item as ACTIVE / LEARNING / EXPLORING. Open the SVG in a text editor and change the label text, or the status word and its color (`#22c55e` green, `#eab308` yellow, `#3b82f6` blue).
- **Stats not showing:** `github-readme-stats` (Vercel) and other free services can rate-limit or go down. The README keeps working because the rest is local. If one stays broken, remove that `<img>` line or swap in another service.
- **Cache:** GitHub caches images. After changing an SVG, a hard refresh (Ctrl+Shift+R) or a few minutes of waiting is normal.
- **Review monthly:** open your profile, check every image loads, and update the learning list and roadmap as you actually progress.
- **Stay honest:** statistics cards only show what GitHub reports. Contribution graphs fill in from your real activity, so keep committing.

## 8. Notes on compatibility

- GitHub does not run JavaScript or external CSS in READMEs. All animation here uses SVG (SMIL) that plays when loaded through an `<img>` tag.
- Some shields.io brand icons (for example HTML5, CSS3, Excel) can change names between releases. If a logo disappears, the badge still shows its text; remove or change the `logo=` value.
- Credits: contribution snake by [Platane/snk](https://github.com/Platane/snk).
