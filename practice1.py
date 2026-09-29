# Company Scoring Program

company_name = input("Enter your company name: ")
industry = input("Enter your industry: ")

is_profitable = (
    input("Do you have profit? (yes/no): ")
    .strip()
    .lower()
    == "yes"
)

annual_revenue = float(
    input("What is your annual revenue in $? ")
)

growth_rate = float(
    input("What is your yearly growth rate in %? ")
)

years_operating = float(
    input("How many years has your company been operating? ")
)

is_high_risk_sector = (
    input("Is it a high-risk sector? (yes/no): ")
    .strip()
    .lower()
    == "yes"
)

has_patent = (
    input("Do you have a patent? (yes/no): ")
    .strip()
    .lower()
    == "yes"
)

# Calculate the base score
base_score = annual_revenue * 0.0002 + (growth_rate * 3.0)

# Calculate the final score
if years_operating < 1 or (not is_profitable and growth_rate < 5):
    score = 0

elif is_high_risk_sector and has_patent:
    score = (base_score * 1.5) + 20

elif growth_rate > 50 or (has_patent and annual_revenue > 1_000_000):
    score = (base_score * 1.3) + 15

elif is_high_risk_sector or years_operating < 3:
    score = base_score - 10

else:
    score = base_score

# Display the results
print("\n--- Company Report ---")
print("Company Name:", company_name)
print("Industry:", industry)
print("Base Score:", round(base_score, 2))
print("Final Score:", round(score, 2))
