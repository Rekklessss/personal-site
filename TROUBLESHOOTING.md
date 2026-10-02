# Troubleshooting

## Local preview

Start Docker Desktop, then run `docker compose up --build`. The site uses http://localhost:8080. If the port is occupied, stop the conflicting service or existing preview. `docker compose down` stops this project's containers.

Changes to `_config.yml` require restarting Jekyll. Content and SCSS normally rebuild automatically. Rebuild the Docker image after changing dependencies or the Dockerfile.

## Build failures

Run the production build locally to reproduce errors:

```bash
docker compose run --rm -e JEKYLL_ENV=production jekyll bundle exec jekyll build
```

Check the first error, YAML indentation and quoting, Liquid syntax, and referenced assets. ImageMagick is required for responsive images and is installed in Docker and Amplify. Keep `url: https://thedivyanshupabia.com` and an empty `baseurl`.

If Amplify reports an empty `platform`, its app configuration needs the static hosting platform `WEB`. This is an Amplify configuration error rather than a Jekyll source error. Check the app and branch settings, then redeploy using [the deployment guide](docs/AMPLIFY_DEPLOYMENT.md).

## Fonts and styling

Geist and Geist Mono are served from `assets/fonts/`. Confirm the WOFF2 files return HTTP 200, rebuild, then refresh the browser. Font Awesome and academic icons retain separate fonts. Avoid overriding all elements with a universal font rule.

A production styling difference can come from PurgeCSS. Check selectors against `purgecss.config.js`, especially classes created by JavaScript. Verify both themes and narrow screens.

## Résumé PDF

Install the pinned dependencies in a virtual environment and run `_scripts/render_resume.py` as described in [README.md](README.md). Use this wrapper rather than calling RenderCV alone, because it adds company logos and icon contacts. Inspect both PDF pages after edits, especially the header and the break after Projects.

## Domain redirects

The apex domain is canonical. Check Amplify's custom-domain settings and redirect rules if `www` becomes canonical again. Keep Hostinger's validation records and unrelated mail records intact. See [hosting instructions](docs/AMPLIFY_DEPLOYMENT.md).
