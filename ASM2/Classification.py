from Reader import read, extract_symbols_and_sentences
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
        if hasattr(parsed[0], 'asList'):
            return parsed[0].asList()
        else:
            return [parsed[0]]   # Return a list with the single literal
    except Exception as e:
        print(f"Error parsing sentence '{sentence}': {e}")
        return []

def is_fact(expression):
    """Check if the expression is a fact (single positive literal), adjusted for list-wrapped literals."""
    if isinstance(expression, list) and len(expression) == 1:
        expression = expression[0]
    return isinstance(expression, str) and not expression.startswith("~")

def is_horn_clause(expression):
    """Broadens Horn clause definition to include disjunctions with one positive literal."""
    if isinstance(expression, list):
        if len(expression) == 1 and not expression[0].startswith("~"):
            return True
        elif len(expression) == 3 and expression[1] == "=>":
            conclusion = expression[2]
            if not conclusion.startswith("~"):
                return True
        elif len(expression) == 3 and expression[1] == "||":
            literals = [expression[0], expression[2]]
            positive_literals = [lit for lit in literals if not isinstance(lit, list) or not lit[0].startswith("~")]
            if len(positive_literals) == 1:
                return True
    return False

def add_horn_clause(knowledge_base, clause):
    """Adds identified Horn clause to knowledge base."""
    if is_fact(clause):
        knowledge_base["facts"].add(clause)
    elif isinstance(clause, list):
        knowledge_base["implications"].append(clause)

def add_fact(knowledge_base, literal):
    """Ensures literals are added as facts to the knowledge base, handling list-wrapped literals."""
    # Unwrap the literal if it's a single-item list
    if isinstance(literal, list) and len(literal) == 1:
        literal = literal[0]
    # Now, literal is guaranteed to be not a list; add it to the set of facts
    knowledge_base["facts"].add(literal)

def build_knowledge_base(filename):
    tell, ask = read(filename)
    symbols, sentences = extract_symbols_and_sentences(tell)
    
    knowledge_base = {"facts": set(), "implications": []}
    
    for sentence in sentences:
        parsed_sentence = parse_logical_expression(sentence)
        if is_fact(parsed_sentence):
            add_fact(knowledge_base, parsed_sentence)
        elif is_horn_clause(parsed_sentence):
            add_horn_clause(knowledge_base, parsed_sentence)
        else:
            print(f"Non-Horn clause detected, skipping: {parsed_sentence}")
    
    return knowledge_base, ask

def print_knowledge_base(knowledge_base):
    print("Facts:", ", ".join(sorted(knowledge_base["facts"])))
    print("Horn Clause: ")
    for clause in knowledge_base["implications"]:
        print(clause)


