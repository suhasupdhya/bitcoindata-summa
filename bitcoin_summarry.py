import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'bitcoin.csv'  # Replace with your actual CSV file path
df = pd.read_csv(file_path)

# Convert 'Date' column to datetime if it exists
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])

# 1. Dataset Info
print("🔹 Dataset Information:")
print(df.info())
print("\n")

# 2. First 5 rows
print("🔹 First 5 Rows:")
print(df.head())
print("\n")

# 3. Summary statistics
print("🔹 Summary Statistics:")
print(df.describe())
print("\n")

# 4. Missing value check
print("🔹 Missing Values:")
print(df.isnull().sum())
print("\n")

# 5. Date range (if applicable)
if 'Date' in df.columns:
    print(f"🔹 Date Range: {df['Date'].min().date()} to {df['Date'].max().date()}")
    print("\n")

# 6. Optional: Plot Closing Price over Time
if 'Close' in df.columns and 'Date' in df.columns:
    plt.figure(figsize=(12, 5))
    plt.plot(df['Date'], df['Close'], label='Closing Price', color='blue')
    plt.title('Bitcoin Closing Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
