# Deploying AmateurHour Coaching to Render

## Prerequisites

- GitHub account
- Render account (free tier works great)
- Code pushed to GitHub repository

## Step 1: Push to GitHub

```bash
cd "/Users/dontestevens/Desktop/CyNet Security & Design LLC/Sites/AmateurHour_Flask_Site"

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - AmateurHour Coaching website"

# Add your GitHub remote
git remote add origin YOUR_GITHUB_REPO_URL

# Push to GitHub
git push -u origin main
```

## Step 2: Deploy on Render

### 2.1 Create Web Service

1. Go to [render.com](https://render.com) and sign in
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Select the `AmateurHour_Flask_Site` repository

### 2.2 Configure the Service

**Basic Settings:**
- **Name:** `amateurhour-coaching` (or your preferred name)
- **Region:** Choose closest to your users
- **Branch:** `main`
- **Root Directory:** Leave blank (if repo root) or set to project folder
- **Runtime:** `Python 3`

**Build Settings:**
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn wsgi:app`

### 2.3 Add Environment Variables

Click **"Advanced"** and add these environment variables:

| Key | Value | Notes |
|-----|-------|-------|
| `PYTHON_VERSION` | `3.10.0` | Python version |
| `SECRET_KEY` | `your-random-secret-key-here` | Generate a strong random key |
| `FLASK_DEBUG` | `False` | IMPORTANT: Set to False for production |

**Optional - For Contact Form Email:**
| Key | Value |
|-----|-------|
| `MAIL_SERVER` | `smtp.gmail.com` |
| `MAIL_PORT` | `587` |
| `MAIL_USE_TLS` | `True` |
| `MAIL_USERNAME` | `your-email@gmail.com` |
| `MAIL_PASSWORD` | `your-app-password` |
| `MAIL_DEFAULT_SENDER` | `noreply@amateurhourcoaching.com` |

### 2.4 Deploy

1. Click **"Create Web Service"**
2. Render will automatically build and deploy
3. Wait for build to complete (usually 2-5 minutes)
4. Your site will be live at: `https://amateurhour-coaching.onrender.com`

## Step 3: Add Gunicorn

Add gunicorn to requirements.txt if not already there:

```txt
Flask==3.0.0
Flask-Mail==0.9.1
python-dotenv==1.0.0
Werkzeug==3.0.1
blinker==1.7.0
gunicorn==21.2.0
```

## Step 4: Verify Deployment

Visit your Render URL and test:
- ✅ Homepage loads
- ✅ All navigation works
- ✅ Images display
- ✅ All pages accessible
- ✅ Contact form (if email configured)

## Custom Domain Setup (Optional)

### On Render:
1. Go to your service → **Settings**
2. Scroll to **Custom Domain**
3. Click **Add Custom Domain**
4. Enter your domain: `www.amateurhourcoaching.com`

### On Your Domain Registrar:
Add these DNS records:

**For www.amateurhourcoaching.com:**
- Type: `CNAME`
- Name: `www`
- Value: `amateurhour-coaching.onrender.com`

**For root domain (optional):**
- Type: `A`
- Name: `@`
- Value: Get from Render dashboard

**Wait 24-48 hours for DNS propagation**

## Troubleshooting

### Build Fails
- Check `requirements.txt` is correct
- Verify Python version compatibility
- Check build logs in Render dashboard

### Site Won't Load
- Check Start Command is correct: `gunicorn wsgi:app`
- Verify `wsgi.py` exists
- Check environment variables are set

### Images Not Loading
- Ensure images are in `static/images/` folder
- Check file paths in templates
- Verify images are committed to Git

### Contact Form Not Working
- Email variables must be set in environment
- Use Gmail App Password (not regular password)
- Check Render logs for errors

## Free Tier Limitations

Render free tier:
- ✅ SSL certificate included
- ✅ Custom domain support
- ⚠️ Spins down after 15 min of inactivity
- ⚠️ 750 hours/month (enough for one site)
- ⚠️ First load after sleep takes ~30 seconds

To avoid spin-down, upgrade to paid tier ($7/month).

## Updating the Site

```bash
# Make your changes locally
# Test locally first

# Commit changes
git add .
git commit -m "Update: description of changes"

# Push to GitHub
git push origin main

# Render auto-deploys from GitHub!
```

## Support

- Render Docs: https://render.com/docs
- Render Community: https://community.render.com
- GitHub Issues: Create in your repository

---

**Website built by FrostPalm Technologies LLC**

