import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import gensim

model = gensim.models.Word2Vec.load("models/word2vec.mod")
import pdb; pdb.set_trace()