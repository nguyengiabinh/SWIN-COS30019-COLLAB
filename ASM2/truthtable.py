from itertools import product
from tabulate import tabulate
from typing import Dict, Generator, Any, List, Tuple, Union  
from Parser import *  
from logic import Conjunction, model_check  

class TruthTable:
    def __init__(self, symbols: List[str], knowledgeBase: Union[Conjunction, List[Any]], query: Union[str, Any]):
        if not all(isinstance(symbol, str) for symbol in symbols):
            raise ValueError("All symbols must be strings.")
        if not isinstance(knowledgeBase, (Conjunction, list)) or (isinstance(knowledgeBase, list) and not all(isinstance(kb, Conjunction) for kb in knowledgeBase)):
            raise ValueError("Knowledge base must be a Conjunction or a list of Conjunctions.")
        if not isinstance(query, str) and not hasattr(query, "evaluate"):
            raise ValueError("Query must be a string or an object with an 'evaluate' method.")
        
        self.symbols = sorted(symbols)
        self.knowledgeBase = Conjunction(*knowledgeBase) if isinstance(knowledgeBase, list) else knowledgeBase
        self.query = self.parse(query) if isinstance(query, str) else query
        self.table = list(self.generate_table())  # Generate and store the table
        self.count = 0

    def generate_table(self) -> Generator[Tuple[Dict[str, bool], bool, bool], None, None]:
        combinations = product([True, False], repeat=len(self.symbols))
        for combination in combinations:
            model = dict(zip(self.symbols, combination))
            yield (model, self.knowledgeBase.evaluate(model), self.query.evaluate(model))

    def check_facts(self) -> None:
        self.count = sum(1 for model, kb_eval, query_eval in self.table if kb_eval and query_eval)

    def brute_force_check(self) -> bool:
        return model_check(self.knowledgeBase, self.query)

    def get_entailed_symbols(self) -> str:
        self.check_facts()
        valid = self.brute_force_check()
        return f'YES: {self.count}' if self.count > 0 and valid else f'NO {self.query}'

    def __str__(self) -> str:
        headers = self.symbols + ["Tell Eval", "Ask Eval"]
        rows = [(list(model.values()) + [kb_eval, query_eval]) for model, kb_eval, query_eval in self.table]
        return tabulate(rows, headers=headers, tablefmt='fancy_grid')