cnt = -1
def dfs(R):
    global cnt
    cnt += 1
    visited[R] = 1
    for x in E[R]:
       if visited[x] ==0 :dfs(x)

n, m = int(input()), int(input())
E = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    u, v = map(int,input().split())
    E[u].append(v)
    E[v].append(u)
dfs(1)
print(cnt)