a,b = map(int,input().split())
return_list = [0 for _ in range(a)]
num_lsit = []
for _ in range(b):
    change = list(map(int,input().split()))
    num_lsit.append(change)

    
for change in num_lsit:
    return_list[change[0]-1:change[1]] = [change[2] for _ in range(change[1]-change[0]+1)]
print(*return_list)