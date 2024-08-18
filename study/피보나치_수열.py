#과정
def recu1(n,a,b):
    if n == 0:
        return
    a,b = b,a+b
    print(b)
    recu1(n-1,a,b)
n = int(input())
if n == 1:
    print("1")
elif n == 2:
    print("1 1")
else:
    recu1(n-2,1,1)

#결과
memo = {}
def recu2(n):
    if n==0: return 0
    if n==1: return 1
    if n in memo: return memo[n]

    memo[n] = recu2(n-1)+recu2(n-2)
    return memo[n]
n = int(input())
print(recu2(n))