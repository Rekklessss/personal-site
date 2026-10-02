# Agent guidelines

This is Divyanshu Pabia's personal portfolio. Read [.github/copilot-instructions.md](.github/copilot-instructions.md) before editing.

## Project conventions

- Jekyll, Liquid, SCSS and vanilla JavaScript. AWS Amplify publishes `_site` from `main` using `amplify.yml`.
- Keep `url: https://thedivyanshupabia.com` and an empty `baseurl` together. The canonical domain has no `www`.
- Use the content sources listed in [README.md](README.md). Selected projects share `_data/home.yml` and `_includes/selected_projects.liquid` across About and Projects.
- Keep professional claims accurate. Study interests do not imply professional proficiency. Preserve required third-party license notices.
- Preserve unrelated working changes. Commit or push only when the user authorizes it.

## Verification

```bash
npm ci
npx prettier . --write
docker compose run --rm -e JEKYLL_ENV=production jekyll bundle exec jekyll build
docker compose up
```

Before committing, check navigation, project cards, experience expansion, skill filters, company logos, and light/dark themes at http://localhost:8080 on desktop and mobile. For résumé edits, regenerate and inspect the PDF too.

## Further guidance

- [Content workflow](docs/CONTENT_WORKFLOW.md)
- [Amplify deployment](docs/AMPLIFY_DEPLOYMENT.md)
- [Troubleshooting](TROUBLESHOOTING.md)
- [Git conventions](.github/GIT_WORKFLOW.md)
- [Customization agent](.github/agents/customize.agent.md)
- [Documentation agent](.github/agents/docs.agent.md)
- File-specific instructions are in `.github/instructions/`.
