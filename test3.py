from gensim.models import Word2Vec

model = Word2Vec.load('model')
model.most_similar('text')


#model.save('testmodel')
#model.gensim.models.Word2Vec.load('testmodel')
#model.most_similar('word')
#model.most_similar([vector])
