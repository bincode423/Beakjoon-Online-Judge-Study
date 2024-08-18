import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip())

visit = [[0 for _ in range(m)] for _ in range(n)]
dq = deque([])

dq.append((0,0))
visit[0][0] = 1
direct = [(1,0),(0,1),(-1,0),(0,-1)]

while len(dq):
    x,y = dq[0]
    dq.popleft()
    for i in direct:
        nx,ny = x + i[0], y + i[1]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == '0' or visit[nx][ny] != 0:
            continue
        visit[nx][ny] = visit[x][y] + 1
        dq.append((nx,ny))
print(visit[n-1][m-1])