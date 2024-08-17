n = int(input())
nums = []
for i in range(n):
    nums.append(list(map(int,input().split())))
for i in range(n):
    print(f"Case #{i+1}: {nums[i][0]+nums[i][1]}")

#효율성 코드?
n = int(input())
for i in range(n):
    x = list(map(int,input().split()))
    print(f"Case #{i+1}: {x[0]+x[1]}")