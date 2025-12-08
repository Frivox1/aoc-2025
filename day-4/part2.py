def read_matrix(filename):
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            row = list(line.strip())
            matrix.append(row)
    return matrix



def find_number_roll_of_paper(matrix):
    answer = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'Element at ({i}, {j}): {matrix[i][j]}')

            if matrix[i][j] == '@':
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[i]):
                            if matrix[ni][nj] == '@':
                                count += 1
                if count < 4:
                    answer += 1
                    
                    # I have to keep in memory that this cell needs to be "x" in a list of tuples
                    bad.append((i, j))
                    print("bad:", bad)

bad = []
matrix = read_matrix('example.txt')

find_number_roll_of_paper(matrix)


# while bad is not empty i have to relaunch find_number_roll_of_paper until no more bad cells are found
while bad:
    for (i, j) in bad:
        matrix[i][j] = 'x'  # Mark bad cells as 'x'
    bad = []  # Reset bad list
    find_number_roll_of_paper(matrix)

print("Final matrix:")
for row in matrix:
    print(''.join(row))

# answer is the number of 'x' in the matrix
answer = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'x':
            answer += 1
print(f'Final answer: {answer}')