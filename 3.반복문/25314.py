n = int(input())
while True:
    if n < 4:
        if n > 0:
            print("long int")
        else:
            print("int")
        break
    n -= 4
    print("long",end = " ")