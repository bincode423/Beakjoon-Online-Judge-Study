n = int(input())
num_list = list(map(int,input().split()))
num_list = num_list[:n]
M = max(num_list)

for index,num in enumerate(num_list):
    num_list[index] = num/M *100
print(sum(num_list)/len(num_list))