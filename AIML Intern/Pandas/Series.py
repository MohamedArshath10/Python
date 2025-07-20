#Pandas Series --->
import pandas as pd
s = pd.Series([100.0,200.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,100.0],
              index=['maths', 'physics', 'chemistry', 'tamil' , 'english', 'comp Sci', 'OS', 'OOPS', 'Cloud comp', 'EMS'])
print("Head Element ----->")
print(s.head())
print("Tail Element ----->")
print(s.tail())
print("Size of the data ------>")
print(s.size)
print("Values ----->")
print(s.values)
