---
applyTo: "_config.yml,_data/**/*.yml"
---

# YAML configuration

Read [coding instructions](../copilot-instructions.md) and the [content source map](../../docs/CONTENT_WORKFLOW.md).

- Keep `url: https://thedivyanshupabia.com` and an empty `baseurl`. Preserve the apex canonical domain.
- Quote strings containing colons or other YAML special characters. Follow existing indentation.
- Homepage selected projects use `_data/home.yml`. Both About and Projects consume the same list.
- Homepage skills use `_data/skills.yml`, including category, icon and optional study metadata.
- Experience data is separate for home summaries, the full experience page and the résumé. Keep overlapping dates, locations and titles consistent.
- `_data/cv.yml` uses RenderCV 2.8 and supplies the web résumé and PDF. The web page is `/resume/`. See README for the render command.
- Company logos are mapped in `_data/organizations.yml`. Repository categories and links are in `_data/repositories.yml`, used on Projects.
- Preserve `_config.yml` exclusions for development files and docs. The generated PDF remains public, while its layout configuration is excluded.
- Format with Prettier, build Jekyll in production mode, and check affected pages. Regenerate and inspect the PDF when CV content changes.
