# It has sentences from three domains: i) imdb ii) amazon iii) yelp 
# Apply preprocessing e.g., removing stop words, lemmatization, stemming. State overall vocabulary size before and after preprocessing. 
# Split data set into training, validation and testing in order to complete modeling. Present your results using confusion matrix and F1 score. 
# Use naive Bayes and Logistic Regression learning algorithm for this task.  Use the multinomial model for document representation. 

import nltk
import re
import csv
from nltk.stem.wordnet import WordNetLemmatizer

## PRE-PROCESSING

lmtzr = WordNetLemmatizer()
stopwords = nltk.corpus.stopwords.words('english')

filename1 = 'sentiment_labelled_sentences/imdb_labelled.txt'
filename2 = 'sentiment_labelled_sentences/amazon_cells_labelled.txt'
filename3 = 'sentiment_labelled_sentences/yelp_labelled.txt'

netWords = []
myDict = []
stringList = []

# replace filename1 with filename2, filename3 etc

with open(filename1, 'r') as f:
    content = f.readlines()
content = [x.strip() for x in content]

for line in content:
	lineDecoded = line.decode("utf8")
	tup = re.split(r'\t+', lineDecoded)
	tup[0] = tup[0].lower()
	stringList.append(tup)
	myWordsTokenized = nltk.word_tokenize(tup[0])
	resultwords  = [word for word in myWordsTokenized if word.lower() not in stopwords]
	# print resultwords
	for oneWord in resultwords:
		lemmatized = lmtzr.lemmatize(oneWord)
		netWords.append(lemmatized)
	for item in netWords:
	    if item not in myDict:
	        myDict.append(item)

print 'Vocab Before : ', len(netWords)
print 'Vocab After : ', len(myDict)


## ENTER NAIVE BAYES CLASSIFIER

from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier

newsTrainer = Trainer(tokenizer)

# You need to train the system passing each text one by one to the trainer module.
newsSet =[
    {'text': 'Love', 'category': 'positive'},
    {'text': 'Hate', 'category': 'negative'}
]

countPos = 0
countNeg = 0
for string,klass in stringList:
	if klass == '1':
		countPos += 1
		newsSet.append({'text': string, 'category': 'positive'})
	if klass == '0':
		countNeg += 1
		newsSet.append({'text': string, 'category': 'negative'})

# Train Model
for news in newsSet:
    newsTrainer.train(news['text'], news['category'])

# Classify Known Data
newsClassifier = Classifier(newsTrainer.data, tokenizer)

# Classify Unknown Data
str1 = "amazing good stuff"
classification = newsClassifier.classify(str1)
print(str1, classification)

str2 = "hate this shit"
classification = newsClassifier.classify(str2)
print(str2,classification)
