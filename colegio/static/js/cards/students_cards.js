/**
 * Student Card Component JavaScript
 * Handles animations and interactive effects
 */

document.addEventListener('DOMContentLoaded', function() {
    initializeStudentCards();
});

function initializeStudentCards() {
    // Add staggered animation to cards
    addStaggeredAnimations();
    
    // Add ripple effects to buttons
    addButtonRippleEffects();
    
    // Initialize floating background elements
    createFloatingBackground();
}

/**
 * Adds staggered fade-in animation to student cards
 */
function addStaggeredAnimations() {
    const cards = document.querySelectorAll('.animate-fade-in-up');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 150}ms`;
    });
}

/**
 * Adds ripple effect to buttons on click
 */
function addButtonRippleEffects() {
    const buttons = document.querySelectorAll('.SkolaghButton-orange');
    
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            createRipple(e, this);
        });
    });
}

/**
 * Creates a ripple effect on button click
 * @param {Event} e - Click event
 * @param {Element} button - Button element
 */
function createRipple(e, button) {
    // Remove existing ripples
    const existingRipple = button.querySelector('.ripple');
    if (existingRipple) {
        existingRipple.remove();
    }
    
    const ripple = document.createElement('div');
    const rect = button.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = e.clientX - rect.left - size / 2;
    const y = e.clientY - rect.top - size / 2;
    
    ripple.style.width = size + 'px';
    ripple.style.height = size + 'px';
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';
    ripple.className = 'ripple';
    
    // Ripple styles
    ripple.style.position = 'absolute';
    ripple.style.borderRadius = '50%';
    ripple.style.background = 'rgba(255, 255, 255, 0.6)';
    ripple.style.transform = 'scale(0)';
    ripple.style.animation = 'ripple 0.6s linear';
    ripple.style.pointerEvents = 'none';
    
    button.style.position = 'relative';
    button.style.overflow = 'hidden';
    button.appendChild(ripple);
    
    // Remove ripple after animation
    setTimeout(() => {
        ripple.remove();
    }, 600);
}

/**
 * Creates floating background elements for decoration
 */
function createFloatingBackground() {
    const background = document.querySelector('.student-cards-background');
    if (!background) return;
    
    const colors = ['#3b82f6', '#8b5cf6', '#06b6d4', '#10b981'];
    const sizes = [80, 64, 96, 48];
    
    for (let i = 0; i < 4; i++) {
        const element = document.createElement('div');
        element.className = 'floating-element animate-float';
        element.style.width = sizes[i] + 'px';
        element.style.height = sizes[i] + 'px';
        element.style.backgroundColor = colors[i];
        element.style.top = Math.random() * 80 + '%';
        element.style.left = Math.random() * 80 + '%';
        element.style.animationDelay = i * 1000 + 'ms';
        
        background.appendChild(element);
    }
}

// Add ripple animation keyframe
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple {
        to {
            transform: scale(2);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);