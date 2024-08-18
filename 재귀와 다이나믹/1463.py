#n부터 내려가는 방식
import sys
sys.setrecursionlimit(10**6)
pair = {1:0,2:1,3:1}
def recu(n):
    if n in pair: return pair[n]
    pair[n] = 99999999999999
    if n%3 == 0 and n%2 == 0:
        pair[n] = min(recu(n//3)+1, recu(n//2)+1)
    elif n%3 == 0:
        pair[n] = min(recu(n-1)+1, recu(n//3)+1)
    elif n%2 == 0:
        pair[n] = min(recu(n-1)+1, recu(n//2)+1)
    else:
        pair[n] = recu(n-1)+1
    return pair[n]
n = int(input())
print(recu(n))

# 1부터 거슬러 올라가는 방식
n = int(input())
D = [ 0 for i in range(n+1)]
D[1] = 0
D[2] = 1
D[3] = 1
for i in range(4,n+1):
    D[i] = D[i-1]+1
    if i%2==0:
        D[i] = min(D[i],D[i//2]+1)
    if i%3==0:
        D[i] = min(D[i],D[i//3]+1)
print(D[-1])