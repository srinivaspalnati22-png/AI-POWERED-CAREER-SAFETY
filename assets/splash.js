/**
 * CareerSafe - Enhanced Video Splash Screen Animation
 * Premium entrance animation with advanced visual effects
 */

// Splash screen configuration
const SPLASH_CONFIG = {
    minDuration: 2500, // Minimum display time (2.5 seconds)
    maxDuration: 3500, // Maximum display time (3.5 seconds)
    videoUrl: 'https://assets.mixkit.co/videos/preview/mixkit-cyber-security-and-digital-data-processing-40173-large.mp4',
    fallbackUrl: 'https://cdn.pixabay.com/video/2021/04/12/70860-536967733_large.mp4',
    enableParticles: true,
    particleCount: 120, // Increased for more impressive visual effect
    enableGlowEffects: true,
    enableAdvancedEffects: true // New: Enhanced visual effects
};

class ParticleEffect {
    constructor(container) {
        this.container = container;
        this.particles = [];
        this.animationId = null;
        this.time = 0;
        this.attractors = []; // Attraction points for particles
        this.createParticles();
        this.createAttractors();
    }

    createAttractors() {
        // Create multiple attraction points for dynamic particle movement
        this.attractors = [
            { x: window.innerWidth / 2, y: window.innerHeight / 2, strength: 0.3 }, // Center
            { x: window.innerWidth * 0.3, y: window.innerHeight * 0.3, strength: 0.15 }, // Top-left
            { x: window.innerWidth * 0.7, y: window.innerHeight * 0.3, strength: 0.15 }, // Top-right
            { x: window.innerWidth * 0.5, y: window.innerHeight * 0.8, strength: 0.2 } // Bottom
        ];
    }

    createParticles() {
        const container = this.container;
        if (!container) return;

        const colors = ['#06b6d4', '#3b82f6', '#6366f1', '#4f46e5', '#0ea5e9', '#ec4899', '#f97316', '#14b8a6', '#8b5cf6'];

        for (let i = 0; i < SPLASH_CONFIG.particleCount; i++) {
            const angle = (Math.PI * 2 * i) / SPLASH_CONFIG.particleCount;
            const distance = Math.random() * 250 + 150;

            this.particles.push({
                x: window.innerWidth / 2 + Math.cos(angle) * distance,
                y: window.innerHeight / 2 + Math.sin(angle) * distance,
                baseX: window.innerWidth / 2 + Math.cos(angle) * distance,
                baseY: window.innerHeight / 2 + Math.sin(angle) * distance,
                vx: (Math.random() - 0.5) * 5,
                vy: (Math.random() - 0.5) * 5,
                opacity: Math.random() * 0.8 + 0.2,
                size: Math.random() * 5 + 1,
                color: colors[Math.floor(Math.random() * colors.length)],
                life: 1,
                decay: Math.random() * 0.006 + 0.0015,
                pulse: Math.random() * Math.PI * 2,
                orbitRadius: Math.random() * 180 + 120,
                orbitSpeed: Math.random() * 0.025 + 0.008,
                trailOpacity: Math.random() * 0.4 + 0.1,
                trailLength: Math.floor(Math.random() * 10 + 5)
            });
        }
    }

    animate() {
        if (!this.container) return;
        const ctx = this.container.getContext('2d');
        if (!ctx) return;

        ctx.clearRect(0, 0, this.container.width, this.container.height);
        this.time++;

        // Animate each attractor
        this.attractors.forEach((attractor, idx) => {
            attractor.x = window.innerWidth / 2 + Math.cos(this.time * 0.005 + idx) * 100;
            attractor.y = window.innerHeight / 2 + Math.sin(this.time * 0.006 + idx) * 100;
        });

        this.particles.forEach((p, i) => {
            // Orbital movement with enhanced physics
            const orbitX = Math.cos(this.time * p.orbitSpeed) * p.orbitRadius;
            const orbitY = Math.sin(this.time * p.orbitSpeed) * p.orbitRadius;

            p.x = window.innerWidth / 2 + orbitX + p.vx;
            p.y = window.innerHeight / 2 + orbitY + p.vy;

            // Attraction force from attractors
            this.attractors.forEach(attractor => {
                const dx = attractor.x - p.x;
                const dy = attractor.y - p.y;
                const distance = Math.sqrt(dx * dx + dy * dy) + 1;
                const force = attractor.strength / (distance * 0.5);
                p.vx += (dx / distance) * force * 0.3;
                p.vy += (dy / distance) * force * 0.3;
            });

            // Random wandering
            p.vx += (Math.random() - 0.5) * 0.4;
            p.vy += (Math.random() - 0.5) * 0.4;

            // Speed limits with damping
            const speed = Math.sqrt(p.vx * p.vx + p.vy * p.vy);
            if (speed > 4) {
                p.vx = (p.vx / speed) * 4;
                p.vy = (p.vy / speed) * 4;
            }

            // Damping effect
            p.vx *= 0.95;
            p.vy *= 0.95;

            // Bounce at edges
            if (p.x < 0 || p.x > this.container.width) p.vx *= -1;
            if (p.y < 0 || p.y > this.container.height) p.vy *= -1;

            // Wrap around edges
            if (p.x < -50) p.x = this.container.width + 50;
            if (p.x > this.container.width + 50) p.x = -50;
            if (p.y < -50) p.y = this.container.height + 50;
            if (p.y > this.container.height + 50) p.y = -50;

            // Pulsing opacity with wave effect
            p.life -= p.decay;
            const pulseFactor = Math.sin(this.time * 0.06 + p.pulse) * 0.35 + 0.65;
            const waveEffect = Math.sin((this.time * 0.03 + i * 0.1)) * 0.2 + 0.8;
            p.opacity = Math.max(0, p.life * pulseFactor * waveEffect);

            // Draw particle with enhanced glow
            ctx.fillStyle = p.color;
            ctx.globalAlpha = p.opacity * 0.85;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            ctx.fill();

            // Inner bright core
            ctx.globalAlpha = p.opacity * 0.5;
            ctx.fillStyle = '#ffffff';
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size * 0.4, 0, Math.PI * 2);
            ctx.fill();

            // Outer glow halo
            ctx.globalAlpha = p.opacity * 0.2;
            ctx.fillStyle = p.color;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size * 4, 0, Math.PI * 2);
            ctx.fill();

            // Extended outer glow
            ctx.globalAlpha = p.opacity * 0.08;
            ctx.fillStyle = p.color;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size * 7, 0, Math.PI * 2);
            ctx.fill();
        });

        ctx.globalAlpha = 1;
        this.animationId = requestAnimationFrame(() => this.animate());
    }

    destroy() {
        if (this.animationId) cancelAnimationFrame(this.animationId);
        this.particles = [];
        this.attractors = [];
    }
}

class SplashScreen {
    constructor() {
        this.splashElement = document.getElementById('videoSplash');
        this.video = this.splashElement ? this.splashElement.querySelector('.splash-video') : null;
        this.startTime = Date.now();
        this.particleEffect = null;
        this.loadingStartTime = Date.now();
        this.init();
    }

    init() {
        if (!this.splashElement) {
            console.warn('Splash screen element not found');
            return;
        }

        // Handle video ready state
        if (this.video) {
            this.video.play().catch(err => {
                console.warn('Video autoplay failed:', err);
            });

            this.video.addEventListener('error', () => {
                console.warn('Primary video failed, attempting fallback...');
                this.video.src = SPLASH_CONFIG.fallbackUrl;
            });
        }

        // Create particle effect with enhanced visual
        if (SPLASH_CONFIG.enableParticles) {
            const canvas = this.splashElement.querySelector('.splash-particles');
            if (canvas) {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
                this.particleEffect = new ParticleEffect(canvas);
                this.particleEffect.animate();
            }
        }

        // Add glow effects to elements
        if (SPLASH_CONFIG.enableGlowEffects) {
            this.addGlowEffects();
        }

        // Add advanced effects if enabled
        if (SPLASH_CONFIG.enableAdvancedEffects) {
            this.addAdvancedEffects();
        }

        // Start animations
        this.animateElements();
        this.animateLoadPercentage();
        this.scheduleParticleBurst(); // New: Particle burst effect
        this.scheduleSplashDismissal();
        this.setupInteractionListeners();
    }

    addAdvancedEffects() {
        // Add pulsing glow to splash container
        const splashContent = this.splashElement.querySelector('.splash-content');
        if (splashContent) {
            splashContent.style.animation = 'contentPulseGlow 2s ease-in-out infinite';
        }

        // Add shimmer effect to text
        const splashText = this.splashElement.querySelector('.splash-text');
        if (splashText) {
            splashText.style.animation = 'shimmerFlow 3s ease-in-out infinite';
        }

        // Add bounce animation to dots
        const dots = this.splashElement.querySelectorAll('.dot');
        dots.forEach((dot, idx) => {
            dot.style.animation = `dotBounceAdvanced 0.8s ease-in-out ${idx * 0.15}s infinite`;
        });
    }

    scheduleParticleBurst() {
        // Create particle burst effects at timed intervals
        setInterval(() => {
            if (this.particleEffect && this.particleEffect.particles) {
                // Burst: Add velocity to random particles
                const burstCount = Math.floor(Math.random() * 15 + 8);
                for (let i = 0; i < burstCount; i++) {
                    const randomIdx = Math.floor(Math.random() * this.particleEffect.particles.length);
                    const p = this.particleEffect.particles[randomIdx];
                    if (p) {
                        const angle = Math.random() * Math.PI * 2;
                        const speed = Math.random() * 4 + 3;
                        p.vx = Math.cos(angle) * speed;
                        p.vy = Math.sin(angle) * speed;
                        p.opacity = 1;
                        p.life = 1;
                    }
                }
            }
        }, 800);
    }

    addGlowEffects() {
        const logo = this.splashElement.querySelector('.splash-logo');
        const title = this.splashElement.querySelector('.splash-title');
        const progressBar = this.splashElement.querySelector('.splash-progress-bar');

        if (logo) {
            logo.classList.add('logo-glow-effect');
            logo.style.textShadow = '0 0 20px rgba(6, 182, 212, 0.8), 0 0 40px rgba(59, 130, 246, 0.5), 0 0 60px rgba(99, 102, 241, 0.3)';
        }
        if (title) {
            title.classList.add('title-glow-effect');
            title.style.textShadow = '0 0 30px rgba(59, 130, 246, 0.7), 0 0 60px rgba(99, 102, 241, 0.4)';
        }
        if (progressBar) {
            progressBar.classList.add('progress-glow-effect');
            progressBar.style.boxShadow = '0 0 15px rgba(6, 182, 212, 0.8), inset 0 0 10px rgba(14, 165, 233, 0.6)';
        }
    }

    animateLoadPercentage() {
        const percentageElement = this.splashElement.querySelector('.splash-percentage');
        if (!percentageElement) return;

        let currentPercent = 0;
        const interval = setInterval(() => {
            // Faster initial progress, slower near end
            const remaining = 100 - currentPercent;
            const increment = Math.random() * (remaining * 0.25 + 3) + 5;
            currentPercent += increment;

            if (currentPercent >= 95) currentPercent = 95;

            percentageElement.textContent = Math.floor(currentPercent) + '%';

            if (currentPercent >= 95) {
                clearInterval(interval);
                setTimeout(() => {
                    percentageElement.textContent = '100%';
                }, 600);
            }
        }, 180);
    }

    animateElements() {
        // Elements animate with delays defined in CSS
        const logoContainer = this.splashElement.querySelector('.splash-logo-container');
        const title = this.splashElement.querySelector('.splash-title');
        const tagline = this.splashElement.querySelector('.splash-tagline');
        const progressContainer = this.splashElement.querySelector('.splash-progress-container');
        const splashText = this.splashElement.querySelector('.splash-text');

        if (logoContainer) logoContainer.style.animation = 'logoScaleInPulse 1.2s cubic-bezier(0.34, 1.56, 0.64, 1) forwards';
        if (title) title.style.animation = 'titleSlideInGlow 1.2s ease-out 0.2s forwards';
        if (tagline) tagline.style.animation = 'fadeInScale 1s ease-out 0.4s forwards';
        if (progressContainer) progressContainer.style.animation = 'progressSlideIn 1s ease-out 0.6s forwards';
        if (splashText) splashText.style.animation = 'fadeInScale 1s ease-out 0.8s forwards';
    }

    scheduleSplashDismissal() {
        const randomDelay = Math.random() * (SPLASH_CONFIG.maxDuration - SPLASH_CONFIG.minDuration) + SPLASH_CONFIG.minDuration;

        setTimeout(() => {
            this.dismissSplash();
        }, randomDelay);
    }

    dismissSplash() {
        // Cleanup particle effect
        if (this.particleEffect) {
            this.particleEffect.destroy();
        }

        // Add epic zoom-in fade-out animation
        this.splashElement.classList.add('epic-splash-fade-out');

        // Remove splash screen after animation
        setTimeout(() => {
            this.splashElement.style.display = 'none';
            this.splashElement.remove();

            // Remove page loader
            const pageLoader = document.getElementById('pageLoader');
            if (pageLoader) {
                pageLoader.style.display = 'none';
                pageLoader.remove();
            }

            // Trigger page entrance animations
            this.triggerPageEntranceAnimations();
        }, 1500);
    }

    triggerPageEntranceAnimations() {
        document.body.classList.add('page-entered');

        // Animate main content
        const nav = document.querySelector('nav');
        const heroSection = document.querySelector('.pt-32');
        const mainContent = document.querySelectorAll('section');

        if (nav) nav.style.animation = 'slideDownFadeIn 0.8s ease-out forwards';
        if (heroSection) heroSection.style.animation = 'slideUpFadeIn 0.8s ease-out 0.2s forwards';

        mainContent.forEach((section, index) => {
            section.style.animation = `slideUpFadeIn 0.8s ease-out ${0.4 + index * 0.1}s forwards`;
            section.style.opacity = '0';
        });
    }

    setupInteractionListeners() {
        // Window resize handler for canvas
        window.addEventListener('resize', () => {
            const canvas = this.splashElement.querySelector('.splash-particles');
            if (canvas) {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }
        });

        // Allow skip on click (optional)
        this.splashElement.addEventListener('click', () => {
            // Can uncomment to allow skipping splash by clicking
            // this.dismissSplash();
        });
    }
}

// Initialize splash screen when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        new SplashScreen();
    });
} else {
    // If DOM is already loaded
    new SplashScreen();
}