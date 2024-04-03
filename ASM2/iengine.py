import sys
from Reader import *
from sentence_transformers import *
from logic import *
from truthtable import *
from backward_chaining import *
from forward_chaining import *

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

    knowledge_base = create_knowledge_base(sentences) # Transform sentence into logical sentence
    query_sentence = parse(ask)

    # Model Check
    is_Valid = model_check(knowledge_base, query_sentence)
    # Output the results
    print('\nResults:')
    if method == "TT":
        # Create a TruthTable instance
        truth_table = TruthTable(symbols, knowledge_base, query_sentence)
        entailed_symbols = truth_table.get_entailed_symbols()
        print(truth_table)
        print(entailed_symbols)
    elif method == "FC":
        # Forward Chaining
        fc = ForwardChaining(knowledge_base, ask)
        fc_result = fc.solve()
        print(fc_result)
    elif method == "BC":
        # Backward Chaining
        bc = BackwardChaining(knowledge_base, ask)
        bc_result = bc.solve()
        print(bc_result)

if __name__ == "__main__":
    method = input("input method (TT/FC/BC): ")
    filename = 'test2.txt'
    main(method, filename)

