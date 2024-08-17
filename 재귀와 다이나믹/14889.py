n = int(input())
link = []
for _ in range(n):
    link.append(list(map(int,input().split())))

def sinulge(arr):
    r = 0
    for a in arr:
        for b in arr:
            r += link[a][b]
    return r

miner = ["Error"]
def pair(idx,left, right):
    if idx==n:
        if len(left) == len(right):
            if miner[0] == "Error":
                miner[0] = abs(sinulge(left)-sinulge(right))
            else:
                miner[0] = min(abs(sinulge(left)-sinulge(right)),miner[0])
        return
    pair(idx+1, left+[idx], right)
    pair(idx+1 , left, right+[idx])
    
pair(0,[],[])
print(miner[0])