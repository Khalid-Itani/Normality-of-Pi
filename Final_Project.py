import decimal

decimal.getcontext().prec = 5000

def pi_digit(n):
    pi = decimal.Decimal(0)
    k = 0
    while k < n:
        pi += (decimal.Decimal(1) / 16 ** k) * (decimal.Decimal(4) / (8 * k + 1) - decimal.Decimal(2) / (8 * k + 4) -decimal.Decimal(1) / (8 * k + 5) - decimal.Decimal(1) / (8 * k + 6)
        )
        k += 1
    return pi

pi_str = str(pi_digit(5000))

digit_counts = [(i, pi_str.count(str(i))) for i in range(10)]

print(pi_str[:5000])
print("Digit Counts:")
for digit, count in digit_counts:
    print(f"{digit}: {count} times")
