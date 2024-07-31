n, m = map(int, input().split())
m -= 1
grid = [list(map(int, input().split())) for _ in range(n)]

temp = 0
count = 0
answer = 0
for i in range(n):
    temp = grid[i][0]
    for j in range(1, n):
        if grid[i][j] == temp:
            count += 1
        else:
            temp = grid[i][j]
            count = 0
        if count == m:
            answer += 1
            count = 0
            break

for j in range(n):
    temp = grid[0][j]
    for i in range(1, n):
        if grid[i][j] == temp:
            count += 1
        else:
            temp = grid[i][j]
            count = 0
        if count == m:
            answer += 1
            count = 0
            break
if n == 1:
    if m == 0:
        print(2)
    else:
        print(0)
else:
    print(answer)