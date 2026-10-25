import math

class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):

        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({'amount': -amount, 'description': description})
            return True


    def get_balance(self):
        sum_acount = 0
        for record in self.ledger:
            sum_acount += record['amount']

        return sum_acount


    def transfer(self, amount, destination: 'Category'):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount,  f"Transfer from {self.name}")
            return True
        
    def check_funds(self, amount):
        balance = self.get_balance()

        if(balance < amount):
            return False
        else:
            return True

    def __str__(self):
        lines = []

        # Título: 30 caracteres, nombre centrado entre *
        lines.append(self.name.center(30, '*'))

        # Cada transacción: descripción (máx 23, izquierda) + monto (7, derecha, 2 dec)
        for record in self.ledger:
            desc = record['description'][:23]
            amount = record['amount']
            lines.append(f"{desc:<23}{amount:>7.2f}")

        # Línea total
        lines.append(f"Total: {self.get_balance():.2f}")

        return '\n'.join(lines)   

def create_spend_chart(categories):
    withdrawals = []

    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])
        withdrawals.append(total)

    total_spent = sum(withdrawals)

    percentages = []
    for amount in withdrawals:
        percentage = int((amount / total_spent) * 100)
        percentages.append((percentage // 10) * 10)

    chart = "Percentage spent by category\n"

    for level in range(100, -1, -10):
        chart += f"{level:>3}| "

        for pct in percentages:
            if pct >= level:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(category.name) for category in categories)

    for i in range(max_len):
        chart += "     "

        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "

        if i != max_len - 1:
            chart += "\n"

    return chart

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)   