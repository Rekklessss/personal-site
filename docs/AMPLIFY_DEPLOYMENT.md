# AWS Amplify deployment

This site is a static Jekyll site hosted by AWS Amplify. The Amplify app `personal-site` connects to `Rekklessss/personal-site`, branch `main`, in `us-east-1`.

## Publish an update

1. Edit the site locally and preview with `docker compose up` at <http://localhost:8080>.
2. Format changes with `npm run format` and commit them.
3. Push to `main`. Amplify runs the commands in [`amplify.yml`](../amplify.yml), then serves `_site/`.
4. Check the `main` branch deployment in the [Amplify console](https://us-east-1.console.aws.amazon.com/amplify/apps/d23whgy7kx1qhm/branches/main/deployments?region=us-east-1) and open its generated URL before switching DNS.

The site URL is configured in [`_config.yml`](../_config.yml) as `https://thedivyanshupabia.com`, with an empty `baseurl`. Amplify redirects `www.thedivyanshupabia.com` to the apex domain with a permanent redirect.

## Connect the Hostinger domain

Add `thedivyanshupabia.com` under Amplify **Hosting → Custom domains**. Choose manual DNS configuration if you want to keep DNS at Hostinger. Add the exact certificate validation and domain records shown by Amplify in Hostinger DNS. Keep the existing EC2 records until Amplify reports the certificate and domain are available and the Amplify URL works. Then replace the website records, including `www` if configured, and verify HTTPS on both names. Preserve unrelated records such as MX and TXT records used for email.

## Retire EC2

After the custom domain serves the new site, stop the EC2 instance, verify the site again, and terminate it when no longer needed. Release the Elastic IP after confirming it is no longer referenced by DNS or another service; an idle Elastic IP can still incur charges. Remove the old `EC2_HOST`, `EC2_USER`, `EC2_SSH_KEY`, and `EC2_PORT` GitHub repository secrets after the cutover. Amplify does not use them.
