import nltk
from nltk.corpus import brown
from nltk.corpus import movie_reviews
from nltk.tokenize import RegexpTokenizer
from nltk.collocations import *

tokenizer = RegexpTokenizer(r'\w+')
num_brown_words = brown.words()
num_movie_words = movie_reviews.words()
brown_cor = '-'.join(num_brown_words)
movie_cor = '-'.join(num_movie_words)

b_words = tokenizer.tokenize(brown_cor)
m_words = tokenizer.tokenize(movie_cor)

freq_brown = nltk.FreqDist(b_words)
freq_movie = nltk.FreqDist(m_words)

total_brown_word_count = len(b_words)
total_movie_word_count = len(m_words)

b_vocab = len(freq_brown)
m_vocab = len(freq_movie)

b_prob_dist = []
m_prob_dist = []

for key,value in freq_brown.items():
	add_1_formula = (float(int(value) + 1)/(total_brown_word_count + b_vocab))
	b_prob_dist.append((str(key),add_1_formula))

for key,value in freq_movie.items():
	add_1_formula = (float(int(value) + 1)/(total_movie_word_count + m_vocab))
	m_prob_dist.append((str(key),add_1_formula))

comparison = {}
for b_key in freq_brown.keys():
	if freq_movie.has_key(b_key):
		comparison[b_key] = freq_brown[b_key] - freq_movie[b_key]

comp_list = sorted(comparison, key=lambda dict_value: abs(comparison[dict_value]))

b_bigrams = nltk.ngrams(b_words,2)
b_bigrams = nltk.FreqDist(b_bigrams)

b_bigram_prob_dist = []

for key,value in b_bigrams.items():
	w_1 = key[0]
	w_1_count = freq_brown[w_1]
	add_1_formula = ((float(int(value) + 1))/(w_1_count + b_vocab))
	b_bigram_prob_dist.append((str(key),add_1_formula))

bigram_pmi_measures = nltk.collocations.BigramAssocMeasures()
b_pmi = BigramCollocationFinder.from_words(b_words)
b_pmi.apply_freq_filter(2)
fifty_best_pmi =  b_pmi.nbest(bigram_pmi_measures.pmi,50)