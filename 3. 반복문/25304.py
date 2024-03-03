n = int(input())
a = int(input())
z = 0
for i in range(a):
    x,y = map(int,input().split())
    z += x*y
if z == n:
    print("Yes")
else:
    print("No")