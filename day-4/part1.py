def read_matrix(filename):
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            row = list(line.strip())
            matrix.append(row)
    return matrix

matrix = read_matrix('input.txt')

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

print(f'Final answer: {answer}')