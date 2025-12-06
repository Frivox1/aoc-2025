inputs = []
answer = 0

with open('input.txt', 'r') as file:
    contents = file.read()
    inputs = contents.split(',')
    
for input in inputs:
    print(input)

    start = input.split('-')[0]
    # print(f'Start: {start}')

    end = input.split('-')[1]
    # print(f'End: {end}')

    for number in range(int(start), int(end) + 1):
        str_number = str(number)
        length = len(str_number)

        invalid = False

        # Try different pattern sizes
        # If number is "123123", try pattern size 1, 2, 3
        for size in range(1, length // 2 + 1):
            if length % size == 0:
                pattern = str_number[0:size]
                repetitions = length // size
                if pattern * repetitions == str_number:
                    invalid = True
                    break

        if invalid:
            print(number)
            answer += number

print ('Answer:', answer)