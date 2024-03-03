n = int(input())
num_list = list(map(int,input().split()))
num_list = num_list[:n]
v = int(input())

print(num_list.count(v))