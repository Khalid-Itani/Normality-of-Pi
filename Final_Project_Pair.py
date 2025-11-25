import decimal

decimal.getcontext().prec = 5000

def pi_digit(n):
    pi = decimal.Decimal(0)
    k = 0
    while k < n:
        pi += (decimal.Decimal(1) / 16 ** k) * (
            decimal.Decimal(4) / (8 * k + 1) - decimal.Decimal(2) / (8 * k + 4) -
            decimal.Decimal(1) / (8 * k + 5) - decimal.Decimal(1) / (8 * k + 6)
        )
        k += 1
    return pi

# Calculate the first 10,000 digits of pi
pi_str = str(pi_digit(5000))

# Calculate the frequency of each two-digit pairing
pair_counts = {}
for i in range(10):
    for j in range(10):
        pair_counts[f"{i}{j}"] = pi_str.count(f"{i}{j}")

# Output the frequencies in CSV format
with open('pi_frequencies.csv', 'w') as f:
    f.write("Pair,Frequency\n")
    for pair, count in pair_counts.items():
        f.write(f"{pair},{count}\n")

print("Output saved to pi_frequencies.csv")
