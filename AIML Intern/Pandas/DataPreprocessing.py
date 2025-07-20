# Using isnull() and notnull() to check null values in cells
import  pandas as  pd

data = {
    'Name' : ['A', 'B', 'C', 'D'],
    'Age' : [20, 21, 22, None],
    'City' : ['salem', 'madurai', None, 'chennai'],
    'Marks' : [None, None, None, None]
}
df = pd.DataFrame(data)
# Using notnull()
print('Using notnull()')
print(df.notnull())
# Using isnull()
print('Using isnull()')
print(df.isnull())
# Count of the null values
print('Using .sum()')
print(df.isnull().sum())
# Using drop
print('Row Drop()')
dropped = df.dropna()
print(dropped)
# Using drop for coloumn
print('Coloumn drop')
data_dropped = df.dropna(axis=1, how='all')
print(data_dropped)
# Fill the None with constant value
print('Using fill')
filled = df.fillna('Missing')
print(filled)
# Using forward fill
print('Using forward fill')
f_filled = df.fillna(method='ffill')
print(f_filled)
# Mean
print('Using mean')
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)
print(df)