import matplotlib.pyplot as plt

# Output from the previous code
pi_decimal_str = str(pi_decimal)[:1000]

# Count the frequency of each digit (0-9)
digit_counts = [pi_decimal_str.count(str(i)) for i in range(10)]

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.bar(range(10), digit_counts, color='skyblue')
plt.xlabel('Digit')
plt.ylabel('Frequency')
plt.title('Frequency of Each Digit in the First 1000 Digits of Pi')
plt.xticks(range(10))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
