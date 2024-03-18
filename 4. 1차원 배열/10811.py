a,b = map(int,input().split())
answer = list(range(1,a+1))
num_list = []
for _ in range(b):
    change = list(map(int,input().split()))
    num_list.append(change)

for change in num_list:
    answer[change[0]-1: change[1]] = reversed(answer[change[0]-1: change[1]])
print(*answer)