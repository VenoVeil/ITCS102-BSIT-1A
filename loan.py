loan_ant = float(input("Enter the loan amount: "))
year = int(input("Enter years to pay: "))
month = year * 12
principal = loan_ant / month
remaining_bal = loan_ant
for x in  range (1, month + 1):
    remaining_bal -= principal
    loan_interest = remaining_bal * 0.00256
    monthly_payment = principal + loan_interest
    
    print(f"|{x}\t|\t{round(monthly_payment,2)}\t\t|\t {round(loan_interest,2)}\t\t|\t {round(principal,2)}\t\t|\t {round(remaining_bal, 2)}\t\t\t|")                                                                                                                                               
