from File_Reader import *
from knowledge_base import build_knowledge_base, print_knowledge_base

# Read File
filename = 'test.txt' 

print(f'Debug filename: {filename}\n')

tell, ask = read(filename)
print(f'Tell: {tell}')
print(f'Query/Ask: {ask}\n')

# Extract symbol
symbols, sentences = extract_text(tell)
print(f'Symbols: {symbols}')
print(f'Sentence: {sentences}\n')

# In main.py, when you call build_knowledge_base, unpack the returned tuple:
kb, ask = build_knowledge_base(filename)

# Now, when you pass kb to print_knowledge_base, it should be just the dictionary, not a tuple
print_knowledge_base(kb)

