import random

def random_yes_or_no():
    choices = ["yes", "no"]
    return random.choice(choices)

if __name__ == "__main__":
    try:
        while True:
            answer = random_yes_or_no()
            user_input = input("Press Enter for the next answer, or any other key to exit: ")
            print(answer)
            if user_input and user_input.lower() != 'n':
                break
    except KeyboardInterrupt:
        print("\nExiting the randomization.")
