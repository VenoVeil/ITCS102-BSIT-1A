account_holder = input("Account holder: ")
customer_age = int(input("Age: "))
cubic_meters = float(input("Cubic meters used: "))
is_student_housing = input("Student housing? (yes/no): ").lower() == "yes"
is_industrial = input("Industrial? (yes/no): ").lower() == "yes"
is_peak_season = input("Peak season? (yes/no): ").lower() == "yes"

if is_industrial and cubic_meters <= 100:
    rate = 25.00
elif is_industrial and cubic_meters > 100:
    rate = 38.00
elif cubic_meters <= 20:
    rate = 12.00
elif 21 <= cubic_meters <= 50:
    rate = 18.00
else:
    rate = 28.00

base_cost = cubic_meters * rate

if customer_age >= 60 or is_student_housing:
    base_cost *= 0.88

print(f"Total cost: {base_cost:.2f}")