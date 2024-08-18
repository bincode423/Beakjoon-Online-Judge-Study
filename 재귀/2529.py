n = int(input())
l = input().split()
checker = [0] * 10
ans_pool = []
def good(x,y,op):
    if op==">"and x>y: return True
    if op=="<"and x<y: return True
    return False
def recu(idx, nums):
    if idx==n+1:
        ans_pool.append(nums)
        return
    for i in range(10):
        if checker[i]: continue
        if idx==0 or (good(nums[-1], str(i), l[idx-1])):
            checker[i] = 1
            recu(idx+1, nums+str(i))
            checker[i] = 0
recu(0, '')
print(ans_pool[0])
print(ans_pool[-1])