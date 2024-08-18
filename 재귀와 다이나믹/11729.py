p = []
def recu(n,start,mid,end):
    if n == 1:
        p.append(f"{start} {end}")
        return
    recu(n-1, start, end, mid)
    p.append(f"{start} {end}")
    recu(n-1, mid, start, end)
n = int(input())
recu(n,1,2,3)
print(len(p))
print(*p,sep="\n")