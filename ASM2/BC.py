from Parser import *

class BackwardChaining:
    def __init__(self, KnowledgeBase, target):
        self.KB = KnowledgeBase
        self.goal = target

    def __str__(self) -> str:
        pass

    def verify(self, skipped, sequence, objective, conjuncts):
        for element in conjuncts:
            if isinstance(element, Symbol) and objective == str(element):
                sequence.add(objective)
                return True, sequence

        skipped.add(objective)

        for element in conjuncts:
            if isinstance(element, Implication) and objective == self.KB.conjunct_conclusion(element):
                truth_check = True
                for prerequisite in self.KB.conjunct_premise(element):
                    if prerequisite in sequence or prerequisite in skipped:
                        continue
                    verified, sequence = self.verify(skipped, sequence, prerequisite, conjuncts)
                    if not verified:
                        truth_check = False
                        break
                if truth_check:
                    sequence.add(objective)
                    return True, sequence
        return False, sequence

    def entails(self):
        conjuncts = list(self.KB.conjuncts())
        symbols = {str(item) for item in conjuncts if isinstance(item, Symbol)}
        if self.goal in symbols:
            return True, {self.goal}
        else:
            return self.verify(set(), set(), self.goal, conjuncts)

    def solve(self):
        found, sequence = self.entails()
        sequence = list(sequence)  # Convert back to list if needed for specific ordering or output format
        return "YES: " + ', '.join(sequence) if found else "NO"
