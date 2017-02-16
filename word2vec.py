import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import gensim

model = gensim.models.Word2Vec.load("models/word2vec.mod")
import pdb; pdb.set_trace()
similaridad = model.similarity("men", "play")
print "antes"
print similaridad
total_words = model.vocab.__len__()
print total_words
model.build_vocab(["casa"], update=True)
total_words = model.vocab.__len__()
print total_words
model.train([["play","casa"]])
model.train([["casa","play"]])
similaridad_despues = model.similarity("play","casa")
print "despues " 
print similaridad_despues
import pdb; pdb.set_trace()