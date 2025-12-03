# Skolagh UI Cards 📦✨

Welcome to the **Skolagh Cards Playground** — your visual sandbox for building clean, elegant, and future‑oriented card components.

Right now we have our first card type:

* **User Card** 👤💼

Soon you’ll be able to expand this system with more styles, variants, and specialized cards.

---

## 🧱 User Card

This card is designed for displaying user information in a polished, dimensional, gradient‑driven layout. Perfect for dashboards, profile listings, academic platforms, or anywhere you need a visually rich user presentation.

### 🔧 How to Use

Include it in any Django template like this:

```django
{% include "ui/cards/user_card.html" with name="John Doe" role="Teacher" image="/static/img/profile.png" subtitle="Mathematics" description="Specialized in calculus and discrete math" button_text="View Profile" %}
```

---

## 🎨 Card Structure

The **User Card** uses:

* A subtle 3D tilt effect
* Gradient academic header
* Circular profile image frame
* Optional subtitle
* Optional description
* Optional full‑width action button

---

## 🧩 Available Parameters

| Parameter     | Required | Description                                              |
| ------------- | -------- | -------------------------------------------------------- |
| `name`        | Yes      | Main user name                                           |
| `role`        | No       | Short role or tag under the name                         |
| `image`       | Yes      | URL to the user profile picture                          |
| `subtitle`    | No       | Section subtitle inside the card                         |
| `description` | No       | Longer descriptive text                                  |
| `button_text` | No       | If provided, displays a Skolagh full‑width orange button |

---

## 📦 Example Output

A clean, glowing, academic‑styled card with profile image, gradients, and optional content slots.

---

## 🚀 Quick Include Cheat Sheet

| Card Type | Include Snippet                                                                                |
| --------- | ---------------------------------------------------------------------------------------------- |
| User      | `{% include "ui/cards/user_card.html" with name="John Doe" image="/img.jpg" role="Teacher" %}` |

---

More card types coming soon: analytics cards, statistic blocks, action cards, academic badges, and more.

Go ahead — **card‑ify** your UI! 🚀✨