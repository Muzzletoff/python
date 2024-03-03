import random

def roll_dice():
    die1 = random.randint(1, 6)  # Simulate the roll of the first die (1-6)
    die2 = random.randint(1, 6)  # Simulate the roll of the second die (1-6)
    return die1, die2

if __name__ == "__main__":
    while True:
        input("Press Enter to roll the dice...")
        die1, die2 = roll_dice()
        print(f"Die 1: {die1}")
        print(f"Die 2: {die2}")
        print(f"Total: {die1 + die2}")
        play_again = input("Roll again? (y/n): ").lower()
        if play_again != "y":
            break
