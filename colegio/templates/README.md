# HTML COMPONENTS BY SKOLAGH

---

# 🎓 Student Card Component Documentation

A beautiful, responsive 3D card component designed for educational platforms. Features smooth animations, hover effects, and a modern design.

## ✨ Features

- **3D Hover Effects**: Cards lift and rotate with smooth transitions
- **Responsive Design**: Adapts to different screen sizes
- **Educational Theme**: Designed specifically for student profiles
- **Smooth Animations**: Fade-in animations with staggered timing
- **Modern Styling**: Glass-morphism effects with gradients

## 🎨 CSS Styles

we created a file called `cards.css`:

```html
<link rel="stylesheet" href="{% static 'css/user_experience/cards/cards.css' %}">
```

## 💻 JavaScript

we created a file called `student-cards.js`:

```html
<script src="{%static 'js/cards/students_cards.js' %}"></script>
```

## 🧩 HTML Template Structure

### Basic Card Structure

```html
<!-- Single Student Card -->
<div class="group relative animate-fade-in-up">
    <!-- 3D Shadow -->
    <div class="absolute inset-0 bg-gradient-to-r from-indigo-600/30 to-purple-600/30 rounded-3xl transform rotate-2 student-card-shadow"></div>
    
    <!-- Main Card -->
    <div class="student-card-3d relative bg-gradient-card backdrop-blur-sm rounded-3xl shadow-2xl border border-white/40 overflow-hidden">
        <!-- Student Header with Image -->
        <div class="relative bg-gradient-academic p-6 text-white">
            <!-- Decorative Elements -->
            <div class="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full -mr-16 -mt-16"></div>
            <div class="absolute bottom-0 left-0 w-24 h-24 bg-white/5 rounded-full -ml-12 -mb-12"></div>
            
            <div class="relative z-10 text-center">
                <!-- Student Image -->
                <div class="w-20 h-20 mx-auto mb-4 rounded-full overflow-hidden border-4 border-white/30">
                    <img src="student-photo.jpg" alt="Student Name" class="w-full h-full object-cover">
                </div>
                
                <!-- Student Name -->
                <h3 class="text-2xl font-bold mb-2">John Doe</h3>
                <p class="text-indigo-100">Student</p>
            </div>
        </div>

        <!-- Content Area -->
        <div class="p-6 bg-white">
            <!-- Content Title -->
            <h4 class="text-xl font-bold text-gray-900 mb-3">Academic Information</h4>
            
            <!-- Content Body -->
            <div class="space-y-3 mb-6">
                <p class="text-gray-600">Grade: 10th Grade</p>
                <p class="text-gray-600">Subject: Mathematics</p>
                <p class="text-gray-600">Performance: Excellent</p>
            </div>
            
            <!-- Action Button -->
            <button class="SkolaghButton-orange w-full">
                View Details
            </button>
        </div>
    </div>
</div>
```

### Complete Example with Grid

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Cards Example</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="css/student-cards.css">
</head>
<body class="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-50">
    <!-- Floating Background Elements -->
    <div class="student-cards-background"></div>
    
    <!-- Cards Container -->
    <div class="student-cards-grid">
        <!-- Student Card 1 -->
        <div class="group relative animate-fade-in-up">
            <div class="absolute inset-0 bg-gradient-to-r from-indigo-600/30 to-purple-600/30 rounded-3xl transform rotate-2 student-card-shadow"></div>
            <div class="student-card-3d relative bg-gradient-card backdrop-blur-sm rounded-3xl shadow-2xl border border-white/40 overflow-hidden">
                <div class="relative bg-gradient-academic p-6 text-white">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full -mr-16 -mt-16"></div>
                    <div class="absolute bottom-0 left-0 w-24 h-24 bg-white/5 rounded-full -ml-12 -mb-12"></div>
                    <div class="relative z-10 text-center">
                        <div class="w-20 h-20 mx-auto mb-4 rounded-full overflow-hidden border-4 border-white/30 bg-white/20">
                            <div class="w-full h-full flex items-center justify-center text-3xl">👨‍🎓</div>
                        </div>
                        <h3 class="text-2xl font-bold mb-2">John Doe</h3>
                        <p class="text-indigo-100">Student</p>
                    </div>
                </div>
                <div class="p-6 bg-white">
                    <h4 class="text-xl font-bold text-gray-900 mb-3">Academic Profile</h4>
                    <div class="space-y-3 mb-6">
                        <p class="text-gray-600">Grade: 10th Grade</p>
                        <p class="text-gray-600">Subject: Mathematics</p>
                        <p class="text-gray-600">Performance: Excellent</p>
                    </div>
                    <button class="SkolaghButton-orange w-full">View Profile</button>
                </div>
            </div>
        </div>

        <!-- Student Card 2 -->
        <div class="group relative animate-fade-in-up">
            <div class="absolute inset-0 bg-gradient-to-r from-indigo-600/30 to-purple-600/30 rounded-3xl transform rotate-2 student-card-shadow"></div>
            <div class="student-card-3d relative bg-gradient-card backdrop-blur-sm rounded-3xl shadow-2xl border border-white/40 overflow-hidden">
                <div class="relative bg-gradient-academic p-6 text-white">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full -mr-16 -mt-16"></div>
                    <div class="absolute bottom-0 left-0 w-24 h-24 bg-white/5 rounded-full -ml-12 -mb-12"></div>
                    <div class="relative z-10 text-center">
                        <div class="w-20 h-20 mx-auto mb-4 rounded-full overflow-hidden border-4 border-white/30 bg-white/20">
                            <div class="w-full h-full flex items-center justify-center text-3xl">👩‍🎓</div>
                        </div>
                        <h3 class="text-2xl font-bold mb-2">Jane Smith</h3>
                        <p class="text-indigo-100">Student</p>
                    </div>
                </div>
                <div class="p-6 bg-white">
                    <h4 class="text-xl font-bold text-gray-900 mb-3">Academic Profile</h4>
                    <div class="space-y-3 mb-6">
                        <p class="text-gray-600">Grade: 11th Grade</p>
                        <p class="text-gray-600">Subject: Science</p>
                        <p class="text-gray-600">Performance: Outstanding</p>
                    </div>
                    <button class="SkolaghButton-orange w-full">View Profile</button>
                </div>
            </div>
        </div>
    </div>

    <script src="js/student-cards.js"></script>
</body>
</html>
```

## 🐛 Troubleshooting

### Common Issues

1. **Cards not showing 3D effect**: Ensure Tailwind CSS is loaded
2. **Animations not working**: Check that JavaScript file is included after HTML
3. **Grid layout issues**: Verify container has `student-cards-grid` class
4. **Button not responsive**: Ensure `SkolaghButton-orange` class is applied

### Browser Support

- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 12+
- ✅ Edge 79+

## 📱 Responsive Behavior

- **Desktop**: 3-4 cards per row with full 3D effects
- **Tablet**: 2 cards per row with reduced animations
- **Mobile**: 1 card per row with simplified hover effects

## 🚀 Performance Tips

1. **Limit cards per page**: Recommend max 12 cards for optimal performance
2. **Lazy load images**: Use `loading="lazy"` on student images
3. **Reduce animations**: On low-end devices, consider reducing animation complexity

## 📄 License

This component is designed for educational platforms and can be freely used and modified for educational purposes.

---

**Created with ❤️ for educational excellence**