# Professional Mobile App Guide

## 📱 Running CareerSafe on Android

We have converted your CareerSafe web application into a professional Hybrid Mobile App using **Capacitor**. This allows you to open it in **Android Studio** and run it on an emulator or a real device.

### 1. Prerequisites
- **Android Studio**: Ensure you have Android Studio installed.
- **Node.js**: You already have this.

### 2. Open Project in Android Studio
1. Open **Android Studio**.
2. Select **Open**.
3. Navigate to: `c:\Users\srini\OneDrive\Desktop\careersafefinal\frontend\android`
4. Click **OK**. Android Studio will load the project and sync Gradle files.

### 3. Running the Backend
Since the app runs on your phone/emulator, it needs to reach your backend server.
1. Open your terminal in VS Code.
2. Run: `npm run backend` to start the python server.
3. The app is configured to look for the backend at:
   - `http://10.0.2.2:5000` (for Android Emulator)
   - `http://127.0.0.1:5000` (for Local Web)

### 4. Running the App
1. In Android Studio, wait for indexing to finish.
2. Select an **Emulator** (e.g., Pixel 4 API 30) or connect your physical Android device.
3. Click the green **Run (Play)** button.
4. The app should launch!

### Note on "Production"
- Currently, the app connects to your local computer's backend.
- For a real public app, you would host the Python backend on a server (like Render, AWS, or Heroku) and update `frontend/assets/config.js` with the real URL.

### Troubleshooting
- **API Error**: If the app says "Network Error", ensure `npm run backend` is running.
- **Emulator**: If using Emulator, `10.0.2.2` is the magic IP that points to your computer's localhost.
