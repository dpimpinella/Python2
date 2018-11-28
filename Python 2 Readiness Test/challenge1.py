verb_list = ['add', 'count', 'fix', 'join', 'open', 'perform', 'produce', 'refuse', 'snow', 'wander']

def create_words(verbs):
    for verb in verbs:
        if verb[-1] == 'e':
            base = verb[:-1]
        else: 
            base = verb

        print (verb, base + 'ed', base + 'ing')

create_words(verb_list)