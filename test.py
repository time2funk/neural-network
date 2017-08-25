import os
import pandas as pd
import nltk
import gensim
from gensim import corpora, models, similarities

os.chdir('text');
df=pd.read_csv('text.csv');

x=df['Question'].values.tolist()
y=df['Answer'].values.tolist()

corpus = x+y

tok_corp = [ nltk.word_tokenizer(sent.decode('utf-8')) for sent in corpus ]

model = gensim.models.Word2Vec(tok_corp, min_cout = 1, size = 32)

#model.save('testmodel')
#model.gensim.models.Word2Vec.load('testmodel')
#model.most_similar('word')
#model.most_similar([vector])
