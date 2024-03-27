

# type-token ratio
def type_token_ratio(text_file):
    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Tokenize the text by splitting on whitespace
    tokens = text.split()

    # Calculate the number of unique tokens (types)
    types = set(tokens)

    # Calculate the Type-Token Ratio (TTR)
    ttr = len(types) / len(tokens)

    return ttr

# Use the function
ttr = type_token_ratio('text/enda-kenny-large.txt')
print(f'Type-Token Ratio: {ttr}')