import pandas as pd
import os

## Create a simple dataframe with columns names

data = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' : [25,30,35],
    'City' : ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)


##Adding a new row of the detais to the dataframe
new_row_loc = {'Name':'GF1', 'Age': 20, 'City': 'London'}
df.loc[len(df.index)] = new_row_loc


## Ensure the data directory exists at the root level

data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)


## Defien the ffile path
file_path = os.path.join(data_dir, 'sample_data.csv')

## Save the Dataframe to a CSV files, including columns name
df.to_csv(file_path, index = False)
print(f"CSV file saved to {file_path}")
