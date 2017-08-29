from gensim.models import Word2Vec

model = Word2Vec.load('model')
vec = model.most_similar('man', topn=1)
for v in vec:
	print(v[0])
#model.save('testmodel')
#model.gensim.models.Word2Vec.load('testmodel')
#model.most_similar('word')
#model.most_similar([vector])
