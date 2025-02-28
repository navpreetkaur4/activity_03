"""
Description:
    Implements a penalty strategy that applies a fixed $10.00 fee if
    the payment is insufficient to cover the total amount due.
"""

__author__ = "Your Name"
__version__ = "1.0.0"
# __credits__ = "ACE Faculty"

from .payment_strategy import PaymentStrategy


class PenaltyStrategy(PaymentStrategy):
    """
    Processes payments and applies a fixed penalty if the amount does not
    cover the full balance.
    """

    def process_payment(self, billing_account, payee, amount):
        """
        Deducts the specified payment amount from the payee's balance.
        If the new balance is zero or less, the bill is considered fully paid.
        Otherwise, a $10 penalty is applied to the account.

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
            # Payment insufficient - apply penalty
            billing_account.add_balance(payee, 10.00)
            new_balance = billing_account.get_balance(payee)
            return (f"Insufficient payment. Added penalty fee of $10.00. "
                    f"New balance: ${new_balance:.2f}.")
