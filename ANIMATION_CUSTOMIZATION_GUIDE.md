# Advanced Animation Customization Guide

## Quick Start: Copy & Paste Solutions

### 1. **Speed Up Animation**
Edit `assets/splash.js`:
```javascript
const SPLASH_CONFIG = {
    minDuration: 2000,  // 2 seconds minimum
    maxDuration: 3500,  // 3.5 seconds maximum
    // ... rest of config
};
```

### 2. **More Particles**
```javascript
const SPLASH_CONFIG = {
    particleCount: 80,  // Double the particles!
    // ... rest of config
};
```

### 3. **Fewer Particles (Better Performance)**
```javascript
const SPLASH_CONFIG = {
    particleCount: 20,  // Mobile-friendly
    // ... rest of config
};
```

### 4. **Change Particle Colors**
Edit `assets/splash.js` in the `createParticles()` method:
```javascript
const colors = [
    '#ff0000',  // Red
    '#00ff00',  // Green
    '#0000ff',  // Blue
    '#ffff00',  // Yellow
];
```

---

## 5. **Custom Color Scheme**

Edit `assets/main.css`:
```css
:root {
    --primary-cyan: #00ffff;      /* Change cyan */
    --primary-blue: #0066ff;      /* Change blue */
    --primary-indigo: #7700ff;    /* Change purple */
    --accent-rose: #ff0066;       /* Change accent */
    --deep-bg: #000000;           /* Change background */
}
```

Then refresh your browser.

---

## 6. **Dark Mode (Darker Background)**
Edit `assets/main.css`, find `.splash-overlay`:
```css
.splash-overlay {
    background: radial-gradient(ellipse at center, 
        rgba(0, 0, 0, 0.7) 0%,      /* Darker */
        rgba(0, 0, 0, 0.9) 100%     /* Much darker */
    );
}
```

---

## 7. **Light Mode (Brighter Overlay)**
```css
.splash-overlay {
    background: radial-gradient(ellipse at center, 
        rgba(15, 23, 42, 0.1) 0%,   /* Very light */
        rgba(15, 23, 42, 0.3) 100%  /* Light */
    );
}
```

---

## 8. **Make Text Bigger**
Edit `assets/main.css`, find `.splash-title`:
```css
.splash-title {
    font-size: 5.5rem;  /* Was 4rem, now 5.5rem */
    /* ... rest of styles */
}
```

---

## 9. **Slower Animations**
Edit `assets/main.css`, find keyframe animations and increase duration:
```css
/* Before */
animation: logoScaleInPulse 1s cubic-bezier(...) forwards;

/* After - make it 1.5x slower */
animation: logoScaleInPulse 1.5s cubic-bezier(...) forwards;
```

---

## 10. **Faster Animations**
Make all durations smaller:
```css
/* Before: 1s */
/* After: 0.6s */
animation: logoScaleInPulse 0.6s cubic-bezier(...) forwards;
```

---

## Advanced: Disable Elements

### Disable Particles Entirely
Edit `assets/splash.js`:
```javascript
const SPLASH_CONFIG = {
    enableParticles: false,  // This disables particles
    // ... rest
};
```

### Disable Glow Effects
```javascript
const SPLASH_CONFIG = {
    enableGlowEffects: false,  // Removes all glows
    // ... rest
};
```

### Hide Background Shapes
Edit `assets/main.css`:
```css
.splash-bg-shapes {
    display: none;  /* Hides all 4 blob shapes */
}
```

### Hide Light Effects
```css
.splash-light-effect {
    display: none;  /* Hides floating lights */
}
```

---

## Custom Keyframe Example: Change Logo Size

Edit `assets/main.css`:
```css
@keyframes logoScaleInPulse {
    0% {
        opacity: 0;
        transform: scale(0) rotate(-180deg);          /* Start tiny */
        filter: blur(20px) brightness(0.5);
    }
    50% {
        opacity: 1;
        transform: scale(1.5);                        /* Change from 1.25 to 1.5 */
        filter: blur(0) brightness(1.3);
    }
    75% {
        transform: scale(1.1);                        /* Change from 0.95 to 1.1 */
    }
    100% {
        opacity: 1;
        transform: scale(1);
        filter: blur(0) brightness(1);
    }
}
```

---

## Change Progress Bar Length

Edit `assets/main.css`:
```css
.splash-progress-container {
    width: 500px;  /* Was 300px, now wider */
    height: 6px;
    /* ... rest */
}
```

---

## Change Progress Bar Height

```css
.splash-progress-container {
    width: 300px;
    height: 10px;  /* Was 6px, now thicker */
    /* ... rest */
}
```

---

## Add Rounded Corners to Progress Bar

```css
.splash-progress-container {
    border-radius: 20px;  /* Rounder corners */
    /* ... rest */
}

.splash-progress-bar {
    border-radius: 20px;  /* Match container */
    /* ... rest */
}
```

---

## Custom Background Video

Edit `assets/splash.js`:
```javascript
const SPLASH_CONFIG = {
    videoUrl: 'https://your-video-url.mp4',
    fallbackUrl: 'https://fallback-video-url.mp4',
    // ... rest
};
```

---

## Advanced: Add Custom Animation

Add to `assets/main.css`:
```css
@keyframes myCustomAnimation {
    0% {
        opacity: 0;
        transform: translateY(50px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

.my-custom-element {
    animation: myCustomAnimation 1s ease-out forwards;
    animation-delay: 0.5s;
}
```

Then add to HTML:
```html
<div class="my-custom-element">
    Your custom content
</div>
```

---

## Mobile Optimization: Reduce Particles on Mobile

Edit `assets/splash.js`:
```javascript
const isMobile = window.innerWidth < 768;
SPLASH_CONFIG.particleCount = isMobile ? 20 : 40;
```

---

## Testing Guide

1. **Test Particles**: Open DevTools (F12) → Console
   ```javascript
   // Check particle count
   console.log(SPLASH_CONFIG.particleCount);
   ```

2. **Test Timing**: Measure total animation time
   ```javascript
   // Check config timing
   console.log(SPLASH_CONFIG.minDuration, SPLASH_CONFIG.maxDuration);
   ```

3. **Test Performance**: DevTools → Performance tab → Record → Reload → Stop
   - Should see 60 FPS throughout

4. **Test Colors**: Edit CSS variable and refresh
   ```css
   --primary-cyan: #ff0000;  /* Turn red */
   ```

---

## Troubleshooting Customizations

**Changes not showing?**
- Clear browser cache (Ctrl+Shift+Delete)
- Hard refresh (Ctrl+Shift+R)
- Close and reopen DevTools

**Animation jittery?**
- Reduce particle count
- Reduce animation complexity
- Check CPU usage in DevTools

**Text too small?**
- Increase `font-size` in `.splash-title`
- Increase percentage counter size too

**Colors look wrong?**
- Check hex color codes are valid
- Use online color picker: https://htmlcolorcodes.com
- Test in different browsers

---

## Complete Custom Example: Gaming Theme

```javascript
// assets/splash.js
const SPLASH_CONFIG = {
    minDuration: 2000,
    maxDuration: 3000,
    particleCount: 60,
    enableParticles: true,
    enableGlowEffects: true
};

// In createParticles():
const colors = [
    '#ff00ff',  // Magenta
    '#00ffff',  // Cyan
    '#00ff00',  // Green
    '#ffff00',  // Yellow
];
```

```css
/* assets/main.css */
:root {
    --primary-cyan: #00ffff;
    --primary-blue: #ff00ff;
    --primary-indigo: #00ff00;
    --deep-bg: #000011;  /* Dark purple-black */
}

.splash-title {
    font-size: 5rem;
    letter-spacing: 5px;  /* Extra spaced */
    text-transform: uppercase;
}

.splash-progress-container {
    width: 400px;
    height: 8px;
    border-radius: 20px;
}
```

---

## Pro Tips

1. **Always backup** before making changes
2. **Use browser DevTools** to test in real-time
3. **Test on mobile** - different aspect ratios
4. **Monitor performance** - keep FPS at 60
5. **Keep colors consistent** - use color palette
6. **Test video URLs** - ensure they work
7. **Validate CSS** - check for syntax errors
8. **Use CSS comments** - mark your changes

---

## Ready to Customize!

Your animation system is fully customizable. Start with small changes and test each one. Enjoy creating your perfect entrance animation! 🎨✨

