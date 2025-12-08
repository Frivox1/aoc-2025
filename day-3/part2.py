input = []
answer = 0

with open("input.txt") as f:
    for line in f:
        input.append(line.strip())



for line in input:
    stack = []
    length = 12
    for i in range(len(line)):
        c = line[i]
        print("Considering:", c, "at", i)
        while (len(stack) + (len(line) - i) > length and
               len(stack) > 0 and
               stack[-1] < c):
            print("  Popping:", stack[-1])
            stack.pop()
        if len(stack) < length:
            stack.append(c)
            print("  Pushing:", c)
        print("  Stack now:", stack)
    number = ''.join(stack)
    answer += int(number)


    

print("Answer:", answer)

print(answer == 3121910778619)