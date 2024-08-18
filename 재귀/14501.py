def recu(day, sum):
    if day == n:
        return sum
    if day > n:
        return 0
    ans = 0
    ans = max(recu(day+t[day],sum+v[day]))
    ans = max(recu(day+1,sum))
    return ans


n = int(input())
t, v = [], []
for _ in range(n):
    tt, vv = map(int,input().split())
    t.append(tt)
    v.append(vv)
print(recu(0,0))
