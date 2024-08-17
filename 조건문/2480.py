a,b,c = map(int,input().split())
if a == b and b == c:
    print((a*1000)+10000)
elif a == b:
    print(1000+a*100)
elif b == c:
    print(1000+c*100)
elif a == c:
    print(1000+c*100)
else:
    print(max(a,b,c)*100)