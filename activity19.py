isExpensive = True

while isExpensive == True:
    x = bool(input("Is it expensive? (True/False): "))
    if x == True:
        print("Consider buying it.")
        continue

    else:
        breakpoint