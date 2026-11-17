route = ["Terminal", "Perez Park", "Pacific Mall", "Arias"]
passengers = []
SEATS = 6
FARE = 13
total = 0
while True:
    print()
    print("Sakay", "passengers")
    print(len(passengers), "of", SEATS, "seats")
    print("1 Sakay 2 Priority seat 3 Paea po!")
    print("4 Baba sa pinto 5 Baba sa harap")
    print("6 Seat check 7 Balikan 8 Exit")
    choice = input("Choice: ")

    if choice == "1":
        if len(passengers) == SEATS:
            print("Puno na!")
        else:
            name = input("Name: ")
            passengers.append(name)
            total = total + FARE
            print(name, "boarded at the back. ")

    elif choice == "2":
        if len(passengers) == SEATS:
            print("Puno  na!")
        else:
            name = input("Name: ")
            passengers.insert(0, name)
            total = total + FARE
            print(name, "took priority seat")

    elif choice == "3":
        name = input("Who is getting off? ")
        if name in passengers:
            passengers.remove(name)
            print(name, "Got off. ingat!")
        else:
            print(name, "its not this jeep" )

    elif choice == "4":
        if len(passengers) == 0:
            print("The jeep is empty. ")
        else:
            left = passengers.pop()
            print(left, "got off atb the door. ")

    elif choice == "5":
        if len(passengers) == 0:
            print("The jeep is empty. ")
        else:
            front = passengers.pop(0)
            print(front, "Got off at the front. ")


    elif choice == "6":
        for i in range(len(passengers)):
            print("Seat", i + 1, passengers[i])

    elif choice == "7":
        route.reverse()
        print("Route:", route)
