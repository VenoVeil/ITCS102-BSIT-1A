#age (integer)
#is_employed (boolean)
#credit_score (float)
#annual_income (float)
#is_collateral (boolean)

age = int(input("Enter your age: "))
is_employed = input("Are you employed? (yes/no): ").strip().lower() == "yes"
credit_score = float(input("Enter your credit score ---> "))
annual_income = float(input("Enter your annual income: "))
is_collateral = input("Do you have collateral? (yes/no): ").strip().lower() == "yes"
interest = input("")

base_rate = 0.0

 #Eligibility criteria:
if age >= 18 and is_employed and credit_score >= 750 and annual_income >= 30000 and is_collateral:
    print("You are eligible for the loan")

    
else:
    print("You are not eligible for the loan.")
    if age < 18:
        print("Reason: You must be at least 18 years old.")
    if not is_employed:
        print("Reason: You must be employed.")
    if credit_score < 750:
        print("Reason: Your credit score must be at least 750.")
    if annual_income < 30000:
       base_rate = 4.5
       print("Your base rate is", base_rate)
    else:
       base_rate = 5.0
       print("Your base rate is ", base_rate)
       elif:credit_score >= 600 and credit_score
       print("Reason: Your annual income must be at least P30,000.")
    if not is_collateral:
        print("Reason: You must have collateral.")
