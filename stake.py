# Ask for the initial stake as input
initialstake = float(input("Enter your initial stake (in dollars): $"))

# Check if the input is valid (positive)
if initialstake <= 0:
    print("Please enter a positive initial stake.")
else:
    print(f"Your initial stake is: ${initialstake}")

    # Calculate profit threshold
    lossthreshold = initialstake * 3.992063492

    # Calculate loss threshold
    profitthreshold = lossthreshold * 2
    print(f"Loss Threshold: ${lossthreshold:.2f}")

    print(f"Profit Threshold: ${profitthreshold:.2f}")


    # You can continue your program logic here
