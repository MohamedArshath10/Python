import pandas as pd
data = {
    'Name' : ['A', 'B', 'C', 'A'],
    'Age' : [20, 21, 22, 20],
    'City' : ['salem', 'madurai', 'chennai', 'salem']
}

df = pd.DataFrame(data)
# To identify duplicate
print(df.duplicated())
# TO count the duplicated
print(df.duplicated().sum())
# To drop duplicates
print('Drop row duplicates')
duplica = df.drop_duplicates()
print(duplica)
# For specific column duplicates
print('Specific column  duplicates')
duplica = df.duplicated(subset=['Name'])
print(duplica)
# For droping column duplicates
print('Drop column  duplicates')
duplicat = df.drop_duplicates(keep=False)
print(duplicat)