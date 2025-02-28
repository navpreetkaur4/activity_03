"""
Description:
    Defines the Payment class, which uses a PaymentStrategy to process payments.
"""

__author__ = "Navpreet"
__version__ = "1.0.0"
# __credits__ = "ACE Faculty"

from patterns.strategy.payment_strategy import PaymentStrategy


class Payment:
    """
    Manages the process of paying a bill using a specified PaymentStrategy.
    """

    def __init__(self, strategy):
        """
        Initializes the Payment with the given strategy.

        :param strategy: An instance of PaymentStrategy (or a subclass).
        :raises ValueError: If the provided strategy is not a PaymentStrategy instance.
        """
        if not isinstance(strategy, PaymentStrategy):
            raise ValueError("Invalid Strategy")
        self.strategy = strategy

    def pay_bill(self, billing_account, payee, amount):
        """
        Uses the assigned strategy to process a payment.

        :param billing_account: The BillingAccount instance used to manage the payment.
        :param payee: The Payee (enum) that identifies which account is being paid.
        :param amount: The float amount to be paid.
        :return: A string message indicating the result of the payment operation.
        """
        return self.strategy.process_payment(billing_account, payee, amount)
