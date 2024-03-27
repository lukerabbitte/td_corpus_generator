import os
import numpy as np
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
# from textstat import flesch_kincaid_grade
import string
import pandas as pd

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import math
import string

# LEXICAL

def calculate_ttr(text):
    tokens = word_tokenize(text)
    types = set(tokens)
    return len(types) / len(tokens)

def calculate_lexical_density(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    lexical_tokens = [token for token in tokens if token not in stop_words and token not in string.punctuation]
    return len(lexical_tokens) / len(tokens)

def calculate_avg_token_length(text):
    tokens = word_tokenize(text)
    lengths = [len(token) for token in tokens]
    return sum(lengths) / len(tokens)

def calculate_vocab_richness(text):
    tokens = word_tokenize(text)
    types = set(tokens)
    return len(types) / len(tokens)

def calculate_entropy(text):
    tokens = word_tokenize(text)
    freq_dist = FreqDist(tokens)
    probs = [freq_dist.freq(l) for l in freq_dist]
    return -sum(p * math.log2(p) for p in probs)

# STRUCTURAL

def calculate_sentence_length_in_chars(text):
    sentences = sent_tokenize(text)
    return np.mean([len(sentence) for sentence in sentences])

def calculate_sentence_length_in_tokens(text):
    sentences = sent_tokenize(text)
    return np.mean([len(word_tokenize(sentence)) for sentence in sentences])

def calculate_punctuation_per_token(text):
    tokens = word_tokenize(text)
    punctuations = sum([1 for token in tokens if token in string.punctuation])
    return punctuations / len(tokens)

def calculate_avg_dependency_distance(text):
    # This requires a dependency parser, which is not included in NLTK.
    # You might need to use a library like spaCy for this.
    pass

def calculate_constituents_per_sentence(text):
    # This requires a parser that can generate constituency parse trees.
    # You might need to use a library like NLTK's CoreNLP interface for this.
    pass

def calculate_height_of_parse_trees(text):
    # This also requires a parser that can generate constituency parse trees.
    pass

def calculate_non_terminal_constituents_per_sentence(text):
    # This also requires a parser that can generate constituency parse trees.
    pass

def calculate_flesch_kincaid_grade(text):
    # return flesch_kincaid_grade(text)
    pass

# Update the process_file function to include the new metrics
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return {
        'file': file_path,
        'ttr': calculate_ttr(text),
        'lexical_density': calculate_lexical_density(text),
        'avg_token_length': calculate_avg_token_length(text),
        'vocab_richness': calculate_vocab_richness(text),
        'entropy': calculate_entropy(text),
        'sentence_length_in_chars': calculate_sentence_length_in_chars(text),
        'sentence_length_in_tokens': calculate_sentence_length_in_tokens(text),
        'punctuation_per_token': calculate_punctuation_per_token(text),
        'flesch_kincaid_grade': calculate_flesch_kincaid_grade(text),
        # Add the other metrics here once you have implemented them
    }

directory = 'corpora'
file_names = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.txt')]
results = [process_file(file_name) for file_name in file_names]

print(results)

df = pd.DataFrame(results)
print(df.describe())

os.makedirs('plots', exist_ok=True)

# Create a separate plot for each column
for column in df.columns:
    if column != 'file':
        df.set_index('file')[column].plot(kind='bar')
        plt.title(column)
        plt.savefig(f'plots/{column}.png')
        plt.close()