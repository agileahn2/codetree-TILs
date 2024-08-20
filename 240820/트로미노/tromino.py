n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

MAX = 0
temp = 0

#가로
for i in range(n - 2):
    for j in range(m):
        for k in range(3):
            temp += g[i + k][j]
        if MAX < temp:
            MAX = temp
        temp = 0

#세로
for i in range(n):
    for j in range(m - 2):
        for k in range(3):
            temp += g[i][j + k]
        if MAX < temp:
            MAX = temp
        temp = 0


#ㄴ
s = []
for i in range(n - 1):
    for j in range(m - 1):
        for k in range(2):
            s.append( g[i][j + k] )
            s.append( g[i + 1][j + k] )
            temp = sum(s)
        for k in range(4):
            tempK = temp - s[k]
            if MAX < tempK:
                MAX = tempK
        temp = 0
        s = []      

print(MAX)