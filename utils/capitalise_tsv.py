import pandas as pd

# Read the .tsv file into a DataFrame
df = pd.read_csv('complexity_stats.tsv', sep='\t')

# Capitalize all entries in the "Measure" column
df['Measure'] = df['Measure'].str.title()

# Write the DataFrame back to the .tsv file
df.to_csv('complexity_stats.tsv', sep='\t', index=False)