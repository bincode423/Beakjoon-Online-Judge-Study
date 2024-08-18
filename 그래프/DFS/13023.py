def recu(idx,check):
    if len(check) == 5:
        return True
    for i in arr[idx]:
        if not(i in check):
            check.append(idx)
            if recu(i,check):
                return True
            check.pop()
    return False
n,m = map(int,input().split())
arr = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
t = 0
for num in range(n):
    if recu(num,[num]):
        t = 1
        print(1)
        break
if t == 0:
    print(0)