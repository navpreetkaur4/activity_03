"""
Description:
    Implements a partial payment strategy that allows a portion of the
    amount due to be paid without penalty.
"""

__author__ = "Your Name"
__version__ = "1.0.0"
# __credits__ = "ACE Faculty"

from .payment_strategy import PaymentStrategy


class PartialPaymentStrategy(PaymentStrategy):
    """
    Processes partial payments without applying any penalties.
    """

    def process_payment(self, billing_account, payee, amount):
        """
        Deducts the specified payment amount from the payee's balance.
        If the new balance is zero or less, the bill is considered fully paid.
        Otherwise, it is considered a partial payment.

        :param billing_account: The BillingAccount instance used to manage the payment.
        :param payee: The Payee (enum) that identifies which account is being paid.
        :param amount: The float amount to be paid.
        :return: A string indicating the result of the payment operation.
        """
        # Deduct the payment from the balance
        billing_account.deduct_balance(payee, amount)

        # Check the updated balance
        balance = billing_account.get_balance(payee)

        # If balance is 0 or less, the entire bill is paid off
        if balance <= 0:
            return f"Processed payment of ${amount:.2f}. New balance: $0.00."
        else:
            # Partial payment
            return f"Partial payment of ${amount:.2f} accepted. New balance: ${balance:.2f}."
