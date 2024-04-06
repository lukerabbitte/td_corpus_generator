import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the data
df = pd.read_csv('complexity_stats.tsv', sep='\t')

# Create the plots directory if it doesn't exist
if not os.path.exists('../plots'):
    os.makedirs('../plots')

# Get the unique metrics
metrics = df['Measure'].unique()

# Colours
files = df['File'].unique()
colors = {file: plt.cm.rainbow(i/len(files)) for i, file in enumerate(files)}

# For each metric
for metric in metrics:
    # Filter the data for the current metric
    df_metric = df[df['Measure'] == metric]

    # print(df_metric)
    # print('\n\n\n')
    
    # Create a bar chart
    plt.figure(figsize=(10, 6))
    
    # For each file in the filtered data
    for file in df_metric['File'].unique():
        df_file = df_metric[df_metric['File'] == file]
        plt.errorbar(df_file['File'], df_file['mean'], yerr=df_file['stdev'], marker='o', linestyle='None', capsize=3, color=colors[file])
    
    # Add labels and title
    plt.xlabel('Metric', fontname='monospace', y=0.9)
    plt.ylabel('Mean', fontname='monospace')
    plt.title(f'Scores for Metric {metric} Across Three Corpora', fontname='monospace', weight='bold')

    # Calculate the maximum y value with some headroom
    y_max = df_metric['mean'].max() + df_metric['stdev'].max()
    headroom = 0.1  # 10% headroom
    y_max += y_max * headroom

    # Check if 'stdev' column exists and does not contain NaN values
    if 'stdev' in df_metric.columns and not df_metric['stdev'].isna().any():
        # Check if mean - stdev is less than 0 for any data point
        lower_bound = df_metric['mean'] - df_metric['stdev']
        print(lower_bound)
        if any(lower_bound < 0):
            plt.ylim(top=y_max)
        else:
            plt.ylim(bottom=0, top=y_max)
    else:
        print("'stdev' column does not exist in the DataFrame or contains NaN values")
    
    # Save the plot
    plt.savefig(f'../plots/{metric}.svg')
    
    # Close the plot
    plt.close()