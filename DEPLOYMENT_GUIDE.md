# 🚀 Complete Deployment Guide - CareerSafe

Complete step-by-step guide to deploy the AI-Powered Career Safety platform with all features working.

---

## 📋 Pre-Deployment Checklist

- [ ] Python 3.8+ installed
- [ ] Node.js & npm installed
- [ ] Git installed
- [ ] Gemini API key obtained (https://ai.google.dev/)
- [ ] 2GB+ free disk space
- [ ] Internet connection

---

## 🔧 Local Development Setup

### Step 1: Clone and Navigate to Project

```bash
# Clone the repository
git clone https://github.com/srinivaspalnati22-png/AI-POWERED-CAREER-SAFETY.git
cd AI-POWERED-CAREER-SAFETY
```

### Step 2: Install Node.js Dependencies

```bash
npm install
```

**Expected output:**
```
added X packages in Y seconds
```

### Step 3: Install Python Dependencies

Create and activate virtual environment (recommended):

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

**Required packages:**
- flask
- flask-cors
- PyPDF2
- google-generativeai
- gunicorn

### Step 4: Configure Environment Variables

Create `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` with your settings:

```env
# REQUIRED - Get from https://ai.google.dev/
GEMINI_API_KEY=your_actual_gemini_api_key_here

# Server Configuration
PORT=5000
DEBUG=False

# Security
CORS_ORIGINS=http://localhost:5000,http://localhost:5173
```

### Step 5: Verify Setup

Test both components separately:

```bash
# Test backend
npm run backend

# In a new terminal, test frontend
npm run frontend
```

**Backend** should show:
```
* Running on http://127.0.0.1:5000
```

**Frontend** should show:
```
Local:   http://localhost:5173
```

---

## 🎯 Running the Project Locally

### Option A: Start Everything Together

```bash
npm start
```

This runs both backend (Flask) and frontend (Vite) concurrently:
- **Backend**: `http://localhost:5000`
- **Frontend**: `http://localhost:5173`

### Option B: Start Separately (Debugging)

Terminal 1 - Backend:
```bash
npm run backend
```

Terminal 2 - Frontend:
```bash
npm run frontend
```

### Access the Application

Open browser and go to:
- **Main Site**: `http://localhost:5173` (or `http://localhost:5000`)
- **Features**: http://localhost:5173/features.html
- **Job Analysis**: http://localhost:5173/analyze.html
- **Resume Check**: http://localhost:5173/resume.html
- **Dashboard**: http://localhost:5173/dashboard.html

---

## ✨ Features Activation Checklist

### ✅ Feature 1: Job Scam Detection
**File**: `analyze.html`
- Opens at `/analyze.html`
- Requires: Backend running + Gemini API key
- **Test it**:
  1. Navigate to Analyze tab
  2. Paste a job posting
  3. Click "Analyze Job"
  4. AI analyzes for scam indicators

### ✅ Feature 2: Company Verification
**File**: `analyze.html` (integrated)
- Checks company legitimacy
- Requires: Backend + API key
- **Test it**:
  1. In Analyze tab
  2. Enter company name
  3. Check verification status

### ✅ Feature 3: Resume Authenticity Check
**File**: `resume.html`
- Opens at `/resume.html`
- Requires: Backend + PyPDF2 + Gemini API
- **Test it**:
  1. Navigate to Resume tab
  2. Upload PDF resume
  3. Get AI feedback on authenticity

### ✅ Feature 4: AI Career Guidance
**File**: `dashboard.html`
- Interactive chat interface
- Requires: Backend + Gemini API
- **Test it**:
  1. Go to Dashboard
  2. Type career question
  3. Get personalized guidance

### ✅ Feature 5: Enhanced Loading Animation
**File**: `assets/splash.js`, `assets/main.css`
- Auto-plays when page loads
- Requires: No API key
- **Test it**:
  1. Refresh any page
  2. Watch 2.5-3.5 second animation
  3. Features: particles, glow, progress bar

---

## 📦 Production Deployment

### Option 1: Deploy to Render (Recommended)

**Advantages**: Free tier available, easy setup, auto-deploys from GitHub

**Steps**:

1. **Connect GitHub**:
   - Go to [render.com](https://render.com)
   - Sign up with GitHub
   - Select this repository

2. **Configure Service**:
   ```
   Name: careersafe
   Environment: Node
   Build Command: npm install && pip install -r requirements.txt
   Start Command: npm start
   ```

3. **Add Environment Variable**:
   - Go to Settings → Environment
   - Add: `GEMINI_API_KEY=your_key_here`

4. **Deploy**:
   - Click Deploy
   - Wait 2-3 minutes
   - Access at: `https://careersafe.onrender.com`

**File**: `render.yaml` (already configured)

### Option 2: Deploy to Vercel (Frontend Only)

**Advantages**: Fast CDN, best for static files

**Steps**:

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Deploy:
```bash
vercel
```

3. Configure:
   - Select project
   - Add `GEMINI_API_KEY` in Environment Variables
   - Deploy frontend

**Note**: Backend must be on separate service (Render, Heroku, etc.)

**File**: `vercel.json` (already configured)

### Option 3: Deploy to Heroku

**Steps**:

1. Install Heroku CLI

2. Login:
```bash
heroku login
```

3. Create app:
```bash
heroku create careersafe
```

4. Add config:
```bash
heroku config:set GEMINI_API_KEY=your_key_here
```

5. Deploy:
```bash
git push heroku main
```

**File**: `Procfile` (already configured for Heroku)

---

## 🔐 Security Checklist

### Environment Variables
- [ ] Never commit `.env` to GitHub
- [ ] `.gitignore` includes `.env`
- [ ] Use secrets manager in production
- [ ] Rotate API keys regularly

### CORS Configuration
Update in `app.py` for production:

```python
CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:5000').split(',')
```

Set environment variable:
```
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

### API Key Security
- [ ] Never log API keys
- [ ] Use environment variables only
- [ ] Restrict API key permissions in Google Cloud
- [ ] Enable API quotas/limits

---

## 🧪 Testing All Features

### 1. Test Job Analysis
```bash
curl -X POST http://localhost:5000/api/analyze-job \
  -H "Content-Type: application/json" \
  -d '{"job_posting": "Work from home, earn $5000/week..."}'
```

### 2. Test Resume Upload
```bash
# Upload resume.pdf
curl -F "file=@resume.pdf" http://localhost:5000/api/check-resume
```

### 3. Test Company Verification
```bash
curl -X POST http://localhost:5000/api/verify-company \
  -H "Content-Type: application/json" \
  -d '{"company_name": "Google"}'
```

### 4. Test Career Chat
```bash
curl -X POST http://localhost:5000/api/career-guidance \
  -H "Content-Type: application/json" \
  -d '{"question": "How to become a software engineer?"}'
```

---

## 📱 Mobile App Deployment (Android)

### Prerequisites
- Android Studio installed
- Java SDK 11+
- Android SDK Tools

### Build for Android

```bash
# Build production bundle
npm run build

# Sync with Capacitor
npx cap sync android

# Open Android Studio
npx cap open android
```

### In Android Studio
1. Connect Android device or start emulator
2. Click "Run" button
3. Select target device
4. Wait for build (5-10 minutes)
5. App installs and launches

---

## 🐛 Troubleshooting

### Issue: "Gemini API Error"
**Solution**:
```bash
# Verify API key
echo $GEMINI_API_KEY  # Should show your key

# Test API directly
python -c "import google.generativeai; print('OK')"
```

### Issue: "Port 5000 already in use"
**Solution**:
```bash
# Change port
PORT=5001 npm run backend

# Or kill process using port 5000
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -i :5000
kill -9 <PID>
```

### Issue: "Module not found"
**Solution**:
```bash
# Reinstall all dependencies
rm -rf node_modules package-lock.json
npm install

# Reinstall Python packages
pip install --upgrade -r requirements.txt
```

### Issue: "CORS error"
**Solution**:
1. Check backend is running
2. Verify CORS_ORIGINS in `.env`
3. Clear browser cache (Ctrl+Shift+Delete)
4. Try incognito mode

### Issue: "Loading animation doesn't show"
**Solution**:
1. Check `assets/splash.js` exists
2. Hard refresh (Ctrl+Shift+R)
3. Check browser console (F12)
4. Verify `index.html` includes script tag

---

## 📊 Monitoring & Logging

### Development Logs
```bash
# Backend logs (in terminal)
npm run backend
# Shows all Flask errors and requests

# Frontend logs (browser console)
# F12 → Console tab
```

### Production Logs
**On Render**:
- Go to Dashboard
- Click on service
- View Logs tab

**On Vercel**:
- Go to Projects
- Select project
- View Deployments → Logs

---

## 🚀 Performance Optimization

### Frontend
```bash
# Production build
npm run build

# Analyze bundle
# Check dist/ folder for optimized files
```

### Backend
```python
# In app.py, set for production:
app.config['DEBUG'] = False
app.config['COMPRESS_GZIP'] = True
```

---

## 📞 Support & Resources

### Official Links
- **Gemini API Docs**: https://ai.google.dev/docs
- **Flask Docs**: https://flask.palletsprojects.com
- **Vite Docs**: https://vitejs.dev
- **Render Docs**: https://render.com/docs

### GitHub Issues
For bugs/features: https://github.com/srinivaspalnati22-png/AI-POWERED-CAREER-SAFETY/issues

---

## ✅ Deployment Verification Checklist

After deployment, verify:

- [ ] Homepage loads with animation
- [ ] Navigation menu works
- [ ] Job Analysis feature works
- [ ] Resume upload accepts PDF
- [ ] Chat responds with AI guidance
- [ ] No CORS errors in console
- [ ] Page loads in <3 seconds
- [ ] Mobile responsive design works
- [ ] Animations are smooth
- [ ] API key is secure (not in code)

---

## 🎯 What's Next?

1. **Custom Domain**: Add domain to Render/Vercel
2. **SSL Certificate**: Auto-enabled on Render
3. **Analytics**: Add Google Analytics
4. **Monitoring**: Set up error tracking
5. **Backup**: Configure database backups

---

**Congratulations! Your CareerSafe platform is ready for production! 🎉**
