inputs = []

with open('input.txt', 'r') as file:
    for line in file:
        inputs.append(line.strip())

print("Input size:", len(inputs))

position = 50
answer = 0

for input in inputs:
    print('Processing input:', input)

    value = int(input[1:])

    if (len(input) > 3):
        answer += value // 100
        value = value % 100

    # when we go left from 0 we don't need to answer += 1
    if input[0] == 'L':

        if position == 0:
            answer -= 1

        position -= value

        if position < 0:
            print('Negative value detected:', position)
            position += 100
            print("adding 1 to answer")
            answer += 1
        


    elif input[0] == 'R':
        position += value

        if position > 100:
            print('Value exceeds 100:', position)
            position -= 100
            print("adding 1 to answer")
            answer += 1
        if position == 100:
            position = 0

    
    if position == 0:
        print("Position is zero, adding 1 to answer")
        answer += 1

    print("Current position:", position)
    print("\n")
    
print('Final position:', position)
print('Final answer:', answer)