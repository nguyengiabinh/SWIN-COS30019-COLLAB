# knowledge_base.py
import re
from File_Reader import read, extract_text

def build_knowledge_base(filename):
    """
    Builds a knowledge base from the given file.
    
    Args:
        filename (str): The name of the file containing the knowledge base.
        
    Returns:
        dict: A dictionary representing the knowledge base.
    """
    tell, ask = read(filename)
    symbols, sentences = extract_text(tell)
    
    knowledge_base = {}
    
    for sentence in sentences:
        if "=>" in sentence:
            premise, conclusion = sentence.split("=>")
            premise_parts = re.split(r'(&)', premise)
            premise = frozenset(part for part in premise_parts if part != '&')
            conclusion = conclusion
            
            if premise not in knowledge_base:
                knowledge_base[premise] = set()
            knowledge_base[premise].add(conclusion)
        else:
            # Treat the sentence as a fact
            premise = frozenset()
            conclusion = sentence
            
            if premise not in knowledge_base:
                knowledge_base[premise] = set()
            knowledge_base[premise].add(conclusion)
    
    return knowledge_base

def print_knowledge_base(knowledge_base):
    """
    Prints the knowledge base in a readable format.
    
    Args:
        knowledge_base (dict): The knowledge base to be printed.
    """
    for premise, conclusions in knowledge_base.items():
        if not premise:
            print(f"Facts: {', '.join(conclusions)}")
        else:
            premise_str = ' & '.join(sorted(premise))
            print(f"{premise_str} => {', '.join(conclusions)}")
            
    