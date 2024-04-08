import os
from Reader import *
from Parser import *
from logic import *
from truthtable import *
from BC import *
from FC import *

def main(method, filename):
    # Read File
    tell, ask = read(filename)

    # Extract symbol
    symbols, sentences = extract_symbols_and_sentences(tell)

    # Create a dictionary to hold Symbol instances
    symbol_objects = {}

    # Create a Symbol instance for each unique symbol and store it in the dictionary
    for symbol in symbols:
        symbol_objects[symbol] = Symbol(symbol)

    knowledge_base = construct_knowledge_base(sentences) # Transform sentence into logical sentence
    query_sentence = parse(ask)


    # Output the results
    print('\nResults:')
    if method == "TT":
        # Create a TruthTable instance
        truth_table = TruthTable(symbols, knowledge_base, query_sentence)
        entailed_symbols = truth_table.get_entailed_symbols()
        print(truth_table)
        print(entailed_symbols)
        # Model Check
        is_Valid = model_check(knowledge_base, query_sentence)
        print(is_Valid)
    elif method == "FC":
        # Forward Chaining
        fc = ForwardChaining(knowledge_base, ask)
        fc_result = fc.solve()
        print(fc_result)
        is_Valid = model_check(knowledge_base, query_sentence)
        print(is_Valid)
    elif method == "BC":
        # Backward Chaining
        bc = BackwardChaining(knowledge_base, ask)
        bc_result = bc.solve()
        print(bc_result)
        is_Valid = model_check(knowledge_base, query_sentence)
        print(is_Valid)

if __name__ == "__main__":
    # Define available search algorithms
    method_choice = ['TT', 'FC', 'BC']

while True:
    # Get the filename and method from the user on one line
    user_input = input("Enter the file path and method: ").split()

    # Check if the user entered both the filename and the method
    if len(user_input) != 2:
        print("Please enter both the file path and the method, separated by a space.")
        continue  # This skips the rest of the loop and asks for input again

    filename, method = user_input

    # Check if the file exists
    if not os.path.exists(filename):
        print(f"The file '{filename}' does not exist. Please enter a valid file path.")
        continue  # This skips the rest of the loop and asks for input again

    # Check if the method is valid
    if method not in method_choice:
        print("Invalid method. Please enter a valid method (BC, FC, TT).")
        continue  # This skips the rest of the loop and asks for input again

    # If both the file exists and the method is valid, print confirmation and break out of the loop
    print(f"File: {filename}, Chosen method: {method}")
    break  # Exit the loop since both conditions are met
main(method, filename)
input("Press Enter to exit...")
