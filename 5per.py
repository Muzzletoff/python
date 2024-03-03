# Function to calculate 5% of a given number
def calculate_5_percent(number):
    return 0.05 * number

# Get user input for the number
user_input = input("Enter a number: ")

# Convert the user input to a float (assuming input can be a decimal)
try:
    number = float(user_input)
    result = calculate_5_percent(number)
    print(f"5% of {number} is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
