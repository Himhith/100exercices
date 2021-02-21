# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

# Suppose the following input is supplied to the program:

# 9
# Then, the output should be:

# 11106


inp=int(input())


# print(inp*11)
print(inp+(inp*11)+(inp*111)+(inp*1111))

