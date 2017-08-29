from __future__ import division
from gensim.models import word2vec
from nltk.corpus import brown, treebank
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

tb_lens = 0
for i, sent in enumerate(treebank.sents()):
	tb_lens += len(sent)

model = word2vec.Word2Vec(iter=1, size=300, window=10, min_count=1, sg=0)
model.build_vocab(brown.sents())
model.train(treebank.sents(), total_examples=tb_lens, epochs=model.iter)

print(" < -o- > vocab length:")
print(len(model.wv.vocab))

model.save('model')
