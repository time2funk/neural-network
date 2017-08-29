# import gensim, nltk 
import logging
import os
from gensim.models import Word2Vec
from nltk.corpus import brown, movie_reviews, treebank

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.basicConfig(filename='w2v.log',level=logging.DEBUG)
logging.debug('start')
# logging.debug( type(brown.sents()) )
# logging.info()
class MySentences(object):
	def __init__(self, dirname):
		self.dirname = dirname

	def __iter__(self):
		for fname in os.listdir(self.dirname):
			for line in open(os.path.join(self.dirname, fname)):
				yield line.decode('utf-8').split()

sentences = MySentences('text') # a memory-friendly iterator

model = Word2Vec(sentences, min_count=1)
model.most_similar('text')
model.save('model')

# b = Word2Vec(brown.sents())
# mr = Word2Vec(movie_reviews.sents())
# t = Word2Vec(treebank.sents()

# sentences = word2vec.Text8Corpus('text8')
# sentences = [['first', 'Someone has updated genisms'], ['second', 'So the question is: How to update the model so that it gives out all the possible similarities for the given new sentence?']]
# model = Word2Vec(sentences, size=200)


