"""
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +
"""

input = []

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        print(line)
        # add each element in the line to a list
        input.append([int(x) if x.isdigit() else x for x in line.split()])


operators = input[-1]
values = input[:-1]

# Transpose rows columns 
# (asked chatgpt how to optimize the transpose function I wrote before)
columns = zip(*values)

results = []

for col_index, col in enumerate(columns):
    op = operators[col_index]

    if op == '*':
        result = 1
        for v in col:
            result *= v
    elif op == '+':
        result = sum(col)

    results.append(result)

print(sum(results))