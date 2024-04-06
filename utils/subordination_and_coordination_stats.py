import statistics
from conllu import parse

# Open and read the CoNLL-U file
with open(r'C:\Users\luker\Code\corpus_generator\corpora\social-comments.txt.conllu', 'r', encoding='utf-8') as file:
    data = file.read()

# Parse the CoNLL-U data
sentences = parse(data)

# Initialize a dictionary for verb counts per sentence
verb_counts = {}
sconj_counts = {}
cconj_counts = {}

# Iterate over each sentence
for sentence in sentences:
    # Get the sentence id
    sentence_id = sentence.metadata['sent_id']

    # Initialize a counter for verbs
    verb_count = 0
    sconj_count = 0
    cconj_count = 0

    # Iterate over each token in the sentence
    for token in sentence:
        # If the token is a verb, increment the verb counter
        if token['upostag'] == 'VERB':
            verb_count += 1
        # If the token is a subordinating conjunction, increment the subordinating conjunction counter
        if token['upostag'] == 'SCONJ':
            sconj_count += 1
        # If the token is a coordinating conjunction, increment the coordinating conjunction counter
        if token['upostag'] == 'CCONJ':
            cconj_count += 1

    # Add the counts to the dictionaries
    verb_counts[sentence_id] = verb_count
    sconj_counts[sentence_id] = sconj_count
    cconj_counts[sentence_id] = cconj_count

# Calculate the average, standard deviation and variance for each count
average_verb_count = statistics.mean(verb_counts.values())
std_dev_verb_count = statistics.stdev(verb_counts.values())
variance_verb_count = statistics.variance(verb_counts.values())

average_sconj_count = statistics.mean(sconj_counts.values())
std_dev_sconj_count = statistics.stdev(sconj_counts.values())
variance_sconj_count = statistics.variance(sconj_counts.values())

average_cconj_count = statistics.mean(cconj_counts.values())
std_dev_cconj_count = statistics.stdev(cconj_counts.values())
variance_cconj_count = statistics.variance(cconj_counts.values())

# Print the average counts, standard deviation and variance
print(f'Average count of verbs per sentence: {average_verb_count}, Standard Deviation: {std_dev_verb_count}, Variance: {variance_verb_count}')
print(f'Average count of subordinating conjunctions per sentence: {average_sconj_count}, Standard Deviation: {std_dev_sconj_count}, Variance: {variance_sconj_count}')
print(f'Average count of coordinating conjunctions per sentence: {average_cconj_count}, Standard Deviation: {std_dev_cconj_count}, Variance: {variance_cconj_count}')