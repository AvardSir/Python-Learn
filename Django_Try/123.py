import pandas as pd

#create DataFrame
df = pd.DataFrame({'A': [25, 12, 15, 14, 19, 23, 25, 29],
 'B': [5, 7, 7, 9, 12, 9, 9, 4],
 'C': [11, 8, 10, 6, 6, 5, 9, 12]})
df.drop('B', axis= 1 , inplace= True )
print(df)