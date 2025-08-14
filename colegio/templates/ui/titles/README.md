# Skolagh UI Titles 🎉🌟

Welcome to the **Skolagh Titles Playground**! 🌟
We’ve got a bunch of shiny, reusable, drop-dead gorgeous title styles you can sprinkle all over your project like confetti! 🎈

## 📖 What’s Inside?

For now, we have **six fabulous types of titles**:

1. **Badge Title** 🌟🎉
2. **Icon Title** 🔖
3. **Minimalistic Title** 🧘‍♂️
4. **Principal Title** 🎓
5. **Special Title** 💫
6. **Subtitle Title** 🎤

Each one is designed with **love, gradients, and pixel-perfect precision** ✨.

---

## 📝 How to Use

Using them is **super easy** — like eating cake 🍰.

### Example: Principal Title

```django
{% include "ui/titles/principal.html" with title="Personas Relacionadas" %}
```

That’s it. Boom. Your page now has a **principal gradient title** that says *"I run the show"*. 🌟

---

## 🎭 Title Types & Usage

### 1. Badge Title 🌟🎉

Perfect for pages that have new stuff, updates, or any reason to shout **"Look here!"**.

```html
<div class="page-title-badge">
    <h1>Messages</h1>
    <span>New</span>
</div>
```

### 2. Icon Title 🔖

Ideal for dashboards, menus, or any title that needs a sidekick (an icon).

```html
<div class="page-title-with-icon">
    <svg><!-- your icon --></svg>
    <h1>Calendar</h1>
</div>
```

### 3. Minimalistic Title 🧘‍♂️

For when you want to keep things classy, clean, and distraction-free.

```html
<div class="page-title-minimal">
    <h1>Profile</h1>
</div>
```

### 4. Principal Title 🎓

The "big boss" of titles. Perfect for main sections.

```html
<div class="page-title">
    <h1>Main Title</h1>
</div>
```

### 5. Special Title 💫

Great for modals, announcements, or highlighting something extraordinary.

```html
<div class="page-title-centered">
    <h1>Student Notes</h1>
</div>
```

### 6. Subtitle Title 🎤

Adds context under your main title — perfect for explaining what’s going on.

```html
<div class="page-title-subtitle">
    <p>Student Management</p>
    <h1>Control Panel</h1>
</div>
```

---

## 💡 Pro Tips

* Always pass the **parameters** when including the title in a Django template.
* Titles look even better with **consistent spacing and matching color themes**.
* Pair them with Skolagh’s button & card components for **max visual deliciousness** 🌟.

---

## 🚀 Quick Include Cheat Sheet

| Type         | Include Snippet                                                                                                                          |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Principal    | `{% include "ui/titles/principal.html" with title="My Title" %}`                                                                         |
| Badge        | `{% include "ui/titles/badge.html" with title="Messages" badge="New" %}`                                                                 |
| Icon         | `{% include "ui/titles/icon.html" with title="Calendar" description="My schedule" %}`                                                    |
| Minimalistic | `{% include "ui/titles/minimal.html" with title="Profile" %}`                                                                            |
| Special      | `{% include "ui/titles/special.html" with title="Student Notes" description="All your notes in one place" %}`                            |
| Subtitle     | `{% include "ui/titles/subtitle.html" with subtitle="Student Management" title="Control Panel" description="Manage all student info" %}` |

---

Now go forth and **title-ify** your pages! 🚀🌟✨
