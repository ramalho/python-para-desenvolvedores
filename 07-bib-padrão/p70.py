from fractions import Fraction

# Três frações
f1 = Fraction('-2/3')
f2 = Fraction(3, 4)
f3 = Fraction('.25')

print("Fraction('-2/3') =", f1)
print("Fraction('3, 4') =", f2)
print("Fraction('.25') =", f3)

# Soma
print(f1, '+', f2, '=', f1 + f2)
print(f2, '+', f3, '=', f2 + f3)
