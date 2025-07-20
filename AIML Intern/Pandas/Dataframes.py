import pandas as pd
data = {'name': ['A', 'B', 'C', 'D'],
        'age': [20, 21, 22, 23],
        'city': ['chennai', 'salem', 'madhurai', 'delhi']
        }
df = pd.DataFrame(data)
# Adding data
df['salary'] = [20000, 2000, 1000, 3000]
print(df)
# Accessing data
print("Accessing data ----->")
print(df.loc[3])
# Filtering the datas
print("Filtering ---->")
print(df[df['age'] > 21])
