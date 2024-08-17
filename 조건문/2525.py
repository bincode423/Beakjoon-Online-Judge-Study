x,y = map(int,input().split())
z = int(input())
y += z
x += y//60
y %= 60
if x > 23:
    x -= 24
print(x,y)