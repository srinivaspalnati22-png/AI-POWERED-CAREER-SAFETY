// ============================================================
// CareerSafe - API Configuration
// ============================================================
// IMPORTANT: After deploying the backend to Render.com,
// replace RENDER_BACKEND_URL with your actual Render URL.
// Example: 'https://careersafe-backend.onrender.com'
// ============================================================

const RENDER_BACKEND_URL = 'https://careersafe-backend.onrender.com'; // <-- UPDATE THIS

const CONFIG = {
    API_BASE: (function () {
        const host = window.location.hostname;

        // Local development
        if (host === 'localhost' || host === '127.0.0.1') {
            return 'http://127.0.0.1:5000';
        }

        // Vercel / any other deployment — use Render backend
        return RENDER_BACKEND_URL;
    })()
};

console.log('[CareerSafe] API Base:', CONFIG.API_BASE);
