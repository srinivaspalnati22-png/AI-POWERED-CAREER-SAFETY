# CareerSafe - AI-Powered Career Safety Platform

A comprehensive web application that uses artificial intelligence to detect job scams, verify companies, check resume authenticity, and provide career guidance.

## 🚀 Features

### Core Features
- **🔍 Job Scam Detection**: AI-powered analysis of job postings and messages to identify fraudulent opportunities
- **🏢 Company Verification**: Cross-verify company legitimacy through multiple data sources
- **📄 Resume Authenticity Check**: Detect exaggerated skills, unverifiable experience, and potential fraud
- **🤖 AI Career Guidance**: Get personalized career recommendations based on your skills
- **📊 Real-time Dashboard**: Track your analyses, statistics, and activity history
- **📥 Export Results**: Download analysis reports in JSON format

### Additional Features
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Demo Mode**: Works offline with fallback demo functionality
- **Activity History**: Track all your analyses and verifications
- **Quick Test Buttons**: Pre-loaded test data for easy testing
- **Real-time Notifications**: Instant feedback on all actions
- **Modern UI**: Beautiful glassmorphism design with smooth animations

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🛠️ Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd careersafefinal
   ```

2. **Install backend dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Configure OpenAI API (Optional)**
   - Open `backend/app.py`
   - Replace `"PASTE_YOUR_OPENAI_API_KEY_HERE"` with your OpenAI API key
   - Note: The app works without API key using rule-based analysis

## 🚀 Running the Application

### Start the Backend Server

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Run the Flask server**
   ```bash
   python app.py
   ```

   The server will start on `http://127.0.0.1:5000`

### Access the Frontend

1. **Open the frontend files**
   - Simply open `frontend/index.html` in your web browser
   - Or use a local server (recommended):
     ```bash
     # Using Python
     cd frontend
     python -m http.server 8000
     ```
     Then visit `http://localhost:8000`

2. **Note**: The app works in demo mode even without the backend running!

## 📖 Usage Guide

### 1. **Job Risk Analysis**
- Navigate to "Analyze" page
- Paste job offer text or message
- Click "Analyze Risk" or use quick test buttons
- View risk percentage, reasons, and safety tips
- Export results if needed

### 2. **Company Verification**
- On "Analyze" page, scroll to Company Verification section
- Enter company name
- Click "Verify" or use test buttons (Google, Microsoft, Fake)
- View verification status and risk assessment

### 3. **Resume Check**
- Navigate to "Resume Check" page
- Drag & drop or select a PDF resume
- Click "Analyze Resume"
- Or use quick test buttons for demo results
- View authenticity analysis and recommendations

### 4. **Career Guidance**
- On "Analyze" page, scroll to AI Career Guidance section
- Enter a skill (e.g., python, design, security)
- Click "Get Suggestions"
- View career recommendations with salary ranges

### 5. **Dashboard**
- Login to access dashboard
- View statistics and activity overview
- See charts and recent activity
- Access quick actions

## 🎯 Quick Test Features

All pages include quick test buttons with pre-loaded data:
- **Job Analysis**: Test with scam, legitimate, or suspicious examples
- **Company Verification**: Test with Google, Microsoft, or fake companies
- **Resume Check**: Test with authentic, suspicious, or high-risk resumes
- **Career Guidance**: Test with python, design, security, or javascript

## 🔧 Technical Details

### Backend (Flask)
- **Framework**: Flask with CORS support
- **PDF Processing**: PyMuPDF (fitz)
- **AI Integration**: OpenAI API (optional)
- **Endpoints**:
  - `/analyze` - Job risk analysis
  - `/verify-company` - Company verification
  - `/resume-check` - Resume authenticity check
  - `/career-guidance` - Career recommendations
  - `/health` - Health check
  - `/bulk-analyze` - Bulk analysis
  - `/dashboard-stats` - Dashboard statistics

### Frontend
- **Framework**: Vanilla JavaScript
- **Styling**: Tailwind CSS
- **Charts**: Chart.js
- **Storage**: LocalStorage for history and stats
- **Responsive**: Mobile-first design

## 📱 Responsive Design

The application is fully responsive and works on:
- 📱 Mobile phones (320px+)
- 📱 Tablets (768px+)
- 💻 Laptops (1024px+)
- 🖥️ Desktops (1280px+)

## 🎨 UI Features

- **Glassmorphism Design**: Modern glass-like UI elements
- **Smooth Animations**: Fade-up and hover effects
- **Color-coded Risk Levels**: 
  - 🔴 High Risk (70%+)
  - 🟡 Medium Risk (30-69%)
  - 🟢 Low Risk (<30%)
- **Interactive Charts**: Visual representation of data
- **Real-time Updates**: Instant feedback and notifications

## 🔒 Security & Privacy

- All analysis is performed locally or on your server
- No data is sent to third parties (except optional OpenAI API)
- History stored in browser localStorage
- No user registration required for demo mode

## 🐛 Troubleshooting

### Backend not starting
- Check if Python is installed: `python --version`
- Install dependencies: `pip install -r requirements.txt`
- Check if port 5000 is available

### Frontend not loading
- Ensure you're opening from a web server (not file://)
- Check browser console for errors
- The app works in demo mode without backend

### PDF upload not working
- Ensure file is a valid PDF
- Check file size (should be reasonable)
- Backend must be running for actual PDF processing

## 📝 Default Test Data

The application includes default test data for easy testing:
- **Job Offers**: Scam, legitimate, and suspicious examples
- **Companies**: Google, Microsoft, and fake company examples
- **Resumes**: Authentic, suspicious, and high-risk examples
- **Skills**: Python, design, security, JavaScript examples

## 🚀 Future Enhancements

- Database integration for persistent storage
- User authentication system
- Email notifications
- Advanced AI models
- Multi-language support
- API rate limiting
- Report generation (PDF)

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests.

## 📧 Support

For issues or questions, please check the troubleshooting section or create an issue in the repository.

---

**Made with ❤️ for Career Safety**

