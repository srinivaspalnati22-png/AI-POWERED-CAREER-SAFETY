const CONFIG = {
    // Automatically detect the base URL. If running locally, it uses localhost. 
    // If deployed, it uses the deployment URL.
    API_BASE: (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')
        ? 'http://127.0.0.1:5000'
        : window.location.origin,
};

// Check if running in a mobile environment
const isMobileApp = window.Capacitor !== undefined;

if (isMobileApp) {
    console.log("Running in Mobile App Mode");
    // If testing on a physical mobile device, replace this with your computer's IP address
    // e.g., 'http://192.168.1.5:5000'
    // For local emulator testing:
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        CONFIG.API_BASE = 'http://10.0.2.2:5000';
    }
}

