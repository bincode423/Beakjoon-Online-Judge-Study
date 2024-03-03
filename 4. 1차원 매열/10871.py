a,b = map(int,input().split())
num_list = list(map(int,input().split()))
num_list = num_list[:a]

for num in num_list:
    if num < b:
        print(num,end=" ")