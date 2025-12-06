input = []
answer = 0

with open("input.txt") as f:
    for line in f:
        input.append(line.strip())



for line in input:
    current_max = 0
    for i in range (0, len(line)-1):
        for j in range (i + 1, len(line)):
            value = int(line[i] + line[j])
            if value > current_max:
                current_max = value
            
    answer += current_max

print("Answer:", answer)