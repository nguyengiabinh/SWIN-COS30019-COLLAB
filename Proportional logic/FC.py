
# Forward Chaining logic for the expert system
def forward_chaining(knowledge_base, query):
    # Initialize known facts and inference counts
    known_facts = set()
    counts = {'yes': 0, 'no': 0}
    
    # Populate initial facts from the knowledge base
    for premises, conclusions in knowledge_base.items():
        if not premises:  # Facts have no premises
            known_facts.update(conclusions)

    # Track if new facts are inferred in each iteration to continue or break the loop
    new_inferences = True
    while new_inferences:
        new_inferences = False
        for premises, conclusions in knowledge_base.items():
            if premises <= known_facts and not conclusions.isdisjoint(known_facts) == False:
                # If all premises are known and the conclusion is not already known
                new_facts = conclusions - known_facts
                if new_facts:
                    known_facts.update(new_facts)
                    new_inferences = True
                    if query in new_facts:
                        counts['yes'] += 1
                        return True, counts

    if query not in known_facts:
        counts['no'] += 1
    return False, counts
