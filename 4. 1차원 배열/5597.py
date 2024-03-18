num_list = []
for _ in range(28):
    num_list.append(int(input()))

for you in range(1,31):
    if not you in num_list:
        print(you)