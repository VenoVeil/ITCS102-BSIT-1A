for x in range(7, 0, -1):
    for y in range(1, x + 1):
        print("*", end=" ")
    print()

print()   # blank line between the two patterns

for x in range(1, 8):
    for y in range(1, x + 1):
        print(x, end=" ")
    print()