import nltk
from nltk.corpus import treebank
from nltk.tag import *

data = treebank.tagged_sents()

print "*************************"

traine = hmm.HiddenMarkovModelTrainer()
loT = traine.train_supervised(data)
print loT.tag("The Cambridge Analytica scandal is more than a breach as Facebook executives have defined it It exemplifies the possibility of using online data to algorithmically predict and influence human behavior in a manner that circumvents users awareness of such influence Using an intermediary app Cambridge Analytica was able to havest large data volumes over 50 million raw profiles and use big data analytics to create psychographic profiles in order to subsequently target users with customized digital ads and other manipulative information According to some observers this massive data analytics tactic might have been used to purposively swing election campaigns around the world The reports are still incomplete and more is likely to come to light in the next days.".split())


