"""Test of the CreditCalculator class"""

from credit_calculator import CreditCalculator

calculator1 = CreditCalculator(payment_type="annuity", principal=1000000, periods=60, interest=10)
calculator1.start()

print()

calculator2 = CreditCalculator(payment_type="diff", principal=500000, periods=8, interest=7.8)
calculator2.start()

print()

calculator3 = CreditCalculator(payment_type="annuity", payment=8722, periods=120, interest=5.6)
calculator3.start()

print()

calculator4 = CreditCalculator(payment_type="annuity", principal=500000, payment=23000, interest=7.8)
calculator4.start()
