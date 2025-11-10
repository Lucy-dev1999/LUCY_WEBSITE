# Deploy Your Portfolio to Render.com - Complete Guide

## Prerequisites
- GitHub account
- Render account (sign up at https://render.com)
- Your Django project ready

---

## Step 1: Prepare Your Project for Deployment

### 1.1 Update Email Settings for Production
Open `website/local_settings.py` and update with your Gmail App Password:
```python
EMAIL_HOST_PASSWORD = 'your-actual-16-char-password'
```

### 1.2 Create a .gitignore file (if not exists)
Make sure `website/.gitignore` includes:
```
*.pyc
__pycache__/
db.sqlite3
*.log
website/local_settings.py
staticfiles/
venv/
env/
.vscode/
.idea/
```

---

## Step 2: Push Your Code to GitHub

### 2.1 Initialize Git (if not already done)
```bash
cd website
git init
git add .
git commit -m "Initial commit - Portfolio website"
```

### 2.2 Create a GitHub Repository
1. Go to https://github.com/new
2. Name it: `portfolio-website`
3. Don't initialize with README (you already have code)
4. Click "Create repository"

### 2.3 Push to GitHub
```bash
git remote add origin https://github.com/YOUR-USERNAME/portfolio-website.git
git branch -M main
git push -u origin main
```

---

## Step 3: Deploy on Render

### 3.1 Create a New Web Service
1. Go to https://dashboard.render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub account
4. Select your `portfolio-website` repository

### 3.2 Configure the Web Service

**Basic Settings:**
- **Name**: `lucia-portfolio` (or your preferred name)
- **Region**: Choose closest to you
- **Branch**: `main`
- **Root Directory**: `website`
- **Runtime**: `Python 3`
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn website.wsgi:application`

**Instance Type:**
- Select: **Free**

### 3.3 Add Environment Variables
Click "Advanced" and add these environment variables:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11.0` |
| `SECRET_KEY` | Generate a new one at https://djecrety.ir/ |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `lucia-portfolio.onrender.com` (use your actual Render URL) |
| `EMAIL_HOST_USER` | `ainembabaziliciarachel02@gmail.com` |
| `EMAIL_HOST_PASSWORD` | Your Gmail App Password (16 chars, no spaces) |

### 3.4 Create PostgreSQL Database (Optional but Recommended)
1. In Render Dashboard, click "New +" → "PostgreSQL"
2. Name: `lucia-portfolio-db`
3. Select **Free** tier
4. Click "Create Database"
5. Copy the **Internal Database URL**
6. Go back to your Web Service → Environment
7. Add: `DATABASE_URL` = (paste the Internal Database URL)

### 3.5 Deploy!
1. Click "Create Web Service"
2. Wait 5-10 minutes for deployment
3. Your site will be live at: `https://lucia-portfolio.onrender.com`

---

## Step 4: Update Settings After First Deploy

### 4.1 Update ALLOWED_HOSTS
After deployment, go to Environment Variables and update:
```
ALLOWED_HOSTS = your-app-name.onrender.com
```

### 4.2 Update CSRF Settings
Add to your Render environment variables:
```
CSRF_TRUSTED_ORIGINS = https://your-app-name.onrender.com
```

---

## Step 5: Add Custom Domain (Optional)

### 5.1 In Render Dashboard
1. Go to your Web Service
2. Click "Settings" → "Custom Domain"
3. Click "Add Custom Domain"
4. Enter your domain (e.g., `luciarachel.com`)

### 5.2 Update DNS Settings
In your domain registrar (Namecheap, GoDaddy, etc.):
- Add a CNAME record pointing to your Render URL

### 5.3 Update Environment Variables
```
ALLOWED_HOSTS = luciarachel.com,your-app-name.onrender.com
```

---

## Step 6: Test Your Deployed Site

### 6.1 Check These Features:
- ✅ Home page loads
- ✅ Navigation works (smooth scrolling)
- ✅ About section displays
- ✅ Projects section shows
- ✅ Experience section visible
- ✅ Contact form works (send a test email)
- ✅ CV download button works
- ✅ Social media links work

---

## Troubleshooting

### Issue: Site shows "Application Error"
**Solution**: Check the logs in Render Dashboard → Logs tab

### Issue: Static files not loading (no CSS)
**Solution**: 
1. Check build logs for `collectstatic` errors
2. Verify `STATIC_ROOT` in settings.py
3. Run manual deploy

### Issue: Contact form not sending emails
**Solution**:
1. Verify `EMAIL_HOST_PASSWORD` is correct (no spaces)
2. Check Gmail App Password is valid
3. Ensure 2-Step Verification is enabled on Gmail

### Issue: Database errors
**Solution**:
1. Check `DATABASE_URL` is set correctly
2. Verify PostgreSQL database is running
3. Check migrations ran successfully in build logs

---

## Updating Your Site

### After Making Changes:
```bash
git add .
git commit -m "Description of changes"
git push origin main
```

Render will automatically detect the push and redeploy!

---

## Important Notes

⚠️ **Free Tier Limitations:**
- Site spins down after 15 minutes of inactivity
- Takes ~30 seconds to wake up on first visit
- 750 hours/month (enough for most portfolios)

✅ **Advantages:**
- Automatic HTTPS/SSL
- Custom domain support (free)
- Auto-deploy from GitHub
- Contact form works (can send emails)

---

## Your Live URLs

After deployment, your portfolio will be available at:
- **Render URL**: `https://your-app-name.onrender.com`
- **Custom Domain** (if added): `https://yourdomain.com`

---

## Need Help?

- Render Docs: https://render.com/docs
- Django Deployment: https://docs.djangoproject.com/en/5.1/howto/deployment/
- Check Render logs for errors

---

**Congratulations! Your portfolio is now live! 🎉**

Share your link:
- On LinkedIn
- In your CV
- With potential employers
- On your GitHub profile
