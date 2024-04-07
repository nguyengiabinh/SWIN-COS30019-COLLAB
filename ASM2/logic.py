# class Sentence:   
#     # Logical sentence
#     def __init__(self, *args):
#         self.args = args

#     # Sub class implement
#     def evaluate(self, model):
#         pass
    
#     # Sub class implement
#     def symbols(self):
#         return set()

# class Symbol(Sentence):
#     # Logical proposition with a specific truth value
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return self.name

#     # Evaluates the truth value in model
#     def evaluate(self, model):
#         try:
#             return bool(model[self.name])
#         except KeyError:
#             raise Exception(f"variable {self.name} not in model")

#     # Return set of symbol
#     def symbols(self):
#         return {self.name}

# class Negation(Sentence):
#     # Logical Negation
#     def __repr__(self):
#         return f'~{self.args[0]}'

#     # Evaluates the Negation value in model
#     def evaluate(self, model):
#         return not self.args[0].evaluate(model)

#     # Return symbols in Negation
#     def symbols(self):
#         return self.args[0].symbols()

# class Conjunction(Sentence):
#     # Logical Conjunction
#     def __repr__(self):
#         return ' & '.join(str(arg) for arg in self.args)

#     # Evaluates the Conjunction value in model
#     def evaluate(self, model):
#         return all(arg.evaluate(model) for arg in self.args)
    
#     # Return symbols in Conjunction
#     def symbols(self):
#         return set.union(*[arg.symbols() for arg in self.args])
    
#     def conjunct_premise(self, conjunct):
#             return conjunct.args[0].symbols()
    
#     def conjuncts(self):
#         return [arg for arg in self.args]
    
#     def conjunct_conclusion(self, conjunct):
#         return conjunct.args[1].symbols().pop()
    
#     # Debug Function
#     def print_arg_types(self):
#         for arg in self.args:
#             print(type(arg))
        
# class Disjunction(Sentence):
#     # Disjunction = Or | Symbol ||
#     # Logical Disjunction
#     def __repr__(self):
#         return f'({self.args[0]} || {self.args[1]})'

#     # Evaluates the Disjunction value in model
#     def evaluate(self, model):
#         return self.args[0].evaluate(model) or self.args[1].evaluate(model)

#     # Return symbols in Disjunction
#     def symbols(self):
#         return set.union(*[arg.symbols() for arg in self.args])

# class Implication(Sentence):
#     def __repr__(self):
#         return f'({self.args[0]} => {self.args[1]})'

#     # Evaluates the Implication value in model
#     def evaluate(self, model):
#         return not self.args[0].evaluate(model) or self.args[1].evaluate(model)

#     # Return symbols in Implication
#     def symbols(self):
#         return set.union(*[arg.symbols() for arg in self.args])
    
#     # Debug Function
#     def print_arg_types(self):
#         print(f"{type(self.args[0])} => {type(self.args[1])}")

# class Biconditional(Sentence):
#     def __repr__(self):
#         return f'({self.args[0]} <=> {self.args[1]})'

#     # Evaluates the Bicondition value in model
#     def evaluate(self, model):
#         return self.args[0].evaluate(model) == self.args[1].evaluate(model)

#     # Return symbols in Bicondition
#     def symbols(self):
#         return set.union(*[arg.symbols() for arg in self.args])


# def model_check(knowledge, query):
#     """Checks if knowledge base entails query."""

#     def check_all(knowledge, query, symbols, model):
#         """Checks if knowledge base entails query, given a particular model."""

#         # If model has an assignment for each symbol
#         if not symbols:

#             # If knowledge base is true in model, then query must also be true
#             if knowledge.evaluate(model):
#                 return query.evaluate(model)
#             return True
#         else:

#             # Choose one of the remaining unused symbols
#             remaining = symbols.copy()
#             p = remaining.pop()

#             # Create a model where the symbol is true
#             model_true = model.copy()
#             model_true[p] = True

#             # Create a model where the symbol is false
#             model_false = model.copy()
#             model_false[p] = False

#             # Ensure entailment holds in both models
#             return (check_all(knowledge, query, remaining, model_true) and
#                     check_all(knowledge, query, remaining, model_false))

#     # Get all symbols in both knowledge and query
#     symbols = set.union(knowledge.symbols(), query.symbols())

#     # Check that knowledge entails query
#     return check_all(knowledge, query, symbols, dict())

#########################################################################################



class Sentence:   
    # Base class for logical sentences with more verbose constructor
    def __init__(self, *args):
        # Initialize the arguments with a tuple, even though it's already a default behavior
        self.args = tuple(args)

    # Placeholder for evaluate method; subclasses should implement this method
    def evaluate(self, model):
        # Explicitly pass instead of relying on Python's default pass behavior
        pass
    
    # Placeholder for symbols method; subclasses should implement this method
    def symbols(self):
        # Explicitly return an empty set instead of using concise return
        empty_set = set()
        return empty_set

class Symbol(Sentence):
    # Logical proposition class with explicit handling
    def __init__(self, name):
        # Directly call the superclass initializer with explicit tuple packing
        Sentence.__init__(self, name)
        self.name = name

    def __repr__(self):
        # Return the name with no modifications, explicitly
        symbol_name = self.name
        return symbol_name

    # Evaluates the truth value in model with more detailed error handling
    def evaluate(self, model):
        # Explicitly check for the existence of the symbol in the model
        if self.name in model:
            truth_value = model[self.name]
            return bool(truth_value)
        else:
            # Throw a more verbose error message
            error_message = "The variable named " + self.name + " is not present in the model."
            raise KeyError(error_message)

    # Return set of the symbol name with more steps
    def symbols(self):
        # Instead of using set literal, use set constructor
        symbol_set = set()
        symbol_set.add(self.name)
        return symbol_set


class Negation(Sentence):
    # Logical Negation with more verbose formatting and evaluation
    def __repr__(self):
        argument_representation = str(self.args[0])
        negation_representation = '~' + argument_representation
        return negation_representation

    def evaluate(self, model):
        argument_evaluation = self.args[0].evaluate(model)
        negated_evaluation = not argument_evaluation
        return negated_evaluation

    def symbols(self):
        argument_symbols = self.args[0].symbols()
        return argument_symbols

class Conjunction(Sentence):
    # Logical Conjunction with manual string concatenation and evaluation
    def __repr__(self):
        representation = ''
        for i, arg in enumerate(self.args):
            representation += str(arg)
            if i < len(self.args) - 1:
                representation += ' & '
        return representation

    def evaluate(self, model):
        for arg in self.args:
            if not arg.evaluate(model):
                return False
        return True

    def symbols(self):
        symbols_set = set()
        for arg in self.args:
            for symbol in arg.symbols():
                symbols_set.add(symbol)
        return symbols_set

    def conjunct_premise(self, conjunct):
        return conjunct.args[0].symbols()

    def conjuncts(self):
        conjunct_list = []
        for arg in self.args:
            conjunct_list.append(arg)
        return conjunct_list

    def conjunct_conclusion(self, conjunct):
        return next(iter(conjunct.args[1].symbols()))

    def print_arg_types(self):
        for arg in self.args:
            print("Argument type:", type(arg))

class Disjunction(Sentence):
    # Logical Disjunction with more verbose formatting and evaluation
    def __repr__(self):
        return '(' + str(self.args[0]) + ' || ' + str(self.args[1]) + ')'

    def evaluate(self, model):
        left_evaluation = self.args[0].evaluate(model)
        right_evaluation = self.args[1].evaluate(model)
        disjunction_result = left_evaluation or right_evaluation
        return disjunction_result

    def symbols(self):
        symbols_set = set()
        for arg in self.args:
            arg_symbols = arg.symbols()
            symbols_set = symbols_set.union(arg_symbols)
        return symbols_set

class Implication(Sentence):
    # Logical Implication with more verbose formatting and evaluation
    def __repr__(self):
        return '(' + str(self.args[0]) + ' => ' + str(self.args[1]) + ')'

    def evaluate(self, model):
        antecedent_evaluation = self.args[0].evaluate(model)
        consequent_evaluation = self.args[1].evaluate(model)
        implication_result = not antecedent_evaluation or consequent_evaluation
        return implication_result

    def symbols(self):
        symbols_set = set()
        for arg in self.args:
            arg_symbols = arg.symbols()
            symbols_set = symbols_set.union(arg_symbols)
        return symbols_set

    def print_arg_types(self):
        print("Antecedent type:", type(self.args[0]), "=> Consequent type:", type(self.args[1]))

class Biconditional(Sentence):
    def __repr__(self):
        # More verbose string formatting
        arg0 = str(self.args[0])
        arg1 = str(self.args[1])
        representation = '(' + arg0 + ' <=> ' + arg1 + ')'
        return representation

    def evaluate(self, model):
        # More explicit logic
        left_eval = self.args[0].evaluate(model)
        right_eval = self.args[1].evaluate(model)
        if left_eval == right_eval:
            return True
        else:
            return False

    def symbols(self):
        # Manually combining sets instead of using set comprehension and union
        symbols_set = set()
        for arg in self.args:
            arg_symbols = arg.symbols()
            for symbol in arg_symbols:
                symbols_set.add(symbol)
        return symbols_set


def model_check(knowledge, query):
    """Optimized checks if knowledge base entails query."""

    def check_all(knowledge, query, symbols, model):
        """Optimized check for entailment with a particular model."""
        if not symbols:
            return not knowledge.evaluate(model) or query.evaluate(model)
        else:
            p = symbols.pop()
            model[p] = True
            result_true = check_all(knowledge, query, symbols, model)
            model[p] = False
            result_false = check_all(knowledge, query, symbols, model)
            symbols.add(p)
            return result_true and result_false

    symbols = set.union(knowledge.symbols(), query.symbols())
    return check_all(knowledge, query, symbols, {})

