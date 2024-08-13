from collections import defaultdict

__author__ = "Agrim"
__version__ = "1.0"
__description__ = ("A Python class to manage shared expenses among a group of people, tracking individual balances and "
                   "detailed transactions.")


class ExpenseManager:
    """
    A class to manage and track shared expenses among a group of people.

    Attributes:
    balances (dict): Stores the net balance of each person.
    transactions (dict): Stores detailed transactions of who owes whom and for what.

    Methods:
    add_expense(payer, amount, participants, item=None):
        Adds an expense to the system, splits it among participants, and updates balances and transactions.

    get_balances():
        Returns the net balances of all participants.

    get_transactions():
        Returns the detailed transactions of all participants.

    display_balances():
        Prints the net balance of each participant, showing who is owed and who owes money.

    display_transactions():
        Prints detailed transactions and a summary of total amounts owed between participants.
    """

    def __init__(self):
        self.balances = defaultdict(float)
        self.transactions = defaultdict(lambda: defaultdict(float))

    def add_expense(self, payer, amount, participants, item=None):
        """
        Adds an expense to the system, splits it among participants, and updates balances and transactions.

        Args:
        payer (str): The name of the person who paid the expense.
        amount (float): The total amount of the expense.
        participants (list): The names of the people sharing the expense.
        item (str, optional): A description of the item or service paid for. Defaults to 'Unknown item'.
        """
        split_amount = amount / len(participants)
        self.balances[payer] += amount  # The payer gets the full amount added to their balance
        for person in participants:
            if person != payer:
                self.balances[person] -= split_amount
                self.balances[payer] -= split_amount
                if item:
                    self.transactions[person][payer] += split_amount
                else:
                    self.transactions[person][payer] += split_amount

    def get_balances(self):
        """
        Returns the net balances of all participants.

        Returns:
        dict: A dictionary of participants and their net balances.
        """
        return dict(self.balances)

    def get_transactions(self):
        """
        Returns the detailed transactions of all participants.

        Returns:
        dict: A dictionary of participants and their detailed transactions.
        """
        return dict(self.transactions)

    def display_balances(self):
        """
        Prints the net balance of each participant, showing who is owed and who owes money.
        """
        for person, balance in self.balances.items():
            if balance > 0:
                print(f"{person} is owed {balance:.2f} INR.")
            elif balance < 0:
                print(f"{person} owes {-balance:.2f} INR.")
            else:
                print(f"{person} is settled up.")

    def display_transactions(self):
        """
        Prints detailed transactions and a summary of total amounts owed between participants.
        """
        total_debts = defaultdict(lambda: defaultdict(float))

        # Aggregate transactions between participants
        for person, debts in self.transactions.items():
            for payer, amount in debts.items():
                total_debts[person][payer] += amount
                total_debts[payer][person] -= amount

        # Display individual transactions
        print("\nDetailed Transactions:")
        for person, debts in total_debts.items():
            for payer, amount in debts.items():
                if amount > 0:
                    print(f"{person} owes {payer} {amount:.2f} INR.")

        # Display the summary of total amounts owed
        print("\nSummary of Total Amounts Owed:")
        for person, debts in total_debts.items():
            for payer, total_amount in debts.items():
                if total_amount > 0:
                    print(f"{person} owes {payer} a total of {total_amount:.2f} INR.")


# Usage example
if __name__ == "__main__":
    expense_manager = ExpenseManager()

    # Add expenses
    expense_manager.add_expense('Agrim', 3073, ['Agrim', 'Geet', 'Ashish', 'Kartik', 'Lavisha'], 'Diesel')
    expense_manager.add_expense('Agrim', 976, ['Agrim', 'Geet', 'Ashish', 'Kartik', 'Lavisha'], 'Breakfast A2B')

    # Display the final balances
    expense_manager.display_balances()

    # Display individual transactions
    expense_manager.display_transactions()
