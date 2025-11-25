Normality of Pi

This project explores whether the digits of π exhibit normality in base 10 and base 16. A number is normal if every digit and finite sequence of digits occurs with equal limiting frequency. Although no formal proof exists, large computational studies suggest π behaves like a normal number. This project analyzes digit distributions using the Bailey-Borwein-Plouffe (BBP) algorithm, which can compute the nth hexadecimal digit of π without needing earlier digits.

Project Goals

Compute digits of π using the BBP digit extraction algorithm

Analyze digit frequencies in base 10

Analyze digit pair frequencies (00 to 99)

Analyze hexadecimal digit frequencies

Visualize distributions with bar graphs

Compare results to expected normal distributions

Discuss how findings relate to the normality conjecture

Files Included

Final_Project.py – Computes base 10 digit frequencies
Final_Project_Pair.py – Computes two digit sequence frequencies
Final_Project_Hex.py – Computes hexadecimal digits
Final_Project_Graph.py – Visualization support
pi_frequencies.csv – Single digit frequencies
pi_hexadecimal_output.csv – Hexadecimal digits

Methodology
Digit Extraction

Digits of π are computed using the BBP algorithm, allowing digit by digit extraction where each digit is independent of previous ones.

Frequency Analysis

The program counts each digit (in base 10 or base 16), computes relative frequencies, and compares them to the expected uniform distribution. This is repeated for:

Base 10 single digits

Base 10 two digit sequences

Base 16 digits

Visualization

Matplotlib bar graphs show:

Actual frequencies

Expected frequencies

How distributions trend toward uniformity as sample size increases

Results Summary

Across all tests, π behaves in a way consistent with normality:

Base 10 digits are near uniform

Two digit sequences approximate expected distribution

Hex digits appear uniformly distributed

Larger sample sizes move closer to uniformity

These results support the conjecture that π behaves like a normal number, although they do not prove it.

Important Note

This project does not prove π is normal. Normality is a global property that cannot be confirmed with finite data. Instead, this project provides empirical evidence that π behaves like a normal number in multiple bases.

How to Run
git clone https://github.com/Khalid-Itani/Normality-of-Pi.git
pip install numpy matplotlib
python Final_Project.py
python Final_Project_Pair.py
python Final_Project_Hex.py

References

Bailey, Borwein, Plouffe. “BBP Algorithm”

SAS Blog: Digit Frequency Analysis of Pi

Various computational studies of π digit distribution
