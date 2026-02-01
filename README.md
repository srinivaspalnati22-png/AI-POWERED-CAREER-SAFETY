# CareerSafe - AI-Powered Career Safety Platform

An AI-powered platform to detect job scams, verify companies, check resumes, and provide career guidance. Now available as a **Web App** and **Android App**.

---

## 📦 Quick Start

### 1. Install Dependencies
```bash
npm install
```

### 2. Install Python Dependencies
```bash
pip install flask flask-cors pymupdf openai
```

### 3. Run the Application
```bash
npm start
```

This will start both:
- **Backend (Flask)**: `http://127.0.0.1:5000`
- **Frontend (Vite)**: `http://localhost:5173`

---

## 🏗️ Project Structure (Flattened)

```
careersafefinal/
├── app.py                  # Flask backend (main server)
├── index.html             # Homepage
├── dashboard.html         # User dashboard
├── login.html            # Login page
├── features.html         # Features showcase
├── analyze.html          # Job analysis tool
├── resume.html           # Resume checker
├── assets/               # CSS, JS, images
├── android/              # Android Studio project (Capacitor)
├── dist/                 # Build output (generated)
├── vite.config.js        # Vite configuration
├── capacitor.config.json # Mobile app config
└── package.json          # Node.js dependencies
```

---

## 🚀 Features

1. **Job Scam Detection**: Analyze job postings for scam indicators
2. **Company Verification**: Verify company legitimacy
3. **Resume Authenticity**: Check resume for red flags
4. **AI Career Guidance**: Get personalized career advice
5. **Mobile App**: Run on Android via Capacitor

---

## 📱 Android App

### Build for Android
```bash
npm run build
npx cap sync android
npx cap open android
```

Then in **Android Studio**, click the **Run** button to install on your emulator/device.

---

## 🛠️ Development

- **Backend only**: `npm run backend`
- **Frontend only**: `npm run frontend`
- **Build for production**: `npm run build`

---

## 🔑 API Key Setup

To enable AI features, add your OpenAI API key in `app.py`:
```python
openai.api_key = "your-key-here"
```

---

## 📝 License

MIT License - Feel free to use and modify.
