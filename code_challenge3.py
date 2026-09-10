#Write a program that calculates total shipping charges using package details locations,ruled and strict conditional order.


name = input("Enter name of pqckage sender: ")
item = input("Type of item: ")
is_fragile = input("Is the item fragile? (yes/no): ").lower().startswith("y")
weight = float(input("Enter weight in kg: "))
distance = float(input("Enter distance in km: "))
is_express = input("Is this express shipping? (yes/no): ").lower().startswith("y")
is_international = input("Is this an international shipment? (yes/no): ").lower().startswith("y")


base_cost = (weight * 2.50) + (distance * 0.15)

if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
    total = 0.00
elif is_international and is_express:
    total = (base_cost * 1.40) + 50
elif is_express or (is_international and weight > 20):
    total = (base_cost * 1.20) + 25
elif weight > 30 or distance > 1000:
    total = base_cost + 30
else:
    total = base_cost

print(f"\nSender: {name}")
print(f"Item: {item}")
print(f"Fragile: {is_fragile}")
print(f"Total shipping cost: P{total:.2f}")