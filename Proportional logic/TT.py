import itertools

def generate_truth_table(expressions):
    print("Truth Table:")
    variables = sorted(set().union(*[set(exp) for exp in expressions]))
    headers = variables + expressions
    print(' | '.join(headers))
    for values in itertools.product([False, True], repeat=len(variables)):
        truth_values = dict(zip(variables, values))
        eval_results = [eval(exp, truth_values) for exp in expressions]
        row = values + tuple(eval_results)
        print(' | '.join(str(v) for v in row))
