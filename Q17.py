# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:

# D 300
# D 300
# W 200
# D 100
# Then, the output should be:

# 500
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

# text = '\n'.join(lines)
# inp=[n.split(',') for n in (input().split('\n')]
print(lines)

lines = [line.split(' ') for line in lines]
net = 0
for value in lines:
    if (value[0] == 'W'):
        net -= int(value[1])
    elif (value[0] == 'D'):
        net += int(value[1])
# print(lines)

print(net)
