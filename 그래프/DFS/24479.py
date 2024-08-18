import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
cnt = 0
def dfs(R):
    global cnt
    cnt += 1
    visited[R] = 1
    V[R] = cnt
    ee = sorted(E[R])
    for x in ee:
        if visited[x] ==0 :
            dfs(x)


n,m,r = map(int,input().split())
E = [[] for _ in range(n+1)]
V = [0]*(n+1)
visited = [0] * (n+1)
for _ in range(m):
    u, v = map(int,input().split())
    E[u].append(v)
    E[v].append(u)
dfs(r)
for i in V[1:]:
    print(i)