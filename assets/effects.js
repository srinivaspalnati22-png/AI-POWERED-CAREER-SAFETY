// Enhanced Effects and Utilities (Optimized for performance)
// Use requestIdleCallback for non-critical operations
const runWhenIdle = window.requestIdleCallback || ((cb) => setTimeout(cb, 1));

// Initialize immediately if DOM is ready, otherwise wait
(function initEffects() {
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        // DOM already loaded
        setTimeout(init, 0);
    }
    
    function init() {
        // Critical: Initialize notifications immediately
        initNotifications();
        
        // Non-critical: Run animations when idle
        runWhenIdle(() => {
            // Fade-up animations with delay
            document.querySelectorAll(".fade-up").forEach((el, i) => {
                el.style.animationDelay = `${i * 0.15}s`;
            });
            
            // Initialize tooltips (non-critical)
            initTooltips();
        });
        
        // Check authentication status (critical)
        checkAuth();
    }
})();

// Authentication check
function checkAuth() {
    const isLoggedIn = localStorage.getItem('careersafe_user');
    const currentPage = window.location.pathname;
    
    if (isLoggedIn && currentPage.includes('login.html')) {
        window.location.href = 'index.html';
    }
}

// Show notification
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `fixed top-4 right-4 z-50 p-4 rounded-lg shadow-lg notification transform transition-all ${
        type === 'success' ? 'bg-green-500' : 
        type === 'error' ? 'bg-red-500' : 
        type === 'info' ? 'bg-blue-500' :
        'bg-gray-500'
    } text-white max-w-sm`;
    
    // Add icon based on type
    const icons = {
        'success': '✓',
        'error': '✗',
        'info': 'ℹ'
    };
    
    notification.innerHTML = `
        <div class="flex items-center gap-2">
            <span class="text-xl">${icons[type] || '•'}</span>
            <span>${message}</span>
        </div>
    `;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 10);
    
    setTimeout(() => {
        notification.style.opacity = '0';
        notification.style.transform = 'translateX(100%)';
        notification.style.transition = 'opacity 0.3s, transform 0.3s';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Initialize notifications system
function initNotifications() {
    window.showNotification = showNotification;
}

// Initialize tooltips
function initTooltips() {
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    tooltipElements.forEach(el => {
        el.addEventListener('mouseenter', showTooltip);
        el.addEventListener('mouseleave', hideTooltip);
    });
}

function showTooltip(e) {
    const text = e.target.getAttribute('data-tooltip');
    const tooltip = document.createElement('div');
    tooltip.className = 'absolute bg-gray-900 text-white text-xs rounded py-1 px-2 z-50';
    tooltip.textContent = text;
    tooltip.id = 'tooltip';
    document.body.appendChild(tooltip);
    
    const rect = e.target.getBoundingClientRect();
    tooltip.style.top = `${rect.top - 30}px`;
    tooltip.style.left = `${rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2)}px`;
}

function hideTooltip() {
    const tooltip = document.getElementById('tooltip');
    if (tooltip) tooltip.remove();
}

// Loading state management
function setLoading(element, isLoading) {
    if (isLoading) {
        element.disabled = true;
        element.innerHTML = '<div class="spinner"></div>';
    } else {
        element.disabled = false;
    }
}

// Format date
function formatDate(date) {
    return new Date(date).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// Export utilities
window.careersafeUtils = {
    showNotification,
    setLoading,
    formatDate,
    checkAuth
};