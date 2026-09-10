Input("")


midterm = float(input("Enter Midterm grade: "))
semifinal = float(input("Enter Semi-Final grade: "))
final = float(input("Enter Final grade: "))
quiz = float(input("Enter Quiz grade: "))
pt = float(input("Enter Project grade: "))

# Computing Final Grade

finalgrade = (midterm * 0.15) + (semifinal * 0.15) + (final * 0.15) + (quiz * 0.25) + (pt * 0.15)

print("\nFinal Grade:", round(finalgrade, 2))

if finalgrade >= 75:
    print("Congratulations! You passed the course.")
else:
    print("Sorry, you failed.")