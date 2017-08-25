from gensim.models import word2vec
from nltk.corpus import brown, movie_reviews, treebank
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = word2vec.Word2Vec(iter=1)  # an empty model, no training yet
model.build_vocab(brown.sents())  # can be a non-repeatable, 1-pass generator
model.train(movie_reviews.sents())  # can be a non-repeatable, 1-pass generator
model.train(treebank.sents())

model.save('model')
