import unittest

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

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('user123', 1000.0)

    def test_initial_conditions(self):
        self.assertEqual(self.account.balance, 1000.0)
        self.assertEqual(self.account.get_holdings(), {})
        self.assertEqual(self.account.get_transaction_history(), [])

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance, 1500.0)
        self.assertIn(('deposit', 500.0), self.account.get_transaction_history())

    def test_withdraw_sufficient_balance(self):
        result = self.account.withdraw(200.0)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 800.0)
        self.assertIn(('withdraw', 200.0), self.account.get_transaction_history())

    def test_withdraw_insufficient_balance(self):
        result = self.account.withdraw(1200.0)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, 1000.0)

    def test_buy_shares_sufficient_balance(self):
        result = self.account.buy_shares('AAPL', 5)
        self.assertTrue(result)
        self.assertIn('AAPL', self.account.get_holdings())
        self.assertEqual(self.account.get_holdings()['AAPL'], 5)
        self.assertEqual(self.account.balance, 1000.0 - 5 * 150.0)

    def test_buy_shares_insufficient_balance(self):
        result = self.account.buy_shares('GOOGL', 1)
        self.assertFalse(result)
        self.assertNotIn('GOOGL', self.account.get_holdings())
        self.assertEqual(self.account.balance, 1000.0)

    def test_sell_shares_sufficient_holdings(self):
        self.account.buy_shares('AAPL', 5)
        result = self.account.sell_shares('AAPL', 5)
        self.assertTrue(result)
        self.assertNotIn('AAPL', self.account.get_holdings())
        self.assertEqual(self.account.balance, 1000.0)

    def test_sell_shares_insufficient_holdings(self):
        self.account.buy_shares('AAPL', 5)
        result = self.account.sell_shares('AAPL', 10)
        self.assertFalse(result)
        self.assertIn('AAPL', self.account.get_holdings())

    def test_portfolio_value(self):
        self.account.buy_shares('AAPL', 2)
        portfolio_value = self.account.get_portfolio_value()
        self.assertEqual(portfolio_value, self.account.balance + 2 * 150.0)

    def test_calculate_profit_loss(self):
        self.account.buy_shares('AAPL', 2)
        profit_loss = self.account.calculate_profit_loss()
        expected_value = self.account.get_portfolio_value() - 1000.0
        self.assertEqual(profit_loss, expected_value)

if __name__ == '__main__':
    unittest.main()