
def diagonalDifference(n, matrix):
    main_diagnol = []
    second_diagnol = []

    for i in range(n):
        main_diagnol.append(matrix[i][i])
        second_diagnol.append(matrix[i][n-1-i])

    return abs(sum(main_diagnol) - sum(second_diagnol))

matrix = []
n = int(input())

for _ in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)

print(diagonalDifference(n, matrix))