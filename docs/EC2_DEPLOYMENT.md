# EC2 Deployment Guide

This repo is configured to deploy as a static site to EC2.

## Architecture

- Jekyll builds the site into `_site/`.
- GitHub Actions builds on every push to `main`.
- The workflow syncs `_site/` to your EC2 instance with `rsync` over SSH.
- Nginx serves the static files.
- `thedivyanshupabia.com` and `www.thedivyanshupabia.com` point to the EC2 Elastic IP.
- Certbot adds HTTPS once DNS resolves.

## Assumptions

- Your instance is reachable with SSH.
- You are using Ubuntu on EC2.
- The site will live at `/var/www/thedivyanshupabia.com/current`.
- The deploy user is the default SSH user for your AMI, such as `ubuntu`.

If you launched Amazon Linux instead of Ubuntu, keep the same Nginx idea but adjust package commands.

## 1. Point the domain from Hostinger to EC2

In Hostinger DNS for `thedivyanshupabia.com`:

- Add an `A` record for `@` pointing to your EC2 Elastic IP.
- Add a `CNAME` record for `www` pointing to `thedivyanshupabia.com`.
- Do not create an `AAAA` record unless you are also serving the site over IPv6.

Once saved, give DNS time to propagate.

## 2. Confirm the EC2 security group

Allow these inbound rules:

- `22` from your IP address only
- `80` from `0.0.0.0/0`
- `443` from `0.0.0.0/0`

If you use IPv6 on the instance, also allow `80` and `443` from `::/0`.

## 3. Prepare the server

SSH into the instance and run:

```bash
sudo apt-get update
sudo apt-get install -y nginx certbot python3-certbot-nginx rsync
sudo mkdir -p /var/www/thedivyanshupabia.com/current
sudo chown -R "$USER":www-data /var/www/thedivyanshupabia.com
sudo chmod -R 775 /var/www/thedivyanshupabia.com
```

Copy the Nginx config from `ops/nginx/thedivyanshupabia.com.conf` into `/etc/nginx/sites-available/thedivyanshupabia.com`:

```bash
sudo cp ops/nginx/thedivyanshupabia.com.conf /etc/nginx/sites-available/thedivyanshupabia.com
sudo ln -s /etc/nginx/sites-available/thedivyanshupabia.com /etc/nginx/sites-enabled/thedivyanshupabia.com
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl reload nginx
```

At this point you can place a temporary `index.html` in `/var/www/thedivyanshupabia.com/current/` if you want to test the web server before the first GitHub deploy.

## 4. Add GitHub Actions secrets

In GitHub, open `Settings -> Secrets and variables -> Actions` and create:

- `EC2_HOST`
  Use the Elastic IP or a DNS name that resolves to the instance.
- `EC2_USER`
  Usually `ubuntu` on Ubuntu AMIs.
- `EC2_SSH_KEY`
  Paste the private key contents for the SSH key allowed on the server.
- `EC2_PORT`
  Optional. Leave unset if you use the default SSH port `22`.

The deploy workflow already assumes the target directory is:

```text
/var/www/thedivyanshupabia.com/current
```

## 5. Run the first deployment

From your local repo:

```bash
npm install
npm run format
git status
git add _config.yml _pages/ _data/ .github/workflows/deploy.yml bin/ docs/ ops/ package.json assets/json/resume.json
git commit -m "feat: configure initial portfolio deployment"
git push origin main
```

Then watch the `Deploy site` workflow in GitHub Actions. If it succeeds, your built site should now exist on the EC2 instance under `/var/www/thedivyanshupabia.com/current`.

## 6. Enable HTTPS

Once DNS is resolving to the instance and Nginx is serving the domain over port 80, run:

```bash
sudo certbot --nginx -d thedivyanshupabia.com -d www.thedivyanshupabia.com
```

Choose the redirect option when prompted so HTTP automatically forwards to HTTPS.

Then verify renewal:

```bash
sudo certbot renew --dry-run
```

## 7. Smoke-test the live site

Check these URLs:

- `http://thedivyanshupabia.com`
- `https://thedivyanshupabia.com`
- `https://www.thedivyanshupabia.com`

Verify:

- The home page loads.
- CSS and fonts load correctly.
- `/blog/`, `/projects/`, `/repositories/`, and `/cv/` load.
- The SSL certificate is valid.

## 8. Ongoing updates

After the one-time setup, the workflow is:

1. Edit locally.
2. Preview with Docker.
3. Push to `main`.
4. Let GitHub Actions redeploy automatically.

There is no app server to restart because Nginx is just serving new static files after each sync.
