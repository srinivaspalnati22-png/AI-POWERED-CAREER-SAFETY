# Homepage Animation Application Map

## Complete Visual Reference of All Animations

### Hero Section
```html
<!-- Main Hero Title with Glowing Text -->
<h1 class="text-white text-glow-animate">
    Secure Future Work.
</h1>
Animation: text-glow-animate
Effect: Continuous glowing text shadow (3s cycle)
Color: Cyan → Blue → Indigo → Purple glow
```

### Hero Image Container
```html
<!-- Floating Image with Dynamic Shadow -->
<div class="floating hero-image-animate">
    <img src="hero_ai_shield_1772724281641.png">
</div>
Animation: hero-image-animate
Effect: Vertical floating motion with scale change (4s cycle)
Motion: Y: 0→-30px, Scale: 1→1.04
Shadow: Dynamic drop-shadow with color shifts
```

### Floating Badge (Status Indicator)
```html
<!-- Pulsing 3D Badge -->
<div class="hero-badge-animate">
    Active Status Badge
</div>
Animation: hero-badge-animate
Effect: Pulsing scale + 3D rotation (2s cycle)
Motion: Scale 1→1.05, RotateY 5 degrees
Creates: Floating, breathing effect
```

### CTA Buttons (Both)
```html
<!-- Start Analysis Button -->
<a href="analyze.html" class="btn-glow">
    Start Analysis →
</a>

<!-- Explore Features Button -->
<a href="features.html" class="btn-glow">
    Explore Features
</a>
Animation: btn-glow
Effect: Box-shadow glow pulse on hover (1.5s)
Trigger: :hover state
Color: Glowing white border effect
```

---

## Features Section

### Section Header
```html
<!-- Features Section Title with Glow -->
<h2 class="text-glow-animate">
    Your Career, Protected
</h2>
Animation: text-glow-animate
Effect: Glowing text (3s cycle, repeats forever)
Entrance: Fades up with stagger delay (0.1s)
```

---

## Feature Cards Grid

### Card 1: Job Risk Scan
```html
<div class="glass card-slide-in card-hover-lift">
    <div class="icon-bounce">🔍</div>
    <h3>Job Risk Scan</h3>
    <p>AI-powered job opportunity risk assessment...</p>
</div>

Animations Applied:
├─ card-slide-in
│  ├─ Entrance: Slides in from below (0.6s)
│  ├─ Start: translateY(50px), rotateX(10deg), opacity(0)
│  ├─ End: translateY(0), rotateX(0deg), opacity(1)
│  ├─ Timing: Appears at 0.1s delay
│  └─ Effect: 3D perspective entrance from bottom
│
├─ card-hover-lift  
│  ├─ Trigger: :hover state
│  ├─ Effect: Card lifts up with shadow
│  ├─ Transform: translateY(-15px) scale(1.02)
│  ├─ Shadow: Enhanced drop-shadow
│  └─ Duration: 300ms smooth transition
│
└─ icon-bounce (on 🔍 emoji)
   ├─ Animation: Continuous bounce (2s cycle)
   ├─ Motion: Scale pulse + vertical bounce
   ├─ Effect: Up and down bouncing motion
   └─ Duration: Repeats forever
```

### Card 2: Resume Integrity
```html
<div class="glass card-slide-in card-hover-lift">
    <div class="icon-bounce">📄</div>
    <h3>Resume Integrity</h3>
    <p>Ensure your resume passes ATS systems...</p>
</div>

Animations Applied:
├─ card-slide-in
│  ├─ Entrance: Slides in from below (0.6s)
│  ├─ Timing: Appears at 0.3s delay (200ms after first card)
│  └─ Effect: 3D perspective entrance from bottom
│
├─ card-hover-lift
│  ├─ Trigger: :hover state
│  ├─ Effect: Card lifts with shadow
│  └─ Duration: Smooth 300ms transition
│
└─ icon-bounce (on 📄 emoji)
   ├─ Continuous bounce animation
   └─ Repeats forever
```

### Card 3: Company Verify
```html
<div class="glass card-slide-in card-hover-lift">
    <div class="icon-bounce">🌍</div>
    <h3>Company Verify</h3>
    <p>Real-time business registration checks...</p>
</div>

Animations Applied:
├─ card-slide-in
│  ├─ Entrance: Slides in from below (0.6s)
│  ├─ Timing: Appears at 0.5s delay (200ms after Resume card)
│  └─ Effect: 3D perspective entrance from bottom
│
├─ card-hover-lift
│  ├─ Trigger: :hover state
│  └─ Effect: Lifts with enhanced shadow
│
└─ icon-bounce (on 🌍 emoji)
   ├─ Continuous bounce
   └─ Repeats forever
```

### Card 4: Future Career
```html
<div class="glass card-slide-in card-hover-lift">
    <div class="icon-bounce">🔮</div>
    <h3>Future Career</h3>
    <p>AI-driven career path prediction...</p>
</div>

Animations Applied:
├─ card-slide-in
│  ├─ Entrance: Slides in from below (0.6s)
│  ├─ Timing: Appears at 0.6s delay (100ms after Company card)
│  └─ Effect: 3D perspective entrance
│
├─ card-hover-lift
│  ├─ Trigger: :hover state
│  └─ Effect: Lifts with shadow
│
└─ icon-bounce (on 🔮 emoji)
   ├─ Continuous bounce
   └─ Repeats forever
```

---

## Animation Timing Diagram

```
Page Load Timeline:

0ms      100ms    200ms    300ms    400ms    500ms    600ms
|--------|--------|--------|--------|--------|--------|
│
├─ Hero Text Fade-up Starts (staggered)
│  ├─ Badge: 0ms
│  ├─ Heading: 100ms
│  ├─ Paragraph: 200ms
│  ├─ Buttons: 300ms
│  └─ Completes: 600ms
│
├─ Hero Image Float Animation Starts
│  └─ Continuous 4s cycle (0→4→8→12s...)
│
├─ Hero Badge Pulse Animation Starts
│  └─ Continuous 2s cycle (0→2→4→6s...)
│
├─ Features Section Title Glow Starts
│  └─ Continuous 3s cycle
│
└─ Card Entrance Animations (Staggered)
   ├─ Card 1 (Job Risk): 100ms
   ├─ Card 2 (Resume): 300ms
   ├─ Card 3 (Company): 500ms
   ├─ Card 4 (Future): 600ms
   └─ All Complete: 1200ms (1.2 seconds after page load)

Icon Bounce (All Cards): Starts immediately
├─ Icon 1: 0→2→4→6s... (continuous)
├─ Icon 2: 0→2→4→6s... (continuous)
├─ Icon 3: 0→2→4→6s... (continuous)
└─ Icon 4: 0→2→4→6s... (continuous)

Button Glow: Triggered on :hover (any time after load)
├─ Button 1: On hover → 1.5s animation
└─ Button 2: On hover → 1.5s animation

Card Hover: Triggered on :hover (any time after load)
├─ Card 1: On hover → 300ms lift
├─ Card 2: On hover → 300ms lift
├─ Card 3: On hover → 300ms lift
└─ Card 4: On hover → 300ms lift
```

---

## Animation Classes Quick Reference

### Apply to Text Elements
```html
<h1 class="text-glow-animate">Glowing Text</h1>
<!-- Creates continuous glowing text effect (3s) -->

<p class="fade-up">Content Appears</p>
<!-- Creates fade-up entrance with stagger delays -->

<p class="fade-in">Content Fades In</p>
<!-- Creates fade-in entrance with brightness increase -->
```

### Apply to Image Elements
```html
<div class="hero-image-animate">
    <img src="...">
</div>
<!-- Creates floating animation with scale changes (4s) -->
```

### Apply to Badge Elements
```html
<div class="hero-badge-animate">Badge Content</div>
<!-- Creates pulsing 3D badge effect (2s) -->
```

### Apply to Card Elements
```html
<div class="card-slide-in card-hover-lift">
    <div class="icon-bounce">Icon</div>
    <!-- Creates:
         - Card slide-in entrance (0.6s) with stagger
         - Card lift on hover (300ms)
         - Icon bounce (2s continuous)
    -->
</div>
```

### Apply to Button Elements
```html
<button class="btn-glow">Click Me</button>
<!-- Creates glowing button effect on :hover (1.5s) -->
```

---

## CSS Animation Definitions Reference

### Text Glow Animation
```css
@keyframes textGlow {
    0%, 100% {
        text-shadow: 0 0 10px rgba(6, 182, 212, 0.5),
                     0 0 20px rgba(59, 130, 246, 0.3);
    }
    50% {
        text-shadow: 0 0 20px rgba(6, 182, 212, 0.8),
                     0 0 40px rgba(59, 130, 246, 0.6),
                     0 0 60px rgba(99, 102, 241, 0.4);
    }
}
```

### Hero Image Float
```css
@keyframes heroImageFloat {
    0%, 100% { 
        transform: translateY(0px) scale(1);
        filter: drop-shadow(0 20px 50px rgba(0, 0, 0, 0.3));
    }
    50% { 
        transform: translateY(-30px) scale(1.04);
        filter: drop-shadow(0 40px 80px rgba(59, 130, 246, 0.5));
    }
}
```

### Card Slide-In (3D)
```css
@keyframes cardSlideIn {
    from {
        opacity: 0;
        transform: translateY(50px) rotateX(10deg);
    }
    to {
        opacity: 1;
        transform: translateY(0) rotateX(0deg);
    }
}
```

### Icon Bounce
```css
@keyframes iconBounce {
    0%, 100% { 
        transform: translateY(0) scale(1);
    }
    50% { 
        transform: translateY(-10px) scale(1.1);
    }
}
```

### Button Glow (Hover)
```css
.btn-glow:hover {
    animation: buttonGlow 1.5s ease-in-out infinite;
}

@keyframes buttonGlow {
    0%, 100% { 
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.5);
    }
    50% { 
        box-shadow: 0 0 40px rgba(255, 255, 255, 0.8);
    }
}
```

---

## Visual Element to Animation Mapping

| Element | Animation Class | Type | Duration | Trigger |
|---------|-----------------|------|----------|---------|
| Hero Title | `text-glow-animate` | Glow | 3s | Automatic |
| Hero Image | `hero-image-animate` | Float | 4s | Automatic |
| Hero Badge | `hero-badge-animate` | Pulse | 2s | Automatic |
| CTA Button 1 | `btn-glow` | Glow | 1.5s | Hover |
| CTA Button 2 | `btn-glow` | Glow | 1.5s | Hover |
| Section Title | `text-glow-animate` | Glow | 3s | Automatic |
| Card 1 | `card-slide-in` | Slide | 0.6s | Load |
| Card 1 | `card-hover-lift` | Lift | 0.3s | Hover |
| Card 1 Icon | `icon-bounce` | Bounce | 2s | Automatic |
| Card 2 | `card-slide-in` | Slide | 0.6s | Load |
| Card 2 | `card-hover-lift` | Lift | 0.3s | Hover |
| Card 2 Icon | `icon-bounce` | Bounce | 2s | Automatic |
| Card 3 | `card-slide-in` | Slide | 0.6s | Load |
| Card 3 | `card-hover-lift` | Lift | 0.3s | Hover |
| Card 3 Icon | `icon-bounce` | Bounce | 2s | Automatic |
| Card 4 | `card-slide-in` | Slide | 0.6s | Load |
| Card 4 | `card-hover-lift` | Lift | 0.3s | Hover |
| Card 4 Icon | `icon-bounce` | Bounce | 2s | Automatic |

---

## Total Animation Count

```
✅ Automatic (Always Running):
   • 2 Text Glow effects
   • 1 Hero Float animation
   • 1 Badge Pulse animation
   • 4 Icon Bounce animations
   ────────────────────────────
     Total: 8 infinite animations

✅ On Hover:
   • 2 Button Glow effects
   • 4 Card Lift effects
   ────────────────────────────
     Total: 6 hover-triggered animations

✅ On Load (One-Time):
   • 4 Card Slide-In animations
   • 4 Staggered entrance timings
   ────────────────────────────
     Total: 4 entrance animations

════════════════════════════════
GRAND TOTAL: 18+ Animation Applications
```

---

**All animations are fully implemented and ready to use!**
