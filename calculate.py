try:
    starting_price = float(input("Enter the starting price: "))
    multiplier = float(input("Enter the multiplier: "))
    rng = int(input("Enter the range: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Initialize the result with the starting price
result = starting_price
print(f"Starting price is  : {starting_price}")

# Initialize a list to store the differences
differences = []

# Perform the multiplication rng times and print the result at each step
for i in range(rng):
    previous_result = result
    result *= multiplier
    difference = result - previous_result
    differences.append(difference)
    print(f"Result after step {i + 1}: {result}")
# Display the differences
print("Differences between each step:")
for i, diff in enumerate(differences):
    print(f"Step {i + 0} to Step {i + 1}: {diff}")
# Display the final result
print(f"Starting price after multiplying by {multiplier} {rng} times is: {result}")
