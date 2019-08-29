import random
import pdb

grammar = {
    '_S' : [ '_NP _VP' ], # _S -> Sentence Rule
    '_NP': ['_N', '_A _NP _P _A _N'], # _NP -> Noun Phrase
    '_VP': ['_V', '_V _NP'], # _VP -> Verb Phrase
    '_N' : ['data science', 'Python', 'regression'],
    '_A' : ['big', 'linear', 'logistic'],
    '_P' : ['about', 'near'],
    '_V' : ['learns', 'trains', 'tests', 'is'],
}

def is_terminal(item):
    return item[0] != '_'

def expand(grammar, tokens):
    tokens_copy = tokens.copy()
    
    while True:
        tokens_modified = False

        for token_index, token in enumerate(tokens_copy):
            if not is_terminal(token):
                expanded_token = random.choice(grammar[token]).split(' ')
                tokens_copy = tokens_copy[0 : token_index] + expanded_token + tokens_copy[token_index + 1:]
                tokens_modified = True
                break

        if not tokens_modified: break
    
    return tokens_copy

print(expand(grammar, ['_S']))