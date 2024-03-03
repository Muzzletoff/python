import random
import time

# Set a seed to initialize the PRNG
seed = int(time.time())
random.seed(seed)

# Generate the first decimal number in the sequence
first_number = random.uniform(1.0, 10000.0)

# Predict the next decimal number using the same seed
next_number = random.uniform(1.0, 10000.0)

print(f"The first decimal number in the sequence is: {first_number:.2f}")
print(f"The predicted next decimal number is: {next_number:.2f}")
