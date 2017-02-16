import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import gensim

def splitInTuplas(sentence, window):
	sentence = sentence.split()
	resultado = []
	for index, word in enumerate(sentence):
		for j in range(1,window+1):
			if(index-j >= 0):
				resultado.append([word, sentence[index-j]])
			if(index+j < len(sentence)):
				resultado.append([word, sentence[index+j]])
	return resultado

print "Leyendo archivo..."
file = open("files/file_training.txt")
sentences = file.readlines()
print "Armando tuplas..."
sentences = [splitInTuplas(i.replace(" .\n",""),5) for i in sentences]
tuplas = []
"""for i in sentences:
	tuplas = tuplas + i
"""
for sentence in sentences:
	for words in sentence:
		tuplas.append(words)
print "Entrenando modelo..."
model = gensim.models.Word2Vec(tuplas, size=300, min_count=30,workers=4)
print "Guardando modelo..."
model.save("models/word2vec.mod")
print "Fin"
#import pdb; pdb.set_trace()