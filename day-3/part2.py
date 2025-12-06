input = []
answer = 0

with open("small.txt") as f:
    for line in f:
        input.append(line.strip())



for line in input:
    digits = [(int(line[i]), i) for i in range(len(line))]
    digits.sort(reverse=True, key=lambda x: x[0])
    print("digits:", digits)
    

print("Answer:", answer)