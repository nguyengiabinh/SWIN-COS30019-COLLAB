from Reader import *

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

