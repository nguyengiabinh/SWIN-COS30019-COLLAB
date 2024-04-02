from File_Reader import read, extract_text
from pyparsing import ParserElement, infixNotation, opAssoc, oneOf, Word, alphas, alphanums

# Improves parsing performance
ParserElement.enablePackrat()

# Define basic elements
var = Word(alphas, alphanums + "_")
operator = oneOf("~ & || => <=>")

# Define expression with comprehensive handling for nested and complex logical structures
expr = infixNotation(var, [
    ("~", 1, opAssoc.RIGHT),
    ("&", 2, opAssoc.LEFT),
    ("||", 2, opAssoc.LEFT),
    ("=>", 2, opAssoc.RIGHT),
    ("<=>", 2, opAssoc.RIGHT),
])

def parse_logical_expression(sentence):
    try:
        parsed = expr.parseString(sentence, parseAll=True)
        return parsed[0]  # Return the first (and only) element of the parsed result
    except Exception as e:
        print(f"Error parsing sentence '{sentence}': {e}")
        return []

def is_fact(expression):
    """Check if the expression is a fact (single positive literal)."""
    return isinstance(expression, str) and not expression.startswith("~")

def is_horn_clause(expression):
    """Check if the expression is a Horn clause (including facts and implications with a single positive literal conclusion)."""
    if is_fact(expression):  # Single positive literal is a Horn clause (fact)
        return True
    if isinstance(expression, list):
        # Implication with a single positive literal conclusion and literals as premises
        if len(expression) == 3 and expression[1] == "=>":
            conclusion = expression[2]
            premises = expression[0]
            if is_fact(conclusion):  # Check if conclusion is a single positive literal
                # Check if premises are literals (negated or positive)
                if isinstance(premises, str):
                    return True  # Single premise
                elif isinstance(premises, list):
                    for premise in premises:
                        # Each premise must be a positive literal or negated literal
                        if not is_fact(premise) and not (isinstance(premise, list) and premise[0] == "~" and is_fact(premise[1])):
                            return False  # Non-literal found, not a Horn clause
                    return True  # All premises are literals
    return False  # Default case if none of the above conditions are met

def add_horn_clause(knowledge_base, clause):
    """Add a Horn clause to the knowledge base."""
    if is_fact(clause):  # If it's a fact
        knowledge_base["facts"].add(clause)
    else:  # If it's an implication
        premises, conclusion = clause[0], clause[2]
        # Ensure premises are handled as a list
        if isinstance(premises, str):
            premises = [premises]
        elif isinstance(premises, list):
            # Simplify nested lists if any
            flattened_premises = []
            for prem in premises:
                if isinstance(prem, list) and prem[0] == '~':
                    # Keeping negation as part of the premise
                    flattened_premises.append(f"~{prem[1]}")
                else:
                    flattened_premises.append(prem)
            premises = flattened_premises

        knowledge_base["implications"].setdefault(conclusion, []).append(premises)


def build_knowledge_base(filename):
    tell, ask = read(filename)
    symbols, sentences = extract_text(tell)
    
    knowledge_base = {"facts": set(), "implications": {}}
    
    for sentence in sentences:
        parsed_sentence = parse_logical_expression(sentence)
        if is_horn_clause(parsed_sentence):
            add_horn_clause(knowledge_base, parsed_sentence)
        else:
            print(f"Non-Horn clause detected, skipping: {parsed_sentence}")
    
    return knowledge_base, ask

def print_knowledge_base(knowledge_base):
    print("Facts:", ", ".join(knowledge_base["facts"]))
    for conclusion, premises_list in knowledge_base["implications"].items():
        for premises in premises_list:
            print(f"{' & '.join(premises)} => {conclusion}")

