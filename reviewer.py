# Inputs
#owner_age (integer)
#monthly_revenue (float)
#credit_score (integer)
#years_in_business (float)
#has_defaults (boolean)
#collateral_name (string)
#collateral_value (float)

age = int(input)("AGE =-->")
rev = float(input("REVENUE--->"))
credit_score = int(input("CREDIT SCORE--->"))
yrs = float(input("YEARS OF BISNESS--->"))
has_defaults = bool(input("FILE FOR BANKRUPTCY--->"))
collateral = input("COLLATERAL NAME--->")
c_value = float(input("COLLATERAL VALUE--->"))

max_loan = 0
base_fee = 0

if age >= 21 and has_defaults == False and yrs >= 2.0:
    print("BASELINE PASASED")
    if credit_score >= 720:
        print("CREDIT SCORE CONSIDERED HIGH")
        max_loan = rev * 3
        if rev >= 50000:
            print("ABOVE 50K REVENUE")
            base_fee + max_loan * 0.015
            print("BASE FEE IS SET TO", base_fee)
    else:
           print("REVENUE BELOW 50K")
    base_fee = max_loan * 0.025
    print("BASE FEE IS SET TO ", base_fee)
else:
    print("CREDIT SCORE TOO LOW")
    print("BASELINE FAILED")



