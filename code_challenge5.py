n = int(input("input size of x "))
for x in range(n):
    for y in range (n):
        if x + y == n - 1 or x==y:
            print("*",end=" ")
        else:
            print("",end=" ")
    print()
print( )

z = 1
for x in range(5):
    for y in range(5):
           print(y,end=" ")
           z = z + 1
    print()