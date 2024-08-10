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
    expense_manager.add_expense('Lavisha', 145, ['Ashish', 'Kartik', 'Lavisha', 'Agrim', 'Geet'], 'Trin Cafe')
    expense_manager.add_expense('Ashish', 40, ['Ashish', 'Kartik', 'Lavisha', 'Agrim', 'Geet'], 'Water bottles')
    expense_manager.add_expense('Lavisha', 80, ['Lavisha', 'Geet'], 'Trindavanam Cafe')
    expense_manager.add_expense('Kartik', 100, ['Kartik', 'Lavisha'], 'Ice Cream')
    expense_manager.add_expense('Lavisha', 60, ['Agrim', 'Geet', 'Ashish', 'Kartik', 'Lavisha'], 'Shore Temple Parking')
    expense_manager.add_expense('Lavisha', 200, ['Agrim', 'Geet', 'Ashish', 'Kartik', 'Lavisha'],
                                'Entry Tickets Mallapuram')
    expense_manager.add_expense('Lavisha', 100, ['Geet', 'Kartik'], 'Coconut Water')
    expense_manager.add_expense('Lavisha', 1139, ['Agrim', 'Geet', 'Ashish', 'Kartik', 'Lavisha'],
                                'Lunch Mahabalipuram')
    expense_manager.add_expense('Lavisha', 455, ['Ashish', 'Lavisha'], 'Marc Cafe')
    expense_manager.add_expense('Lavisha', 200, ['Kartik'], 'Marc Cafe')
    expense_manager.add_expense('Lavisha', 290, ['Geet', 'Agrim'], 'Marc Cafe')
    expense_manager.add_expense('Lavisha', 139, ['Geet'], 'Baker St. Cinamon Roll')
    expense_manager.add_expense('Lavisha', 318, ['Agrim'], 'Sarguru Lunch')
    expense_manager.add_expense('Lavisha', 186, ['Geet'], 'Sarguru Lunch')
    expense_manager.add_expense('Lavisha', 153, ['Kartik'], 'Sarguru Lunch')
    expense_manager.add_expense('Lavisha', 410, ['Ashish', 'Lavisha'], 'Sarguru Lunch')
    expense_manager.add_expense('Lavisha', 54, ['Agrim', 'Geet', 'Ashish', 'Kartik', 'Lavisha'], 'Sarguru Lunch GST')
    expense_manager.add_expense('Lavisha', 150, ['Agrim', 'Geet', 'Ashish', 'Kartik', 'Lavisha'], 'Auroville Parking')
    expense_manager.add_expense('Lavisha', 647, ['Kartik'], 'Zomato Dinner')
    expense_manager.add_expense('Lavisha', 1158, ['Geet'], 'Maxx Shopping')
    expense_manager.add_expense('Ashish', 2110, ['Agrim', 'Geet', 'Ashish', 'Kartik', 'Lavisha'], 'Diesel 2nd time')
    expense_manager.add_expense('Ashish', 970, ['Ashish', 'Lavisha'], 'Baker Street Packing')
    expense_manager.add_expense('Lavisha', 2242, ['Agrim', 'Geet', 'Ashish', 'Kartik', 'Lavisha'], 'Dillwala6 Dinner')
    expense_manager.add_expense('Ashish', 350, ['Kartik'], 'B & C Breakfast')
    expense_manager.add_expense('Ashish', 660, ['Lavisha'], 'B & C Breakfast')
    expense_manager.add_expense('Ashish', 180, ['Geet'], 'B & C Breakfast')
    expense_manager.add_expense('Ashish', 310, ['Agrim'], 'B & C Breakfast')
    expense_manager.add_expense('Ashish', 560, ['Ashish'], 'B & C Breakfast')
    expense_manager.add_expense('Ashish', 98, ['Agrim', 'Geet', 'Ashish', 'Kartik', 'Lavisha'], 'B & C Breakfast GST')
    expense_manager.add_expense('Lavisha', 470, ['Agrim', 'Geet'], 'Aishwarya Bhawan Lunch')
    expense_manager.add_expense('Lavisha', 465, ['Ashish', 'Lavisha'], 'Aishwarya Bhawan Lunch')
    expense_manager.add_expense('Lavisha', 290, ['Kartik'], 'Aishwarya Bhawan Lunch')
    expense_manager.add_expense('Lavisha', 1770, ['Agrim', 'Geet', 'Ashish', 'Kartik', 'Lavisha'],
                                'Boating Charges Paradise Beach')
    expense_manager.add_expense('Ashish', 103, ['Agrim', 'Geet', 'Ashish', 'Kartik', 'Lavisha'],
                                'Paradise Beach Parking')
    expense_manager.add_expense('Ashish', 13171, ['Agrim', 'Geet', 'Ashish', 'Kartik', 'Lavisha'], 'Revv Car')
    expense_manager.add_expense('Agrim', 890, ['Geet', 'Lavisha'], 'Sula Wine')
    expense_manager.add_expense('Agrim', 2700, ['Kartik', 'Agrim'], 'Jamison')
    expense_manager.add_expense('Agrim', 520, ['Kartik'], '4 Beers Budwiser')
    expense_manager.add_expense('Agrim', 160, ['Ashish'], 'Amstel Beer')
    expense_manager.add_expense('Lavisha', 2242, ['Geet', 'Lavisha'], 'Wine')
    expense_manager.add_expense('Lavisha', 1542, ['Geet'], 'Red Wine')
    expense_manager.add_expense('Geet', 9080, ['Geet', 'Agrim'], '4 Seasons Stay')
    expense_manager.add_expense('Agrim', 250, ['Geet'], 'Veg Biryani from Madras Wedding Biryani')
    expense_manager.add_expense('Agrim', 780, ['Agrim', 'Geet'], 'Baker Street')
    expense_manager.add_expense('Agrim', 360, ['Geet'], 'Zomato Biryani')
    expense_manager.add_expense('Ashish', 258, ['Lavisha'], 'Auroville Bakery')
    expense_manager.add_expense('Ashish', 210, ['Ashish'], 'Auroville Bakery')
    expense_manager.add_expense('Ashish', 132, ['Geet'], 'Auroville Bakery')
    expense_manager.add_expense('Ashish', 265, ['Agrim'], 'Auroville Bakery')
    expense_manager.add_expense('Ashish', 250, ['Kartik'], 'Auroville Bakery')
    expense_manager.add_expense('Ashish', 53, ['Agrim', 'Geet', 'Ashish', 'Kartik', 'Lavisha'], 'Auroville Bakery GST')
    expense_manager.add_expense('Lavisha', 470, ['Geet', 'Ashish', 'Lavisha'], 'Tanto Veg Pizza')
    expense_manager.add_expense('Lavisha', 550, ['Agrim', 'Kartik'], 'Tanto Chicken Pizza')
    expense_manager.add_expense('Ashish', 51, ['Agrim', 'Geet', 'Ashish', 'Kartik', 'Lavisha'], 'Tanto GST')
    expense_manager.add_expense('Agrim', 450, ['Kartik'], 'Zomato Chicken Biryani')
    expense_manager.add_expense('Ashish', 133, ['Geet'], 'Baker Street')
    expense_manager.add_expense('Ashish', 76, ['Kartik'], 'Baker Street')
    expense_manager.add_expense('Lavisha', 60, ['Geet'], 'Bakery')

    # Display the final balances
    expense_manager.display_balances()

    # Display individual transactions
    expense_manager.display_transactions()
