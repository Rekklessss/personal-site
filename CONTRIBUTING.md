# Contributing

This repository is a personal portfolio. Keep changes focused and factual, and use the [content workflow](docs/CONTENT_WORKFLOW.md) to find the source for each page.

## Check changes

```bash
npm ci
npx prettier . --write
docker compose run --rm -e JEKYLL_ENV=production jekyll bundle exec jekyll build
```

Preview with `docker compose up` at http://localhost:8080. Check desktop/mobile, light/dark themes, navigation and affected interactions. Regenerate and inspect the PDF for résumé changes. Preserve license notices and never include credentials or generated site files.

Use the [Git conventions](.github/GIT_WORKFLOW.md). Publishing to `main` triggers Amplify, so push only when publication is intended and authorized.
