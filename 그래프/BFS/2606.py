from collections import deque
n, m = int(input()), int(input())
visited = [0 for _ in range(n+1)]
g = [[] for _ in range(n+1)]
q = deque()

for _ in range(m):
  u, v = map(int,input().split())
  g[u].append(v)
  g[v].append(u)
q.append(1)
visited[1] = 1

while q:
  v = q.popleft()
  for edge in g[v]:
    if visited[edge] == 0:
      visited[edge] = 1
      q.append(edge)
print(visited.count(1)-1)