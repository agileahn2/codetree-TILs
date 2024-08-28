#마름모 모양 채굴, 금 개수 리턴
def mine(K, x, y, n, g):
    gold = 0
    for i, ii in zip(range(y - K, y + K + 1), list(range(K)) + list(range(K, -1, -1))):
        for j in range(x - ii, x + ii + 1):
            if 0 <= i < n and 0 <= j < n:
                if g[i][j] == 1:
                    gold += 1
    return gold



n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

Max = 0
#K∗K+(K+1)∗(K+1)
K_Cal = lambda x : x*x+(x+1)*(x+1)
g_n = 0 #gold num
m_g = 0 #g_n * m
K_R = 0 #rejult

for L in range(n - n%2 + 1): #
    for i in range(n - int(L /2)):
        for j in range(n - int(L/2)):
            g_n = mine(L, j, i, n, g)
            m_g = g_n * m
            K_R = K_Cal(L)
            if K_R < m_g and Max < g_n:
                Max = g_n

print(Max)



#print(mine(1, 4, 4, 5, g))