# Divyanshu Pabia — personal website

Portfolio focused on LLM systems, GPU computing, inference, and performance engineering.

**Website:** https://thedivyanshupabia.com

**Stack:** Jekyll, Liquid, SCSS, vanilla JavaScript, AWS Amplify. Typography uses self-hosted Geist for text and Geist Mono for code and compact labels.

## Local preview

```bash
docker compose up --build
```

Open http://localhost:8080. Stop with `docker compose down`.

## Edit content

| Content                          | Source                                           |
| -------------------------------- | ------------------------------------------------ |
| Homepage and expanded biography  | `_pages/about.md`                                |
| Selected experience and projects | `_data/home.yml`                                 |
| Company logos                    | `_data/organizations.yml`, `assets/img/`         |
| Skills and icons                 | `_data/skills.yml`                               |
| Full experience                  | `_data/experience.yml`                           |
| Selected résumé experience       | `_data/cv.yml`                                   |
| Project write-ups and index      | `_projects/`, `_data/repositories.yml`           |
| Research                         | `_pages/research.md`, `_bibliography/papers.bib` |
| Blog posts                       | `_posts/`                                        |
| Site settings                    | `_config.yml`                                    |

Keep experience claims backed by projects or professional work. Study status belongs in skill metadata and tooltips, rather than repeated visible labels. Use a logo asset only when it is the organization's actual logo.

## Validate changes

```bash
npm ci
npx prettier . --write
docker compose run --rm -e JEKYLL_ENV=production jekyll bundle exec jekyll build
```

Check desktop/mobile layout, navigation, light/dark themes, images, and links at http://localhost:8080 before publishing.

## Deployment

Amplify builds `_site` using `amplify.yml`. Changes pushed to the connected branch trigger a deployment. See [deployment instructions](docs/AMPLIFY_DEPLOYMENT.md). Keep `url: https://thedivyanshupabia.com` and `baseurl:` empty.

## Résumé

The web résumé reads `_data/cv.yml`. Generate the downloadable PDF with RenderCV 2.8:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python _scripts/render_resume.py
```

## Dependency maintenance

Build with Ruby 4.0.7, Bundler 4.0.22 and Node.js 24 LTS. Docker, GitHub Actions and Amplify use the same Ruby and Node release lines. Install Node dependencies with `npm ci` and Python tools with `pip install -r requirements.txt`.

After changing Ruby dependencies, rebuild with `docker compose up --build`. Preview startup checks the installed gems and preserves the working lockfile.

Ruby gems resolve to the newest versions supported by Jekyll and its plugins. Browser libraries retain compatible major versions, with updated CDN integrity hashes. Bootstrap 4 and jQuery 3 remain paired with the site's existing MDB components. PurgeCSS stays at 7.0.2 because version 8 currently brings an audited vulnerable dependency chain. Recheck this constraint when updating dependencies.

Run `npm run format:check`, `npm audit`, the production Jekyll build and `npm run css:purge` after updates. Preview desktop and mobile layouts in both themes, including navigation, skill filters and expandable experience. Verify the generated résumé when changing RenderCV.

## Documentation

[Content workflow](docs/CONTENT_WORKFLOW.md) · [Troubleshooting](TROUBLESHOOTING.md) · [Agent instructions](AGENTS.md)

The source is distributed under the terms in [LICENSE](LICENSE). Preserve required third-party copyright and permission notices.
