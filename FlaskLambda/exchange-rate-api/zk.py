
import pandas as pd

file_path = 'KDDTrain.csv'
rows_per_file = 25000


# Read in the large CSV file using pandas
df = pd.read_csv('KDDTrain.csv', on_bad_lines='skip')

# Split the data into smaller dataframes based on the number of rows
df_list = [df.loc[i:i+rows_per_file-1, :] for i in range(0, len(df), rows_per_file)]

# Save each smaller dataframe to a separate CSV file
for i, df in enumerate(df_list):
    df.to_csv(f'smaller_file_{i+1}.csv', index=False)