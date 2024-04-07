# import re
# from lark import Lark, Transformer
# from truthtable import *
# from logic import *

# # Precompile regular expression for efficiency
# split_re = re.compile(r'\s*&\s*')

# class Parser:
#     def __init__(self, grammar):
#         self.grammar = grammar
#         self.cursor = 0

#     def skip_whitespace(self):
#         while self.cursor < len(self.grammar) and self.grammar[self.cursor].isspace():
#             self.cursor += 1

#     def expect(self, pattern):
#         self.skip_whitespace()
#         if self.grammar.startswith(pattern, self.cursor):
#             self.cursor += len(pattern)
#             return True
#         return False

#     def extract_symbol(self):
#         self.skip_whitespace()
#         symbol_start = self.cursor
#         while self.cursor < len(self.grammar) and self.grammar[self.cursor].isalnum():
#             self.cursor += 1
#         return Symbol(self.grammar[symbol_start:self.cursor])

#     def analyze_atom(self):
#         if self.expect("("):
#             atom_result = self.analyze_biconditional()
#             if not self.expect(")"):
#                 raise Exception("Missing ')'")
#             return atom_result
#         return self.extract_symbol()

#     def analyze_negation(self):
#         if self.expect("~"):
#             return Negation(self.analyze_atom())
#         return self.analyze_atom()

#     def analyze_conjunction(self):
#         conjunction_result = self.analyze_disjunction()
#         while self.expect("&"):
#             conjunction_result = Conjunction(conjunction_result, self.analyze_disjunction())
#         return conjunction_result

#     def analyze_disjunction(self):
#         disjunction_result = self.analyze_negation()
#         while self.expect("||"):
#             disjunction_result = Disjunction(disjunction_result, self.analyze_negation())
#         return disjunction_result

#     def analyze_implication(self):
#         implication_result = self.analyze_conjunction()
#         while self.expect("=>"):
#             implication_result = Implication(implication_result, self.analyze_conjunction())
#         return implication_result

#     def analyze_biconditional(self):
#         biconditional_result = self.analyze_implication()
#         while self.expect("<=>"):
#             biconditional_result = Biconditional(biconditional_result, self.analyze_implication())
#         return biconditional_result

#     def parse(self):
#         return self.analyze_biconditional()

# class SentenceTransformer(Transformer):
#     # Transformer methods remain unchanged
#     def symbol(self, args):
#         return Symbol(args[0].value)

#     def atom(self, args):
#         return args[0]

#     def negation(self, args):
#         return Negation(args[0])

#     def conjunction(self, args):
#         return Conjunction(*args)

#     def disjunction(self, args):
#         return Disjunction(*args)

#     def implication(self, args):
#         return Implication(*args)

#     def biconditional(self, args):
#         return Biconditional(*args)

# # Initialize the Lark parser once to optimize performance
# grammar_parser = Lark(r"""
#     ?start: biconditional
#     ?biconditional: implication
#                   | biconditional "<=>" implication -> biconditional
#     ?implication: conjunction
#                 | implication "=>" conjunction -> implication
#     ?conjunction: disjunction
#                 | conjunction "&" disjunction -> conjunction
#     ?disjunction: negation
#                 | disjunction "||" negation -> disjunction
#     ?negation: "~" atom -> negation
#             | atom
#     atom: symbol
#         | "(" biconditional ")"
#     symbol: /[a-z0-9_]+/
#     %import common.WS
#     %ignore WS
# """, start='start', parser='lalr', transformer=SentenceTransformer())

# def parse(sentence):
#     return Parser(sentence).parse()

# def parse1(sentence):
#     return grammar_parser.parse(sentence)

# def construct_knowledge_base(statements):
#     parsed_statements = []
#     print("\nParsed statements: ")
#     for statement in statements:
#         parsed = parse(statement.strip())
#         print(parsed)
#         parsed_statements.append(parsed)
#     knowledge = Conjunction(*parsed_statements)
#     return knowledge

# def interpret_knowledge_base(kb_string):
#     statement_list = []
#     propositions = split_re.split(kb_string)

#     for proposition in propositions:
#         if "=>" in proposition:
#             premises, conclusion = proposition.strip("()").split(" => ")
#             if " & " in premises:
#                 parts = [Symbol(part.strip()) for part in premises.split(" & ")]
#                 statement_list.append(Implication(Conjunction(*parts), Symbol(conclusion)))
#             else:
#                 statement_list.append(Implication(Symbol(premises), Symbol(conclusion)))
#         else:
#             statement_list.append(Symbol(proposition))
#     return statement_list

# def convert_knowledge_base_to_text(kb_structure):
#     kb_text = ""
#     for element in kb_structure.args:
#         if isinstance(element, Implication):
#             premise_part = element.args[0]
#             conclusion_part = element.args[1]
#             if isinstance(premise_part, Conjunction):
#                 conjunction_parts = " & ".join(str(arg) for arg in premise_part.args)
#                 kb_text += f"({conjunction_parts} => {conclusion_part})"
#             else:
#                 kb_text += f"({premise_part} => {conclusion_part})"
#         else:
#             kb_text += str(element)
#         kb_text += " & "
#     return kb_text[:-3]

##############################################################################################

import re
from lark import Lark, Transformer

# Assuming the classes from 'truthtable' and 'logic' are defined elsewhere:
from truthtable import *
from logic import *

# Use Lark for parsing to leverage its power and simplify our code
grammar = r"""
    ?start: biconditional
    ?biconditional: implication
                  | biconditional "<=>" implication -> biconditional
    ?implication: conjunction
                | implication "=>" conjunction -> implication
    ?conjunction: disjunction
                | conjunction "&" disjunction -> conjunction
    ?disjunction: negation
                | disjunction "||" negation -> disjunction
    ?negation: "~" atom -> negation
            | atom
    atom: symbol
        | "(" biconditional ")"
    symbol: /[a-z0-9_]+/
    %import common.WS
    %ignore WS
"""

# Use a custom exception for clearer error reporting
class ParsingException(Exception):
    pass

class SentenceTransformer(Transformer):
    def symbol(self, args):
        return Symbol(args[0].value)

    def atom(self, args):
        return args[0]

    def negation(self, args):
        return Negation(args[0])

    def conjunction(self, args):
        return Conjunction(*args)

    def disjunction(self, args):
        return Disjunction(*args)

    def implication(self, args):
        return Implication(*args)

    def biconditional(self, args):
        return Biconditional(*args)

# Initialize Lark with the grammar and transformer
grammar_parser = Lark(grammar, start='start', parser='lalr', transformer=SentenceTransformer())

def parse(sentence):
    try:
        return grammar_parser.parse(sentence)
    except Exception as e:
        raise ParsingException(f"Failed to parse the sentence: {sentence}. Error: {e}")

def construct_knowledge_base(statements):
    parsed_statements = []
    print("\nParsed statements: ")
    for statement in statements:
        parsed = parse(statement.strip())
        print(parsed)
        parsed_statements.append(parsed)
    knowledge = Conjunction(*parsed_statements)
    return knowledge

def interpret_knowledge_base(kb_string):
    # Precompile regular expression for efficiency
    split_re = re.compile(r'\s*&\s*')
    statement_list = []
    propositions = split_re.split(kb_string)

    for proposition in propositions:
        if "=>" in proposition:
            premises, conclusion = proposition.strip("()").split(" => ")
            if " & " in premises:
                parts = [Symbol(part.strip()) for part in premises.split(" & ")]
                statement_list.append(Implication(Conjunction(*parts), Symbol(conclusion.strip())))
            else:
                statement_list.append(Implication(Symbol(premises.strip()), Symbol(conclusion.strip())))
        else:
            statement_list.append(Symbol(proposition.strip()))
    return statement_list

def convert_knowledge_base_to_text(kb_structure):
    kb_text = ""
    for element in kb_structure.args:
        if isinstance(element, Implication):
            premise_part = element.args[0]
            conclusion_part = element.args[1]
            if isinstance(premise_part, Conjunction):
                conjunction_parts = " & ".join(str(arg) for arg in premise_part.args)
                kb_text += f"({conjunction_parts} => {conclusion_part})"
            else:
                kb_text += f"({premise_part} => {conclusion_part})"
        else:
            kb_text += str(element)
        kb_text += " & "
    return kb_text[:-3]
