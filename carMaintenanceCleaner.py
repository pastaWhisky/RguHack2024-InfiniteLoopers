# regex to clean the data
import pandas as pd

df = pd.read_csv('Datasets/Car Maintenance Costs.csv')
print(df)
unique_entries = df['Make'].numunique()



# 