N = int(input())
grid = [list(map(int, input().split()))for _ in range(N)]

Max = 0
Temp = 0
loop = (N - 2) # - 3 + 1

for I in range(loop):
    for J in range(loop):
        for i in range(I, 3+I):
            for j in range(J, 3+J):
                Temp += grid[i][j]

        if Max < Temp:
            Max = Temp
        Temp = 0


print(Max)