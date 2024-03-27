import pandas as pd

# Read the TSV file
# df = pd.read_csv(r'C:\Users\luker\Code\corpus_generator\data\Enda-Kenny.D.1975-11-12_limit1000.tsv', sep='\t')

# Read the CSV file
df = pd.read_csv(r'C:\Users\luker\Code\corpus_generator\data\Enda-Kenny-Formal-Corpus.csv')

# Write the 'contribution' column to a TXT file
with open('enda-kenny-formal.txt', 'w', encoding='utf-8') as f:
    for text in df['text']:
        f.write(str(text) + '\n')