# Intermediate Software Development Activity 3

This activity will help to reinforce learning of the **Module 3** concepts of:
- **Design Patterns** (focusing on the Strategy Pattern)

By using different payment strategies (e.g., Partial Payment, Penalty Payment), 
we avoid code duplication and maintain a cleaner, more extensible codebase.

## Author

Navpreet kaur

## Overview

In this activity, we implement a **Strategy Pattern** to handle various billing scenarios:
1. **PartialPaymentStrategy**: Accept partial bill payments without applying penalties.
2. **PenaltyStrategy**: Applies a penalty fee for insufficient payments.
3. **Payment** class: Accepts a strategy at initialization and delegates payment logic to that strategy.

The `BillingAccount` class stores and manages balances for different `Payee` types, 
and the `Payment` class leverages a chosen strategy to adjust those balances accordingly.

## Additional Information

1. **PEP 8 Compliance**:  
   - Followed proper naming conventions, added docstrings to classes and methods, 
     and used consistent indentation.
   
2. **Exception Handling**:  
   - Ensured that a `ValueError` is raised if an invalid strategy is passed to `Payment`.
   - Handled partial and penalty logic gracefully to avoid unexpected application errors.

3. **Modular Structure**:  
   - Organized the code into separate directories (`billing_account`, `payee`, `payment`, and `patterns/strategy`) 
     for maintainability and clarity.

