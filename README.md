# DriveSmart NJ website

Marketing site for **DriveSmart NJ**, the unofficial study buddy for the New Jersey driver knowledge test.

This is a separate project from the iOS app (`rvincent22/drivesmart-nj`).

## Design

Dark navy (`#0F172A`) and teal (`#2DD4BF`) from the app. Serif headlines, glass navigation, generated brand photography (highway dusk, quiz phone, practice / tutor / exam stills). Copy is taken from the app: guest study, 50-question mocks at 80% to pass, 30 free AI tokens, Lifetime Access $4.99, Trenzannt copyright, and the unofficial-MVC disclaimer.

## Local → production demo

```bash
npm install
npm run dev          # local design:  http://localhost:5173
npm run build
npm run preview      # production demo locally: http://localhost:4173
```

Import this repo in Vercel (Framework Preset: Vite, Output: `dist`). `npm run build` uses site root `/`, which is what Vercel needs.

Push to `main`, then in GitHub: **Settings → Pages → Deploy from a branch → `main` / `/docs`**.

Production:

`https://www.drivesmartnj.com/`

GitHub Pages demo:

`https://xvince-agent-ai.github.io/drivesmart-nj-web/`

Rebuild the Pages folder after site edits:

```bash
npm run build:pages
```

## Demo narration (Kokoro)

To change the demo voiceover later, edit `tools/kokoro/narrate.py` and follow `tools/kokoro/README.md`. The ONNX models stay local and are not committed.

## Legal

- Support: support@drivesmartnj.com
- [Privacy](https://rvincent22.github.io/drivesmart-nj-legal/privacy.html)
- [Terms](https://rvincent22.github.io/drivesmart-nj-legal/terms.html)
- Not affiliated with NJ MVC.
