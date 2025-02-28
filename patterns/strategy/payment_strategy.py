"""
Description:
    Base class for Payment Strategy. Provides an interface for different
    payment strategies to implement.
"""

__author__ = "Your Name"
__version__ = "1.0.0"
# __credits__ = "ACE Faculty"  # Uncomment and add your name if you are editing existing ACE-provided code.

class PaymentStrategy:
    """
    A base class for payment strategies. Defines an interface
    for processing payments in various ways.
    """

    def process_payment(self, billing_account, payee, amount):
        """
        Processes a payment for a payee using the specified billing account.

        :param billing_account: The BillingAccount instance used to manage the payment.
        :param payee: The Payee (enum) that identifies which account is being paid.
        :param amount: The float amount to be paid.
        :return: A string message indicating the result of the payment operation.
        """
        raise NotImplementedError("Subclasses must override process_payment.")