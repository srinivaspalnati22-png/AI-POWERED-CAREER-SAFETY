const CONFIG = {
    // Automatically detect the base URL. If running locally, it uses localhost. 
    // If deployed, it uses the deployment URL.
    API_BASE: (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')
        ? 'http://127.0.0.1:5005'
        : window.location.origin,
};

// Check if running in a mobile environment
const isMobileApp = window.Capacitor !== undefined;

if (isMobileApp) {
    console.log("Running in Mobile App Mode");
    // Updated to use the computer's actual local IP so physical devices on Wi-Fi can connect
    CONFIG.API_BASE = 'http://10.46.65.81:5005';
}

