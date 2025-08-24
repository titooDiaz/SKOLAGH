// Global click handler for all <a> and <button> elements
document.addEventListener('click', (e) => {
    const el = e.target.closest('a, button');
    if (el) {
        // Trigger vibration (if supported and on mobile)
        navigator.vibrate?.([40]);

        // Remove focus after a short delay
        setTimeout(() => el.blur(), 100);
    }
});
document.addEventListener('DOMContentLoaded', function() {
    addButtonRippleEffects();
});

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