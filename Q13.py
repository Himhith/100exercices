# Write a program that accepts a sentence and calculate the number of letters and digits.
#
# Suppose the following input is supplied to the program:
#
# hello world! 123
# Then, the output should be:
#
# LETTERS 10
# DIGITS 3

inp=input()

print(type(inp))
alpha_index=0
digit_index=0
#print(inp(3))
for index in range(len(inp)):
    if inp[index].isalpha():
        alpha_index += 1
for index in range(len(inp)):
    if inp[index].isdigit():
        digit_index += 1

print(f"ALPHA {alpha_index} \n"
      f"DIGITS {digit_index}")
