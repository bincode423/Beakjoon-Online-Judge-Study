def recu(sumer, goal):
    if sumer==goal: return 1
    if sumer>goal: return 0
    ans = 0
    for i in range(1,4):
        ans += recu(sumer+i, goal)
    return ans

n = int(input())
for _ in range(n):
    print(recu(0,int(input())))