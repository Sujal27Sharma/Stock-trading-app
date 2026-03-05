from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Indian Stocks (NSE) list
STOCKS_LIST = [
    {'symbol': 'RELIANCE', 'name': 'Reliance Industries', 'price': 2850.60},
    {'symbol': 'TCS', 'name': 'Tata Consultancy Services', 'price': 3982.15},
    {'symbol': 'HDFCBANK', 'name': 'HDFC Bank Limited', 'price': 1435.70},
    {'symbol': 'INFY', 'name': 'Infosys Limited', 'price': 1612.90},
    {'symbol': 'SBIN', 'name': 'State Bank of India', 'price': 748.20}
]

# User Data
USER_PORTFOLIO = {}
AVAILABLE_BALANCE = 100000.00  # Starting with ₹1 Lakh

# --- ROUTES ---

@app.route('/', methods=['GET', 'POST'])
def login():
    # If the user submits the fake login form, send them to the dashboard
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    # Otherwise, show them the login screen
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', stocks=STOCKS_LIST, balance=AVAILABLE_BALANCE)

@app.route('/portfolio')
def portfolio():
    portfolio_list = list(USER_PORTFOLIO.values())
    return render_template('portfolio.html', portfolio=portfolio_list, balance=AVAILABLE_BALANCE)

@app.route('/buy', methods=['POST'])
def buy():
    global AVAILABLE_BALANCE
    symbol = request.form.get('symbol')
    
    # Safety check: If no stock is selected, just reload the page
    if not symbol:
        return redirect(url_for('dashboard'))
        
    name = request.form.get('name')
    price = float(request.form.get('price'))
    quantity = int(request.form.get('quantity'))
    
    total_cost = price * quantity
    
    # Only execute if they have enough balance
    if total_cost <= AVAILABLE_BALANCE:
        AVAILABLE_BALANCE -= total_cost
        if symbol in USER_PORTFOLIO:
            USER_PORTFOLIO[symbol]['quantity'] += quantity
        else:
            USER_PORTFOLIO[symbol] = {'symbol': symbol, 'name': name, 'price': price, 'quantity': quantity}
            
    return redirect(url_for('portfolio'))

@app.route('/sell', methods=['POST'])
def sell():
    global AVAILABLE_BALANCE
    symbol = request.form.get('symbol')
    
    if not symbol:
        return redirect(url_for('dashboard'))
        
    price = float(request.form.get('price'))
    quantity = int(request.form.get('quantity'))
    
    # Only sell if they own the stock and have enough shares
    if symbol in USER_PORTFOLIO and USER_PORTFOLIO[symbol]['quantity'] >= quantity:
        total_revenue = price * quantity
        AVAILABLE_BALANCE += total_revenue
        USER_PORTFOLIO[symbol]['quantity'] -= quantity
        
        # Remove from portfolio if shares hit 0
        if USER_PORTFOLIO[symbol]['quantity'] == 0:
            del USER_PORTFOLIO[symbol]
            
    return redirect(url_for('portfolio'))

if __name__ == '__main__':
    app.run(debug=True)