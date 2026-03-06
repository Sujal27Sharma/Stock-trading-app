# Core Features & Modules

The NEXUS Trading Simulator is divided into several interconnected modules that simulate a live trading environment.

## 1. Authentication Module
* **Fake Secure Login:** A gateway page (`login.html`) that simulates user authentication.
* **Session Redirection:** Automatically routes authenticated users to their personalized dashboard.

## 2. Dynamic Market Dashboard
* **Live Index Tracking:** Visual mockups of NIFTY 50, SENSEX, and NIFTY BANK performance.
* **Interactive Charting (Chart.js):** A responsive line chart that visually redraws itself using vanilla JavaScript when a user selects a different stock from the Market Watch list.
* **Live News Feed:** A scrolling, CSS-styled ticker at the bottom of the dashboard providing contextual (simulated) financial news to the trader.

## 3. Trading Terminal
* **Real-Time Calculation:** As the user inputs a quantity of shares, JavaScript dynamically calculates the total order value based on the current market price of the selected asset.
* **Mode Switching:** Toggle buttons seamlessly switch the terminal's state between 'BUY' and 'SELL' modes, updating the UI colors and form actions dynamically.
* **Order Validation:** Frontend and backend checks ensure a user cannot buy more than their available balance, or sell more shares than they currently own.

## 4. Portfolio Ledger
* **State Persistence:** Tracks the user's active holdings during the session.
* **Dynamic Table Rendering:** Uses Jinja2 templating to render the portfolio table. If the portfolio is empty, it displays a user-friendly prompt to return to the dashboard.
*
