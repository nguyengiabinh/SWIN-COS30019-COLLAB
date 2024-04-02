from File_Reader import *
from interpreter import build_knowledge_base, print_knowledge_base

# Read File
filename = 'test2.txt' 

print(f'Debug filename: {filename}\n')

tell, ask = read(filename)
print(f'Tell: {tell}')
print(f'Query/Ask: {ask}\n')

# Extract symbol
symbols, sentences = extract_text(tell)
print(f'Symbols: {symbols}')
print(f'Sentence: {sentences}\n')

kb = build_knowledge_base(filename)
print_knowledge_base(kb)

