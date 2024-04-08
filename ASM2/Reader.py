import re

def read(filename):
    with open(filename) as f:
        lines = [word for line in f for word in line.strip().lower().split(";")]

    try:
        query_index = lines.index('ask')
        tell = lines[:query_index]
        query = lines[query_index + 1] if query_index + 1 < len(lines) else ''
    except ValueError:  
        tell = lines
        query = ''

    tell = [x.replace(" ", "") for x in tell if x and x not in ["tell", "ask"]]

    return tell, query

def extract_symbols_and_sentences(tell):
    symbols = {match for sentence in tell for match in re.findall(r'\b[a-zA-Z][a-zA-Z0-9]*\b', sentence)}
    sentences = list(tell)  
    return symbols, sentences
