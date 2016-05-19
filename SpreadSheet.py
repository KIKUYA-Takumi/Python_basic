r,c = map(int,input().split())
matrix = [[0 for i in range(c)]for j in range(r)]
for x in range(r):
    matrix[x][:c] = map(int,input().split())

for i in range(r):
    totalc = 0
    for j in range(c):
        totalc += matrix[i][j]
    matrix[i][j].append(totalc)

for i in range(c):
    totalr = 0
    for j in range(r):
        totalr += matrix[j][i]
    matrix[j].append(totalr)

print(matrix)


