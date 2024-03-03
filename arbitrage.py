def calculate_arbitrage(odds1, odds2):
    implied_probability1 = 1 / odds1
    implied_probability2 = 1 / odds2
    total_implied_probability = implied_probability1 + implied_probability2
    print(total_implied_probability)
    if total_implied_probability < 1:
        return "Arbitrage Opportunity Exists The Totall Is Less Than 1"
    else:
        return "No Arbitrage Opportunity The Totall Is Greater Than 1"

if __name__ == "__main__":
    try:
        odds1 = float(input("Enter the first set of odds: "))
        odds2 = float(input("Enter the second set of odds: "))

        result = calculate_arbitrage(odds1, odds2)
        print(result)
    except ValueError:
        print("Invalid input. Please enter valid odds as decimal numbers.")
