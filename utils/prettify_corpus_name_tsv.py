import pandas as pd

# Read the .tsv file into a DataFrame
df = pd.read_csv('complexity_stats.tsv', sep='\t')

# Replace specific entries in the "File" column
df['File'] = df['File'].replace({
    'enda-dail-comments': 'Dáil Comments',
    'formal-articles': 'Journal.ie Articles',
    'social-comments': 'Journal.ie Comments'
})

# Write the DataFrame back to the .tsv file
df.to_csv('complexity_stats.tsv', sep='\t', index=False)