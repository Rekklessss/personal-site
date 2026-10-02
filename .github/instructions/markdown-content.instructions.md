---
applyTo: "_pages/**/*.md,_posts/**/*.md,_projects/**/*.md"
---

# Markdown content

Use [the content workflow](../../docs/CONTENT_WORKFLOW.md) to find the source of each page. Keep public statements factual and specific to Divyanshu's work and interests.

- Pages and project write-ups require YAML front matter with a valid layout and title.
- Navigation uses `nav`, `nav_order` and `permalink` in page front matter. The résumé URL is `/resume/`.
- Blog filenames follow `YYYY-MM-DD-title.md`. The empty blog landing page is intentional until a real post is added.
- Creating a project write-up does not add a selected card. Register selected projects in `_data/home.yml` and repository metadata in `_data/repositories.yml`.
- About should remain concise, with longer personal details in its expandable section. Do not add placeholder achievements or describe study interests as completed work.
- Use existing assets with descriptive alternative text. Check relative links and generated page paths.
- Format with Prettier, run the production Jekyll build, and preview affected pages on desktop and mobile in both themes.
