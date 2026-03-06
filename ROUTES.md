# Backend Routes & Application Logic

The Flask backend in `app.py` handles user navigation, form submissions, and the core trading mathematics. Below is the breakdown of the application's endpoints.

## 🌐 Navigation Routes
* `GET /` : Serves the `login.html` authentication page.
* `POST /` : Processes the login form submission and redirects to the dashboard.
* `GET /dashboard` : Serves the main trading terminal. Passes the `STOCKS_LIST` dictionary and current `AVAILABLE_BALANCE` to the frontend via Jinja2.
* `GET /portfolio` : Serves the user's ledger. Transforms the `USER_PORTFOLIO` dictionary into a list and passes it to the frontend for tabular rendering.

## ⚡ Trading Execution Routes
### `POST /buy`
* **Function:** Executes a simulated purchase order.
* **Logic:** 1. Retrieves `symbol`, `name`, `price`, and `quantity` from the hidden frontend form.
  2. Calculates `total_cost` (price * quantity).
  3. Validates if `total_cost <= AVAILABLE_BALANCE`.
  4. If valid, deducts the cost from the balance and updates the `USER_PORTFOLIO` state.
  5. Redirects the user to `/portfolio`.

### `POST /sell`
* **Function:** Executes a simulated sell order.
* **Logic:**
  1. Retrieves `symbol`, `price`, and `quantity` from the frontend.
  2. Validates that the user currently owns the stock and has an equal or greater quantity to sell.
  3. Calculates `total_revenue`.
  4. Adds revenue to `AVAILABLE_BALANCE` and deducts the shares from `USER_PORTFOLIO`.
  5. Cleans up the dictionary by removing the stock completely if share count reaches 0.
