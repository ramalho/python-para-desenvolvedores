from decimal import Decimal

t = 5.

for i in range(50):
    t = t - 0.1

print('Float:', t)

t = Decimal('5.')

for i in range(50):
    t = t - Decimal('0.1')

print('Decimal:', t)
