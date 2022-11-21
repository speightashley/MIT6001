home_cost = float(input("How much is your dream home? "))
portion_down_payment = 0.25
current_savings = 0
annual_interest_rate = 0.04
annual_salary = float(input("What is your annual salary? "))
monthly_salary = annual_salary / 12
portion_saved = float(input("What portion of salary will you save each month? (fraction) "))
months = 0

down_payment_required = portion_down_payment * home_cost

while down_payment_required > current_savings:
    current_savings += (monthly_salary * portion_saved) + (current_savings * annual_interest_rate / 12)
    months = months + 1

print(f"Number of months required is {months}")
print(f"You have saved {current_savings}")
print(f"Total required is ", down_payment_required)

