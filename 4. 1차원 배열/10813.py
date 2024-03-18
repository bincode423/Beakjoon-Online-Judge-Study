a,b = map(int,input().split())
return_list = list(range(1,a+1))
num_lsit = []
for _ in range(b):
    change = list(map(int,input().split()))
    num_lsit.append(change)
    
for change in num_lsit:
    return_list[change[0]-1],return_list[change[1]-1] = return_list[change[1]-1], return_list[change[0]-1]
print(*return_list)