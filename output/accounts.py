class Account:
    def __init__(self, user_id: str, initial_deposit: float):
        self.user_id = user_id
        self.balance = initial_deposit
        self.initial_deposit = initial_deposit
        self.holdings = {}
        self.transactions = []

    def deposit(self, amount: float) -> None:
        self.balance += amount
        self.transactions.append(('deposit', amount))

    def withdraw(self, amount: float) -> bool:
        if self.can_withdraw(amount):
            self.balance -= amount
            self.transactions.append(('withdraw', amount))
            return True
        return False

    def buy_shares(self, symbol: str, quantity: int) -> bool:
        price = get_share_price(symbol)
        total_cost = price * quantity
        if self.can_buy(symbol, quantity):
            self.balance -= total_cost
            if symbol in self.holdings:
                self.holdings[symbol] += quantity
            else:
                self.holdings[symbol] = quantity
            self.transactions.append(('buy', symbol, quantity, price))
            return True
        return False

    def sell_shares(self, symbol: str, quantity: int) -> bool:
        price = get_share_price(symbol)
        if self.can_sell(symbol, quantity):
            self.balance += price * quantity
            self.holdings[symbol] -= quantity
            if self.holdings[symbol] == 0:
                del self.holdings[symbol]
            self.transactions.append(('sell', symbol, quantity, price))
            return True
        return False

    def get_portfolio_value(self) -> float:
        portfolio_value = self.balance
        for symbol, quantity in self.holdings.items():
            portfolio_value += get_share_price(symbol) * quantity
        return portfolio_value

    def calculate_profit_loss(self) -> float:
        return self.get_portfolio_value() - self.initial_deposit

    def get_holdings(self) -> dict:
        return self.holdings.copy()

    def get_transaction_history(self) -> list:
        return self.transactions.copy()

    def can_withdraw(self, amount: float) -> bool:
        return self.balance >= amount

    def can_buy(self, symbol: str, quantity: int) -> bool:
        price = get_share_price(symbol)
        total_cost = price * quantity
        return self.balance >= total_cost

    def can_sell(self, symbol: str, quantity: int) -> bool:
        return symbol in self.holdings and self.holdings[symbol] >= quantity

def get_share_price(symbol: str) -> float:
    prices = {'AAPL': 150.0, 'TSLA': 800.0, 'GOOGL': 2800.0}
    return prices.get(symbol.upper(), 0.0)