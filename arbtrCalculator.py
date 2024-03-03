# Function to calculate the stake for each bet
def calculate_stake(odds, total_stake):
    return total_stake / odds

try:
    # Get the number of outcomes from the user
    num_outcomes = int(input("Enter the number of outcomes: "))
    
    # Get the odds for each outcome
    outcomes = []
    for i in range(num_outcomes):
        odds = float(input(f"Enter the odds for Outcome {i + 1}: "))
        outcomes.append(odds)
    
    # Prompt for the total stake
    total_stake = float(input("Enter the total stake amount: "))
    
    # Calculate and display the stakes and profits for each outcome
    stakes = [calculate_stake(odds, total_stake) for odds in outcomes]
   
    
    # Display the results
    for i, (odds, stake) in enumerate(zip(outcomes, stakes)):
        print(f"Outcome {i + 1}:")
        print(f"Odds: {odds}")
        print(f"Stake for Outcome {i + 1}: {stake}")
        
    
except ValueError:
    print("Invalid input. Please enter valid numbers.")
