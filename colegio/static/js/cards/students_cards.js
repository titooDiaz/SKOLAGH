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