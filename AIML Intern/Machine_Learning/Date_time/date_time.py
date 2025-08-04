import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Display plots inline 
# %matplotlib inline
# Generate a daily date range
date_range = pd.date_range(start='2023-01-01', end='2023-06-30', freq='D')

# Generate synthetic data with trend and seasonality
np.random.seed(0)
trend = np.linspace(10, 50, len(date_range))
seasonality = 10 * np.sin(2 * np.pi * date_range.dayofyear / 30)  # Monthly seasonality
noise = np.random.normal(scale=2, size=len(date_range))
values = trend + seasonality + noise

# Create DataFrame
df = pd.DataFrame({'Date': date_range, 'Value': values})
df.set_index('Date', inplace=True)
df.head()
df.plot(figsize=(12, 5), title="Original Time Series Data")
plt.xlabel("Date")
plt.ylabel("Value")
plt.grid(True)
plt.show()
df['Rolling_Mean'] = df['Value'].rolling(window=15).mean()

df[['Value', 'Rolling_Mean']].plot(figsize=(12, 5), title="Trend Detection using Rolling Mean")
plt.xlabel("Date")
plt.ylabel("Value")
plt.grid(True)
plt.show()
# Decompose using additive model (monthly seasonality → period=30)
decomposition = seasonal_decompose(df['Value'], model='additive', period=30)

# Plot decomposition
decomposition.plot()
plt.tight_layout()
plt.show()
df['Year'] = df.index.year
df['Month'] = df.index.month
df['Day'] = df.index.day
df['Weekday'] = df.index.day_name()
df[['Value', 'Month', 'Weekday']].head()
weekly_avg = df['Value'].resample('W').mean()

weekly_avg.plot(figsize=(12, 4), title='Weekly Average of Values')
plt.xlabel("Week")
plt.ylabel("Average Value")
plt.grid(True)
plt.show()