import logging
import os
from gensim.models import Word2Vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.debug('start')
# logging.debug()
# logging.info()
class MySentences(object):
	def __init__(self, dirname):
		self.dirname = dirname

	def __iter__(self):
		for fname in os.listdir(self.dirname):
			print ("- > File name: "+os.path.join(self.dirname, fname))
			for line in open(os.path.join(self.dirname, fname)):
				yield line.split()

sentences = MySentences('text')
lens = 0
for i, sent in enumerate(sentences):
	lens += len(sent)

model = Word2Vec.load('model')
model.train(sentences,total_examples=lens, epochs=model.iter)

print(" < -o- > vocab length:")
print(len(model.wv.vocab))

model.save('model')



