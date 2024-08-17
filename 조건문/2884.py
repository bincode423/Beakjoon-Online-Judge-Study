x,y = map(int,input().split())
if y < 45:
    y += 60
    if x == 0:
        x = 24
    x -= 1
y -= 45
print(x,y)