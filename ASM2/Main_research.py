from Reader import *
from Classification import *
import os

# Get the file path from the user
while True:
    filename = input("Enter the file path: ")

    if os.path.exists(filename):
        break
    else:
        print(f"Testing file '{filename}' does not exist. Please enter a valid testing file.")

print(f'Chosen filename: {filename}\n')

tell, ask = read(filename)
print(f'Tell: {tell}')
print(f'Query/Ask: {ask}\n')

# Extract symbol
symbols, sentences = extract_symbols_and_sentences(tell)
print(f'Symbols: {symbols}')
print(f'Sentence: {sentences}\n')

kb, ask = build_knowledge_base(filename)
print_knowledge_base(kb)
input("Press Enter to exit...")

