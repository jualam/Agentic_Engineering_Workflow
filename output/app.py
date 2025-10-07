import gradio as gr
from accounts import Account, get_share_price

# Initialize account
user_account = Account(user_id="user_1", initial_deposit=10000.0)

def create_account(user_id, initial_deposit):
    global user_account
    user_account = Account(user_id, initial_deposit)
    return f"✅ Account created for {user_id} with initial deposit ${initial_deposit:.2f}"

def deposit(amount):
    user_account.deposit(amount)
    return f"Deposited ${amount:.2f}. Current balance: ${user_account.balance:.2f}"

def withdraw(amount):
    if user_account.withdraw(amount):
        return f"Withdrew ${amount:.2f}. Current balance: ${user_account.balance:.2f}"
    return "Error: Insufficient balance."

def buy_shares(symbol, quantity):
    if user_account.buy_shares(symbol, quantity):
        return f"Bought {quantity} shares of {symbol}. Current balance: ${user_account.balance:.2f}"
    return "Error: Insufficient balance or invalid symbol."

def sell_shares(symbol, quantity):
    if user_account.sell_shares(symbol, quantity):
        return f"Sold {quantity} shares of {symbol}. Current balance: ${user_account.balance:.2f}"
    return "Error: Insufficient holdings or invalid symbol."

def view_holdings():
    return f"Current Holdings:\n{user_account.get_holdings()}"

def view_transactions():
    return f"Transaction History:\n{user_account.get_transaction_history()}"

def view_portfolio_value():
    return f"Portfolio Value: ${user_account.get_portfolio_value():.2f}"

def view_profit_loss():
    return f"Profit/Loss: ${user_account.calculate_profit_loss():.2f}"

def perform_action(action, field1, field2):
    try:
        if action == "Create Account":
            return create_account(field1, float(field2))
        elif action == "Deposit":
            return deposit(float(field1))
        elif action == "Withdraw":
            return withdraw(float(field1))
        elif action == "Buy Shares":
            return buy_shares(field1.upper(), int(field2))
        elif action == "Sell Shares":
            return sell_shares(field1.upper(), int(field2))
        elif action == "View Holdings":
            return view_holdings()
        elif action == "View Transactions":
            return view_transactions()
        elif action == "View Portfolio Value":
            return view_portfolio_value()
        elif action == "View Profit/Loss":
            return view_profit_loss()
    except Exception as e:
        return f"Error: {e}"

def update_labels(action):
    """Dynamically update input labels."""
    if action == "Create Account":
        return gr.update(label="User ID"), gr.update(label="Initial Deposit")
    elif action == "Deposit":
        return gr.update(label="Deposit Amount"), gr.update(label="(Leave blank)")
    elif action == "Withdraw":
        return gr.update(label="Withdrawal Amount"), gr.update(label="(Leave blank)")
    elif action == "Buy Shares":
        return gr.update(label="Stock Symbol (e.g. AAPL)"), gr.update(label="Quantity")
    elif action == "Sell Shares":
        return gr.update(label="Stock Symbol (e.g. AAPL)"), gr.update(label="Quantity")
    else:
        return gr.update(label="(Not required)"), gr.update(label="(Not required)")

# --- Modern Minimal CSS ---
modern_css = """
body {
    background-color: #f9fafb;
    color: #111827;
    font-family: 'Inter', sans-serif;
}
h1 {
    color: #0f172a;
    text-align: center;
    font-weight: 600;
}
h3 {
    color: #2563eb;
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
}
.gradio-container {
    max-width: 900px !important;
    margin: 0 auto !important;
    border-radius: 12px !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05) !important;
    background: white !important;
    padding: 30px !important;
}
textarea, input, select {
    border-radius: 8px !important;
    border: 1px solid #d1d5db !important;
    background: #f9fafb !important;
    color: #111827 !important;
}
button {
    background-color: #2563eb !important;
    color: white !important;
    border-radius: 8px !important;
    border: none !important;
    font-weight: 600 !important;
    height: 45px !important;
}
button:hover {
    background-color: #1d4ed8 !important;
}
.output-box {
    background: #f3f4f6 !important;
    border-radius: 8px !important;
    border: 1px solid #d1d5db !important;
    color: #111827 !important;
}
.markdown-table {
    margin-top: 1rem !important;
    border-radius: 8px !important;
    background: #f8fafc !important;
    border: 1px solid #e5e7eb !important;
    padding: 12px;
}
"""

# --- Gradio UI ---
with gr.Blocks(css=modern_css, theme=gr.themes.Base()) as demo:
    gr.Markdown("# Trading Account Management System")
    gr.Markdown(
        "Manage your trading account, perform transactions, and track performance. "
        "Use the guide below to understand what each input represents:"
    )
    gr.Markdown(
        """
        ### Parameter Guide
        | Action | Field 1 | Field 2 |
        |---------|----------|----------|
        | **Create Account** | User ID | Initial Deposit |
        | **Deposit** | Deposit Amount | *(Leave blank)* |
        | **Withdraw** | Withdrawal Amount | *(Leave blank)* |
        | **Buy Shares** | Stock Symbol (e.g. AAPL) | Quantity |
        | **Sell Shares** | Stock Symbol (e.g. AAPL) | Quantity |
        | **View Holdings / Portfolio / Profit-Loss** | *(Not required)* | *(Not required)* |
        """,
        elem_classes=["markdown-table"]
    )

    with gr.Row():
        action = gr.Dropdown(
            choices=[
                "Create Account", "Deposit", "Withdraw",
                "Buy Shares", "Sell Shares",
                "View Holdings", "View Transactions",
                "View Portfolio Value", "View Profit/Loss"
            ],
            label="Select Action",
            interactive=True
        )

    with gr.Row():
        field1 = gr.Textbox(label="Input Field 1", placeholder="e.g. User ID or Stock Symbol")
        field2 = gr.Textbox(label="Input Field 2", placeholder="e.g. Deposit Amount or Quantity")

    run_button = gr.Button("Execute Action")
    output = gr.Textbox(label="Result", elem_classes=["output-box"], lines=8)

    action.change(update_labels, inputs=[action], outputs=[field1, field2])
    run_button.click(perform_action, inputs=[action, field1, field2], outputs=output)

demo.launch()

