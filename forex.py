import pandas as pd
import numpy as np
import talib

# Load your real historical price data from a CSV file
# Replace 'eurusd.csv' with the actual path to your CSV file
df = pd.read_csv('eurusd.csv')

# Convert the 'Date' column to a datetime format and set it as the index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Calculate the 10-period and 15-period moving averages
df['MA10'] = df['Close'].rolling(window=10).mean()
df['MA15'] = df['Close'].rolling(window=15).mean()

# Calculate the stochastic oscillator
df['%K'], df['%D'] = talib.STOCH(df['High'], df['Low'], df['Close'])

# Check for crossovers
crossover_signals = []

# Initialize the 'Crossover Signal' list with a default value (e.g., "No Signal")
crossover_signals.append("No Signal")

for i in range(1, len(df)):
    ma_crossover = 0
    stoch_crossover = 0

    # Moving Average Crossovers
    if df['MA10'][i - 1] < df['MA15'][i - 1] and df['MA10'][i] > df['MA15'][i]:
        ma_crossover = 1
    elif df['MA10'][i - 1] > df['MA15'][i - 1] and df['MA10'][i] < df['MA15'][i]:
        ma_crossover = -1

    # Stochastic Oscillator Crossovers
    if df['%K'][i - 1] < df['%D'][i - 1] and df['%K'][i] > df['%D'][i]:
        stoch_crossover = 1
    elif df['%K'][i - 1] > df['%D'][i - 1] and df['%K'][i] < df['%D'][i]:
        stoch_crossover = -1

    # Combine signals
    if ma_crossover == 1 and stoch_crossover == 1:
        crossover_signals.append("Buy Signal")
    elif ma_crossover == -1 and stoch_crossover == -1:
        crossover_signals.append("Sell Signal")
    else:
        crossover_signals.append("No Signal")

# Assign the 'Crossover Signal' list to the DataFrame
df['Crossover Signal'] = crossover_signals

print(df)
