mainus = []
for _ in range(10):
    num = int(input())
    if not num%42 in mainus:
        mainus.append(num%42)
print(len(mainus))