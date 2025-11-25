import decimal

decimal.getcontext().prec = 1000

def pi_digit(n):
    pi = decimal.Decimal(0)
    k = 0
    while k < n:
        pi += (decimal.Decimal(1) / 16 ** k) * (
            decimal.Decimal(4) / (8 * k + 1) - decimal.Decimal(2) / (8 * k + 4) -decimal.Decimal(1) / (8 * k + 5) - decimal.Decimal(1) / (8 * k + 6))
        k += 1
    return pi

pi_decimal = pi_digit(1000)

pi_integer_hex = hex(int(pi_decimal))[2:]

pi_fractional_hex = ''
fractional_part = pi_decimal - int(pi_decimal)
for _ in range(1000):
    fractional_part *= 16
    digit = int(fractional_part)
    pi_fractional_hex += hex(digit)[2:]
    fractional_part -= digit

pi_hex = pi_integer_hex + '.' + pi_fractional_hex

frequency_counter = {}
for digit_or_letter in pi_hex:
    if digit_or_letter in frequency_counter:
        frequency_counter[digit_or_letter] += 1
    else:
        frequency_counter[digit_or_letter] = 1
