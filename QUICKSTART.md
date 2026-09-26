# Quick start

This repository publishes `thedivyanshupabia.com` with AWS Amplify. See the [Amplify deployment guide](docs/AMPLIFY_DEPLOYMENT.md) for domain setup and migration from EC2.

1. Install dependencies with `npm install` and preview with `npm run dev`.
2. Edit `_config.yml`, `_pages/about.md`, or other content files.
3. Format with `npm run format` and check the preview at <http://localhost:8080>.
4. Commit and push to `main`. Amplify builds the site using `amplify.yml`.
5. Check the deployment in the [Amplify console](https://us-east-1.console.aws.amazon.com/amplify/apps/d23whgy7kx1qhm/branches/main/deployments?region=us-east-1).

To create content, use `npm run new:post -- "Post Title" category` or `npm run new:project -- "Project Title" "Description"`.
