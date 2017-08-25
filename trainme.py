import logging
import os
from gensim.models import Word2Vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# logging.basicConfig(filename='w2v.log',level=logging.DEBUG)
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

sentences = MySentences('text')

model = Word2Vec.load('model')
model.train(sentences)
model.save('model')



