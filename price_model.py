import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('Nat_Gas.csv')

# Convert Dates (fix warning)
df['Dates'] = pd.to_datetime(df['Dates'], format='%m/%d/%y')

# Sort data
df = df.sort_values(by='Dates')

# Plot (optional)
plt.figure(figsize=(10, 5))
plt.plot(df['Dates'], df['Prices'])
plt.xlabel('Dates')
plt.ylabel('Prices')
plt.title('Natural Gas Prices Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Set index
df = df.set_index('Dates')

# Convert to daily + interpolate
df = df.asfreq('D')
df['Prices'] = df['Prices'].interpolate(method='linear')

# Predict future prices (repeat last year's pattern)
last_year = df['Prices'][-365:]

future_dates = pd.date_range(
    start=df.index[-1] + pd.Timedelta(days=1),
    periods=365
)

future_df = pd.DataFrame({
    'Prices': last_year.values
}, index=future_dates)

# Combine past + future
df = pd.concat([df, future_df])

# Function to get price
def get_price(date):
    date = pd.to_datetime(date)
    
    if date in df.index:
        return float(df.loc[date, 'Prices'])
    else:
        return "Date out of range"

# Example usage
#print("Past:", get_price('2023-01-01'))
#print("Future:", get_price('2025-01-01'))