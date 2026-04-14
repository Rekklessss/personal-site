# Content Workflow

This repo is set up so the day-to-day workflow stays simple:

1. Create or update content locally.
2. Preview the site with Docker.
3. Format the repo.
4. Push to `main`.
5. Let GitHub Actions deploy the built static site to EC2.

## Local preview

```bash
npm install
npm run dev
```

Open [http://localhost:8080](http://localhost:8080).

Use `npm run dev:build` if you change dependencies or Docker-related files.

## Create a blog post

```bash
npm run new:post -- "Shipping My Portfolio on AWS" engineering
```

That creates a file like `_posts/2026-04-13-shipping-my-portfolio-on-aws.md`.

After that:

1. Update the `description`.
2. Add tags if you want.
3. Write the post body.
4. Preview the result locally.

## Create a project page

```bash
npm run new:project -- "Personal Portfolio" "Jekyll portfolio deployed to AWS EC2 with GitHub Actions"
```

That creates a file in `_projects/` with a starter structure you can fill in.

## Publish changes

```bash
npm run format
git status
git add _config.yml _pages/about.md _posts/2026-04-13-your-post.md
git commit -m "feat: publish new blog post"
git push origin main
```

Once the push lands on `main`, the deploy workflow builds the site and syncs `_site/` to EC2.

## Recommended writing rhythm

- Use `about.md` for your high-level story.
- Use `_projects/` for durable case studies.
- Use `_posts/` for lightweight notes, lessons, experiments, and essays.
- Keep posts short and frequent; promote the best ones into richer project pages later.

## Files you will edit most often

- `_pages/about.md`
- `_posts/*.md`
- `_projects/*.md`
- `_data/cv.yml`
- `_data/socials.yml`
- `_data/repositories.yml`
