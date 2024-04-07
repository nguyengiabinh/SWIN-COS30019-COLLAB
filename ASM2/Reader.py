# import re

# '''Read from file'''
# def read(filename):
#     with open(filename) as f:
#         lines = [line.strip().lower().split(";") for line in f]
#     flattened_lines = [item for sublist in lines for item in sublist]
    
#     try:
#         query_index = flattened_lines.index('ask')
#     except ValueError:
#         query_index = len(flattened_lines)

#     tell = [x.replace(" ", "") for x in flattened_lines[:query_index] if x not in ["", "tell", "ask"]]
#     query = flattened_lines[query_index + 1].replace(" ", "") if query_index + 1 < len(flattened_lines) else ''

#     return tell, query  
    
# '''Extract Symbol'''
# def extract_symbols_and_sentences(tell):
#     symbols = set()
#     sentences = []
#     for sentence in tell:
#         symbols.update(re.findall(r'\b[a-zA-Z][a-zA-Z0-9]*\b', sentence))
#         sentences.append(sentence)
#     return symbols, sentences



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
