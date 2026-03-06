# System Architecture

The NEXUS Trading Simulator is built using a lightweight, efficient tech stack tailored for rapid prototyping and seamless full-stack integration.

## 🛠️ Technology Stack
* **Frontend (Client-Side):** HTML5, CSS3, Vanilla JavaScript.
* **Backend (Server-Side):** Python 3, Flask Web Framework.
* **Data Visualization:** Chart.js (for rendering dynamic, interactive market graphs).
* **Architecture Pattern:** MVC (Model-View-Controller) utilizing Jinja2 templating.

## 📂 Repository Structure
```text
📦 nexus-trading-app
 ┣ 📂 templates/             # Contains all frontend HTML views (The 'View' in MVC)
 ┃ ┣ 📜 base.html            # Master layout containing sidebar, top-nav, and base CSS
 ┃ ┣ 📜 dashboard.html       # Main trading terminal and dynamic charts
 ┃ ┣ 📜 login.html           # Authentication UI
 ┃ ┗ 📜 portfolio.html       # Ledger displaying user's current holdings
 ┣ 📜 app.py                 # The core Flask backend engine (The 'Controller' in MVC)
 ┗ 📜 README.md              # Project overview
