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
pip install "rendercv[full]==2.8" pyyaml
python _scripts/render_resume.py
```

## Documentation

[Content workflow](docs/CONTENT_WORKFLOW.md) · [Troubleshooting](TROUBLESHOOTING.md) · [Agent instructions](AGENTS.md)

The source is distributed under the terms in [LICENSE](LICENSE). Preserve required third-party copyright and permission notices.
