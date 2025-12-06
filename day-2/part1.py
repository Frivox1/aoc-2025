inputs = []
answer = 0

with open('input.txt', 'r') as file:
    contents = file.read()
    inputs = contents.split(',')
    
for input in inputs:
    print(input)

    start = input.split('-')[0]
    # print("Start", start)

    end = input.split('-')[1]
    # print("End:", end)


    for i in range(int(start), int(end) + 1):
        if len(str(i)) % 2 != 0:
            continue
        else:
            num_str = str(i)
            mid = len(num_str) // 2
            first_half = num_str[:mid]
            second_half = num_str[mid:]
            if first_half == second_half:
                print(i)
                answer += i

    # print("\n")

print ('Answer:', answer)

# print (answer == 1227775554)