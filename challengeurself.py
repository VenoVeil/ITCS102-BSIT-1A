size = int(input("input size of x "))
for x in range(size):
    for y in range (size):
                if x==0 or x==size-1 or y==0 or y==size-1:
                 print(" * ", end=" ")
    else:
            print("   ", end=" ")
    print()
