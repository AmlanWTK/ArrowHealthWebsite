# Arrow Health — Website

**Live: https://arrowhealthwebsite.web.app**

The product site for **Arrow Health**, an AI-assisted health-intelligence app. It presents the product surface — glucose trends, meal safety, medication scanning, an AI wellness companion, activity tracking and a suite of health calculators — alongside a directory of participating doctors and a waitlist signup.

Fully bilingual: every string on every page swaps between **English and বাংলা** through a client-side translation layer with a fade transition.

## Pages

| Page | What it covers |
|---|---|
| `index.html` | Landing page — product overview, feature tour, doctor directory, waitlist |
| `glucose.html` | Glucose trend tracking and interpretation |
| `meal_estimation.html` | Meal-photo nutrition and safety estimation |
| `medicine.html` | MedSnap — medication scanning and verification |
| `ai_wellness.html` | AI wellness companion grounded in the user's own health values |
| `activity.html` | Daily activity and energy-burn tracking |
| `calculators.html` | BMI, BMR, TDEE, Growth IQ and Health Pulse, with saved results |
| `ramadan_calculator.html` | Fasting-aware planning for patients observing Ramadan |
| `feature.html` | Long-form feature breakdown |

## Bilingual system

`translations.js` holds a single `TRANSLATIONS` object with parallel `en` and `bn` trees — roughly 1,400 keys covering navigation, headings, body copy, calculator labels and CTAs across all pages. The language toggle fades the page out, swaps every mapped node, and fades back in, so the switch reads as a transition rather than a reload.

## Doctor directory

`doctors_data.json` holds 43 doctor profiles — name, qualifications, specialty, portrait and biography. `generate_doctors.js` renders the directory cards from that file, so adding a doctor means editing the JSON, not the markup.

## Stack

No framework and no build step — the site is plain HTML, CSS and JavaScript served as static files.

- `style.css` — ~180 KB design system: layout, typography, theming, component styles
- `script.js` — ~29 KB of navigation, scrollspy, interactions and calculator logic
- `scroll-reveal.css` / `scroll-reveal.js` — `IntersectionObserver`-driven reveal animations
- `translations.js` — EN ↔ BN translation layer
- `assets/`, `appimages/`, `appcard/` — imagery, app screenshots and card artwork

## Local development

```bash
git clone https://github.com/AmlanWTK/ArrowHealthWebsite.git
cd ArrowHealthWebsite
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Deployment

Firebase Hosting, project `arrowhealthwebsite`. The repository root is the deploy root and all unmatched routes rewrite to `index.html`.

```bash
firebase deploy --only hosting
```

## Maintenance scripts

The `*.py` files in the repository root are one-off content-injection helpers used while building the site — adding navigation entries to calculator pages, injecting footers, wiring scroll-reveal into existing markup, and merging doctor records. They are historical tooling, not part of the deployed site, and Firebase does not upload them.
