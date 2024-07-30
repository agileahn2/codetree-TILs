N = int(input())
grid = [list(map(int, input().split()))for _ in range(N)]

Max = 0
Temp = 0
count = 0
loop = (N - 2)*(N - 2) # - 3 + 1
while(True):
    if count == loop:
        break
    for i, g in zip(range(N), grid):
        for n, j in enumerate(g):
            if n > N + i:
                break
            Temp += j
    if Temp > Max:
        Max = Temp
        Temp = 0
    count += 1
print(Max)