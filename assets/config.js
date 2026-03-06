// ============================================================
// CareerSafe - API Configuration
// ============================================================

const CONFIG = {
    API_BASE: (function () {
        const host = window.location.hostname;

        // Local development
        if (host === 'localhost' || host === '127.0.0.1') {
            return 'http://127.0.0.1:5000';
        }

        // Vercel deployment — both frontend & backend share the same domain!
        return '';
    })()
};

console.log('[CareerSafe] API Base configured successfully');
