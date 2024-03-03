import random

def flip_coin():
    # Simulate a fair coin flip, 0 for heads, 1 for tails
    return random.randint(0, 1)

def main():
    print("Welcome to the Coin Flip Game!")
    balance = 100  # Starting balance, you can change this

    while balance > 0:
        print(f"Your current balance: ${balance}")
        bet = input("Place your bet (enter 'quit' to exit): $")

        if bet.lower() == 'quit':
            break

        try:
            bet = float(bet)
        except ValueError:
            print("Invalid input. Please enter a valid bet.")
            continue

        if bet <= 0 or bet > balance:
            print("Invalid bet amount. Please enter a bet within your balance.")
            continue

        outcome = flip_coin()
        if outcome == 0:
            print("Heads! You win!")
            balance += bet
        else:
            print("Tails! You lose.")
            balance -= bet

    print("Game over. Your final balance:", balance)

if __name__ == "__main__":
    main()
