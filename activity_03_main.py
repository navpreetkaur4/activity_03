"""A client program written to verify correctness of the activity 
classes.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from billing_account.billing_account import BillingAccount
from payee.payee import Payee

# Step 0: Import necessary classes for the Strategy Pattern
from payment.payment import Payment
from patterns.strategy.penalty_strategy import PenaltyStrategy
from patterns.strategy.partial_payment_strategy import PartialPaymentStrategy


def strategy():
    """Demonstrates the use of the classes defined in this activity."""
    
    print("STRATEGY PATTERN OUTPUT")

    # Given: Creates a BillingAccount object and 
    # adds the current balance owed for each utility.
    account = BillingAccount()
    account.add_balance(Payee.ELECTRICITY, 200.0)
    account.add_balance(Payee.INTERNET, 100.0)
    account.add_balance(Payee.TELEPHONE, 150.0)

    print("Initial Balances:")
    print(account, "\n")

    # 1. Create a Payment object with a PenaltyStrategy payment strategy.
    penalty_payment = Payment(PenaltyStrategy())

    # 2. Use the Payment object's pay_bill method to pay the ELECTRICITY
    # bill with an amount that does not pay off the entire balance shown
    # above - print the result of the pay_bill method.
    result_electricity = penalty_payment.pay_bill(account, Payee.ELECTRICITY, 50.0)
    print("PenaltyStrategy Payment on Electricity (partial):")
    print(result_electricity, "\n")

    # 3. Create a Payment object with a PartialPaymentStrategy payment 
    # strategy.
    partial_payment = Payment(PartialPaymentStrategy())

    # 4. Use the Payment object's pay_bill method to pay the TELEPHONE 
    # bill with an amount that does not pay off the entire balance shown
    # above - print the result of the pay_bill method.
    result_telephone_partial = partial_payment.pay_bill(account, Payee.TELEPHONE, 75.0)
    print("PartialPaymentStrategy Payment on Telephone (partial):")
    print(result_telephone_partial, "\n")

    # 5. Using the Payment object created in step 3, make another 
    # payment for the TELEPHONE bill with an amount that pays off the 
    # remainder of the balance - print the result of the pay_bill 
    # method.
    result_telephone_full = partial_payment.pay_bill(account, Payee.TELEPHONE, 75.0)
    print("PartialPaymentStrategy Payment on Telephone (full):")
    print(result_telephone_full, "\n")

    # 6. Print the BillingAccount object to show the updated balances 
    # for each of the payees.
    print("Updated Balances:")
    print(account)


if __name__ == "__main__":
    strategy()
