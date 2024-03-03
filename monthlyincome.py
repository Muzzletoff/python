def calculate_accumulated_income(daily_salary, working_days_in_month):
    accumulated_income = daily_salary * working_days_in_month
    return accumulated_income

def calculate_yearly_income(accumulated_income, no_months):
    yearly_income = accumulated_income * no_months
    return yearly_income

# Define your daily salary and working days in a month
daily_salary = float(input("Enter the daily salary: "))  # Replace with your daily salary
working_days_in_month = int(input("Enter the number of working days in the month: "))  # Replace with the number of working days in the month
no_months = 12  # Number of months in a year

# Calculate and display the accumulated monthly income and yearly income
accumulated_income = calculate_accumulated_income(daily_salary, working_days_in_month)
yearly_income = calculate_yearly_income(accumulated_income, no_months)

print(f"Daily Salary: ${daily_salary:.2f}")
print(f"Working Days in the Month: {working_days_in_month}")
print("Daily Incomes:")
for day in range(1, working_days_in_month + 1):
    daily_income = daily_salary * day  # Calculate daily income for the current day
    print(f"Day {day}: ${daily_income:.2f}")

print(f"Monthly Income: ${accumulated_income:.2f}")
print(f"Yearly Income: ${yearly_income:.2f}")

