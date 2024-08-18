def dfs(y,x):
    went[y][x] = 1
    sumer = 0
    if y+1 < n and apart[y+1][x] == 1 and went[y+1][x] == 0:
        sumer += dfs(y+1,x)
    if y-1 >= 0  and apart[y-1][x] == 1 and went[y-1][x] == 0:
        sumer += dfs(y-1,x)
    if x+1 < n and apart[y][x+1] == 1 and went[y][x+1] == 0:
        sumer += dfs(y,x+1)
    if x-1 >= 0 and apart[y][x-1] == 1 and went[y][x-1] == 0:
        sumer += dfs(y,x-1)
    return sumer+1

n = int(input())
apart = [list(map(int,input())) for _ in range(n)]
went = [[0 for _ in range(n)] for _ in range(n)]

arr = []
for y in range(n):
    for x in range(n):
        if apart[y][x] == 1 and went[y][x] == 0:
            arr.append(dfs(y,x))
print(len(arr))
arr.sort()
print(*arr,sep='\n')