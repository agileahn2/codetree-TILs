n = int(input())
sq = [ list(map(int, input().split())) for _ in range(n)]

X = [-1, 1, 1,-1]
Y = [ 1, 1,-1,-1]

mx = 0
tmp = 0

for i in range(0, n-2):
    for j in range(1, n-1):
        x = j
        y = i
        for k in range(4):
            while(True):
                x = x + X[k]
                y = y + Y[k]
                if(not(0 <= x < n and 0 <= y < n)):
                    x = x - X[k]
                    y = y - Y[k]
                    break
                tmp = tmp + sq[y][x]
        if(mx < tmp):
            mx = tmp
        tmp = 0

print(mx)





