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
        conjuncts = list(self.KB.conjuncts())  # Reduce calls to self.KB.conjuncts()

        for rule in conjuncts:
            if isinstance(rule, Implication):
                premise_count[rule] = len(self.KB.conjunct_premise(rule))

        facts = deque([str(fact) for fact in conjuncts if isinstance(fact, Symbol)])
        deduced = {fact: False for fact in self.KB.symbols()}

        while facts:
            current_fact = facts.popleft()
            result_chain.append(current_fact)
            if current_fact == self.query:
                return True, result_chain
            if not deduced[current_fact]:
                deduced[current_fact] = True
                for rule in conjuncts:
                    if isinstance(rule, Implication) and current_fact in self.KB.conjunct_premise(rule):
                        premise_count[rule] -= 1
                        if premise_count[rule] == 0 and not deduced[self.KB.conjunct_conclusion(rule)]:
                            facts.append(self.KB.conjunct_conclusion(rule))
        return False, []

    def solve(self):
        has_solution, result_chain = self.evaluate()
        return "YES: " + ', '.join(result_chain) if has_solution else "NO"

