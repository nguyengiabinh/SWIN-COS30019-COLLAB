
# from File_Reader import *
# from interpreter import build_knowledge_base, print_knowledge_base

# # Read File
# filename = 'test2.txt' 

# print(f'Debug filename: {filename}\n')

# tell, ask = read(filename)
# print(f'Tell: {tell}')
# print(f'Query/Ask: {ask}\n')

# # Extract symbol
# symbols, sentences = extract_text(tell)
# print(f'Symbols: {symbols}')
# print(f'Sentence: {sentences}\n')

# kb = build_knowledge_base(filename)
# print_knowledge_base(kb)


from File_Reader import read
from interpreter import build_knowledge_base, print_knowledge_base
from BC import backward_chaining
from FC import forward_chaining
from TT import generate_truth_table

# Read from file and build the knowledge base
filename = 'test2.txt'
kb = build_knowledge_base(filename)
print("Knowledge Base:")

from File_Reader import *
from knowledge_base import build_knowledge_base, print_knowledge_base

# Read File
filename = 'test3.txt' 

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

# BC and FC demonstration
query = 'd'  # Example query
bc_result, bc_counts = backward_chaining(kb, query)
print(f"\nBackward Chaining result for query '{query}': {'YES' if bc_result else 'NO'}, proven {bc_counts['yes']} times, not proven {bc_counts['no']} times")
fc_result, fc_counts = forward_chaining(kb, query)
print(f"Forward Chaining result for query '{query}': {'YES' if fc_result else 'NO'}, proven {fc_counts['yes']} times, not proven {fc_counts['no']} times")

# Truth table demonstration
print("\nTruth Table Demonstration:")
generate_truth_table(['A and B'])
