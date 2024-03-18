num_list = []

for _ in range(9):
    num_list.append(int(input()))
big = max(num_list)
idx = int(num_list.index(big))
print(big,idx+1,sep="\n")