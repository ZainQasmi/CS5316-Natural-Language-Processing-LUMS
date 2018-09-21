########################################### NLTK #######################################

txt = """Atlas Honda is expected to achieve sales of 1.1 million units by end of its 
financial year ending March 31, while it aims to hit sales of 1.3m bikes in its next 
financial year, a Honda dealer said."""

import spacy
nlp = spacy.load('en')
doc = nlp(txt.decode('utf8'))
print doc.ents

from nltk.tree import Tree
from nltk import ne_chunk, pos_tag, word_tokenize


def id_entities(myStr):
    lump1 = word_tokenize(myStr)
    lump2 = pos_tag(lump1)
    lump3 = ne_chunk(lump2)
    block = []
    currBlock = []
    for one in lump3:
        if type(one) == Tree:
            currBlock.append(" ".join([token for token, pos in one.leaves()]))
        elif currBlock:
            entity = " ".join(currBlock)
            if entity not in block:
                block.append(entity)
                currBlock = []
        else:
            continue
    if block:
        entity = " ".join(currBlock)
        if entity not in block:
            block.append(entity)
    return block

print id_entities(txt)

####################################### SpaCy ##########################################

