import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import gensim


print "Leyendo archivo..."
file = open("files/file_training.txt")
sentences = file.readlines()
sentences = [i.replace(" .\n","").split() for i in sentences]
print "Entrenando modelo..."
model = gensim.models.Word2Vec(sentences, size=300,window=5, min_count=1,workers=4)
print "Guardando modelo..."
model.save("models/word2vec.mod")
print "Fin"
