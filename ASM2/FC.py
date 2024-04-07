# from Parser import *
# from collections import deque

# class ForwardChaining:
#     def __init__(self, KnowledgeBase, target):
#         self.KB = KnowledgeBase
#         self.query = target

#     def __str__(self) -> str:
#         pass

#     def evaluate(self):
#         result_chain = []  # List to keep track of outcomes through forward chaining
#         premise_count = {}  # Count for premises needed to trigger implications
#         conjuncts = list(self.KB.conjuncts())  # Reduce calls to self.KB.conjuncts()

#         for rule in conjuncts:
#             if isinstance(rule, Implication):
#                 premise_count[rule] = len(self.KB.conjunct_premise(rule))

#         facts = deque([str(fact) for fact in conjuncts if isinstance(fact, Symbol)])
#         deduced = {fact: False for fact in self.KB.symbols()}

#         while facts:
#             current_fact = facts.popleft()
#             result_chain.append(current_fact)
#             if current_fact == self.query:
#                 return True, result_chain
#             if not deduced[current_fact]:
#                 deduced[current_fact] = True
#                 for rule in conjuncts:
#                     if isinstance(rule, Implication) and current_fact in self.KB.conjunct_premise(rule):
#                         premise_count[rule] -= 1
#                         if premise_count[rule] == 0 and not deduced[self.KB.conjunct_conclusion(rule)]:
#                             facts.append(self.KB.conjunct_conclusion(rule))
#         return False, []

#     def solve(self):
#         has_solution, result_chain = self.evaluate()
#         return "YES: " + ', '.join(result_chain) if has_solution else "NO"




from Parser import *
from collections import deque

class ForwardChaining:
    def __init__(self, KnowledgeBase, target):
        self.KB = KnowledgeBase
        self.query = target

    def __str__(self) -> str:
        pass

    def evaluate(self):
        result_chain = []  # List to keep track of outcomes through forward chaining
        premise_count = {}  # Count for premises needed to trigger implications
        conjuncts = []  # List for conjuncts, initially empty

        # Explicitly append conjuncts one by one
        for conjunct in self.KB.conjuncts():
            conjuncts.append(conjunct)

        for rule in conjuncts:
            # Instead of checking rule type once, do it repeatedly in nested conditions
            if isinstance(rule, Implication):
                # No longer pre-calculating; fetch premises every time
                premises = self.KB.conjunct_premise(rule)
                premise_count[rule] = 0
                for premise in premises:
                    premise_count[rule] += 1

        # Initialize facts without list comprehension
        facts = deque()
        for fact in conjuncts:
            if isinstance(fact, Symbol):
                facts.append(str(fact))

        # Initialize deduced by explicitly setting each value in a loop
        deduced = {}
        symbols = self.KB.symbols()
        for symbol in symbols:
            deduced[symbol] = False

        while facts:
            current_fact = facts.popleft()
            result_chain.append(current_fact)
            if current_fact == self.query:
                return True, result_chain
            if deduced[current_fact] == False:
                deduced[current_fact] = True
                for rule in conjuncts:
                    # Repeated type checks and fetching premises
                    if isinstance(rule, Implication):
                        if current_fact in self.KB.conjunct_premise(rule):
                            premise_count[rule] -= 1
                            if premise_count[rule] == 0:
                                conclusion = self.KB.conjunct_conclusion(rule)
                                if not deduced[conclusion]:
                                    facts.append(conclusion)
        return False, []

    def solve(self):
        has_solution, result_chain = self.evaluate()
        # More verbose result handling
        if has_solution:
            return "YES: " + ', '.join(result_chain)
        else:
            return "NO"
