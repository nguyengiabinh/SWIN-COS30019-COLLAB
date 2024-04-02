# # knowledge_base.py
# import re
# from File_Reader import read, extract_text

# def build_knowledge_base(filename):
#     """
#     Builds a knowledge base from the given file.
    
#     Args:
#         filename (str): The name of the file containing the knowledge base.
        
#     Returns:
#         dict: A dictionary representing the knowledge base.
#     """
#     tell, ask = read(filename)
#     symbols, sentences = extract_text(tell)
    
#     knowledge_base = {}
    
#     for sentence in sentences:
#         if "=>" in sentence:
#             premise, conclusion = sentence.split("=>")
#             premise_parts = re.split(r'(&)', premise)
#             premise = frozenset(part for part in premise_parts if part != '&')
#             conclusion = conclusion
            
#             if premise not in knowledge_base:
#                 knowledge_base[premise] = set()
#             knowledge_base[premise].add(conclusion)
#         else:
#             # Treat the sentence as a fact
#             premise = frozenset()
#             conclusion = sentence
            
#             if premise not in knowledge_base:
#                 knowledge_base[premise] = set()
#             knowledge_base[premise].add(conclusion)
    
#     return knowledge_base

# def print_knowledge_base(knowledge_base):
#     """
#     Prints the knowledge base in a readable format.
    
#     Args:
#         knowledge_base (dict): The knowledge base to be printed.
#     """
#     for premise, conclusions in knowledge_base.items():
#         if not premise:
#             print(f"Facts: {', '.join(conclusions)}")
#         else:
#             premise_str = ' & '.join(sorted(premise))
#             print(f"{premise_str} => {', '.join(conclusions)}")
            
      
      
            
  # knowledge_base.py
import re
from File_Reader import read, extract_text

def build_knowledge_base(filename):
    """
    Builds a knowledge base from the given file.
    """
    tell, ask = read(filename)
    symbols, sentences = extract_text(tell)
    
    knowledge_base = {}
    
    for sentence in sentences:
        if "=>" in sentence:
            premise, conclusion = sentence.split("=>")
            premise_parts = re.split(r'(&)', premise)
            premise = frozenset(part for part in premise_parts if part != '&')
            if premise not in knowledge_base:
                knowledge_base[premise] = set()
            knowledge_base[premise].add(conclusion)
        else:
            # Treat the sentence as a fact
            premise = frozenset()
            if premise not in knowledge_base:
                knowledge_base[premise] = set()
            knowledge_base[premise].add(sentence)
    
    return knowledge_base

def print_knowledge_base(knowledge_base):
    """
    Prints the knowledge base in a readable format.
    """
    for premise, conclusions in knowledge_base.items():
        if not premise:
            print(f"Facts: {', '.join(conclusions)}")
        else:
            premise_str = ' & '.join(sorted(premise))
            print(f"{premise_str} => {', '.join(conclusions)}")

# def backward_chaining(knowledge_base, query, proven=None, counts=None):
#     if proven is None:
#         proven = set()
#     if counts is None:
#         counts = {'yes': 0, 'no': 0}

#     if query in proven:
#         counts['yes'] += 1
#         return True, counts

#     if frozenset() in knowledge_base and query in knowledge_base[frozenset()]:
#         proven.add(query)
#         counts['yes'] += 1
#         return True, counts

#     for premises, conclusions in knowledge_base.items():
#         if query in conclusions:
#             all_proven = True
#             for premise in premises:
#                 proven_result, counts = backward_chaining(knowledge_base, premise, proven, counts)
#                 if not proven_result:
#                     all_proven = False
#                     break
#             if all_proven:
#                 proven.add(query)
#                 counts['yes'] += 1
#                 return True, counts

#     counts['no'] += 1
#     return False, counts

# back_chaing need to modify the main function into main.py file

# def main():
#     filename = 'test2.txt'
#     kb = build_knowledge_base(filename)
#     query = 'd'
    
#     result, counts = backward_chaining(kb, query)
#     if result:
#         print(f"YES, proven {counts['yes']} times, not proven {counts['no']} times")
#     else:
#         print(f"NO, proven {counts['yes']} times, not proven {counts['no']} times")

# if __name__ == "__main__":
#     main()


def forward_chaining(knowledge_base, query):
    # Initialize known facts and inference counts
    known_facts = set()
    counts = {'yes': 0, 'no': 0}
    
    # Populate initial facts from the knowledge base
    for premises, conclusions in knowledge_base.items():
        if not premises:  # Facts have no premises
            known_facts.update(conclusions)

    # Track if new facts are inferred in each iteration to continue or break the loop
    new_inferences = True
    while new_inferences:
        new_inferences = False
        for premises, conclusions in knowledge_base.items():
            if premises <= known_facts and not conclusions.isdisjoint(known_facts) == False:
                # If all premises are known and the conclusion is not already known
                new_facts = conclusions - known_facts
                if new_facts:
                    known_facts.update(new_facts)
                    new_inferences = True
                    if query in new_facts:
                        counts['yes'] += 1
                        return True, counts

    if query not in known_facts:
        counts['no'] += 1
    return False, counts

# forward_chaing need to modify the main function into main.py file

def main():
    filename = 'test2.txt'
    kb = build_knowledge_base(filename)
    query = 'd'
    
    result, counts = forward_chaining(kb, query)
    if result:
        print(f"YES, proven {counts['yes']} times, not proven {counts['no']} times")
    else:
        print(f"NO, proven {counts['yes']} times, not proven {counts['no']} times")

if __name__ == "__main__":
    main()
