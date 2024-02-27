n = int(input())
nums = []
for i in range(n):
    nums.append(list(map(int,input().split())))
for i in range(n):
    print(f"Case #{i+1}: {nums[i][0]+nums[i][1]}")
