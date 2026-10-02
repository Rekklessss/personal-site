# Coding instructions

Divyanshu Pabia's portfolio uses Jekyll 4, Liquid, YAML, SCSS and vanilla JavaScript. Deployment is AWS Amplify, not GitHub Pages or EC2. Read [AGENTS.md](../AGENTS.md) for validation and publication rules.

## Source map

See [README.md](../README.md) and [content workflow](../docs/CONTENT_WORKFLOW.md) for current content sources. Navigation comes from page front matter (`nav`, `nav_order`, `permalink`). The public résumé is `/resume/`, with `/cv/` retained as a redirect. Blog is currently an empty landing page. There is no repositories page.

The homepage and Projects page share `_data/home.yml` and `_includes/selected_projects.liquid`. Full experience is `_data/experience.yml`, homepage summaries are `_data/home.yml`, and résumé experience is `_data/cv.yml`. Keep overlapping facts consistent without adding résumé entries the owner has excluded.

## Styling

Geist and Geist Mono are self-hosted in `assets/fonts/`, declared in `_sass/_fonts.scss`. Body text uses Geist, while code and compact labels use Geist Mono. Preserve icon font families. Home styles are in `_sass/_home-profile.scss`, with shared polish in `_sass/_portfolio-polish.scss`. Dark mode uses a green accent and light mode a complementary darker green. Respect reduced-motion preferences and keep interactive controls keyboard accessible.

## Build

Use `docker compose up --build` for development at http://localhost:8080. Production validation is:

```bash
docker compose run --rm -e JEKYLL_ENV=production jekyll bundle exec jekyll build
```

ImageMagick and notebook conversion dependencies are installed by the Dockerfile and Amplify build specification. Keep Ruby/build changes aligned between them. Root `amplify.yml` is a build specification, not a GitHub workflow. GitHub Actions provide formatting, links, accessibility, CodeQL, citation updates, and PDF rendering.

For résumé changes, use `_scripts/render_resume.py` with RenderCV 2.8. It adds the website's company logos and icon contacts to the generated PDF. See README for setup. Check page breaks visually.

Do not publish documentation, development files or secrets in `_site`. Use `_config.yml` exclusions as well as `.gitignore`. Do not remove third-party license notices. Format edits with Prettier and verify desktop/mobile and both color modes before committing.
