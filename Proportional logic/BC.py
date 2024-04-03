import re
from File_Reader import read, extract_text

def backward_chaining(knowledge_base, query, proven=None, counts=None):
    if proven is None:
        proven = set()
    if counts is None:
        counts = {'yes': 0, 'no': 0}

    if query in proven:
        counts['yes'] += 1
        return True, counts

    if frozenset() in knowledge_base and query in knowledge_base[frozenset()]:
        proven.add(query)
        counts['yes'] += 1
        return True, counts

    for premises, conclusions in knowledge_base.items():
        if query in conclusions:
            all_proven = True
            for premise in premises:
                proven_result, counts = backward_chaining(knowledge_base, premise, proven, counts)
                if not proven_result:
                    all_proven = False
                    break
            if all_proven:
                proven.add(query)
                counts['yes'] += 1
                return True, counts

    counts['no'] += 1
    return False, counts
