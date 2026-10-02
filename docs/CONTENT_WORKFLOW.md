# Content workflow

Edit source files, preview locally, format, and validate. Push only when ready and authorized to publish. Amplify automatically deploys changes to `main`.

## Sources

| Content                                 | Source                                                        |
| --------------------------------------- | ------------------------------------------------------------- |
| About and expanded personal story       | `_pages/about.md`                                             |
| Homepage experience summaries           | `_data/home.yml`                                              |
| Selected projects on About and Projects | `_data/home.yml`, `_includes/selected_projects.liquid`        |
| Full experience                         | `_data/experience.yml`                                        |
| Company logos                           | `_data/organizations.yml`, `assets/img/`                      |
| Homepage skill groups and icons         | `_data/skills.yml`, `_includes/home_skills.liquid`            |
| Web and PDF résumé                      | `_data/cv.yml`, `_scripts/render_resume.py`                   |
| PDF layout                              | `assets/rendercv/design.yaml`, `settings.yaml`, `locale.yaml` |
| Other project/repository cards          | `_data/repositories.yml`                                      |
| Project detail pages                    | `_projects/`                                                  |
| Research and publications               | `_pages/research.md`, `_bibliography/papers.bib`              |
| Blog landing page and posts             | `_pages/blog.md`, `_posts/`                                   |
| Social destinations                     | `_data/socials.yml`                                           |
| Navigation                              | `_pages/` front matter (`nav`, `nav_order`, `permalink`)      |

## Projects

Selected projects use one shared card template and data list on both pages. Update `_data/home.yml` to add or change a selection. Register repository metadata in `_data/repositories.yml` and label forks accurately. Featured repositories are excluded from the lower project index to avoid duplicates.

To create a longer write-up:

```bash
npm run new:project -- "Project title" "Short description"
```

The helper creates a file in `_projects/`. It does not register a selected card or repository entry automatically. Keep those entries and their links consistent.

## Blog

The blog landing page is intentionally empty until a real post is ready. Create a post with:

```bash
npm run new:post -- "Post title" engineering
```

Edit its description, tags and body. Remove example text before publication.

## Experience and résumé

Keep company names, titles, dates and locations consistent across home, experience and résumé data. The résumé intentionally excludes esports and Next Tech Lab. Homepage shows the three most recent entries before an expandable list. Avoid presenting study topics as demonstrated proficiency.

Use the PDF setup in [README](../README.md). The first PDF page ends with Projects, followed by Publications and Skills on page two.

## Appearance and validation

Styles live in `_sass/` and are loaded by `assets/css/main.scss`. Geist and Geist Mono are self-hosted with their licenses in `assets/fonts/`. Use the shared theme variables for accents and hover states.

```bash
npm ci
npm run format
docker compose run --rm -e JEKYLL_ENV=production jekyll bundle exec jekyll build
docker compose up
```

Check http://localhost:8080 on desktop and mobile, including both themes, skill filters, experience expansion, links and the résumé download. Review `git diff` before staging specific files. Publication instructions are in [the Amplify guide](AMPLIFY_DEPLOYMENT.md).

The home-only intro is `_includes/intro.liquid`, `assets/js/intro.js` and `_sass/_intro.scss`. It runs on a first visit and every homepage refresh, but skips internal navigation and browser back/forward returns, can be skipped, and is disabled for reduced motion. Theme selection defaults to the visitor’s system preference, with explicit light/system/dark choices retained.
