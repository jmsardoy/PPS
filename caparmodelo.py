import gensim

sentences = open("files/file_validate.txt").readlines()
sentences = [i.replace(" .\n","").split() for i in sentences]
model_validate = gensim.models.Word2Vec(sentences,min_count=1)
sentences = open("files/file_test.txt").readlines()
sentences = [i.replace(" .\n","").split() for i in sentences]
model_test = gensim.models.Word2Vec(sentences,min_count=1)
model = gensim.models.Word2Vec.load("models/word2vec.mod")
model_wiki = gensim.models.Word2Vec.load_word2vec_format("models/wiki_model.bin",binary=True)

palabras_nuestras_train = model.vocab.viewkeys()
palabras_nuestras_validate = model_validate.vocab.viewkeys()
palabras_nuestras_test = model_validate.vocab.viewkeys()
palabras_wiki = model_wiki.vocab.viewkeys()

palabras_nuestras = []
for i in palabras_nuestras_train:
	if i not in palabras_nuestras:
		palabras_nuestras.append(i)
for i in palabras_nuestras_validate:
	if i not in palabras_nuestras:
		palabras_nuestras.append(i)
for i in palabras_nuestras_test:
	if i not in palabras_nuestras:
		palabras_nuestras.append(i)

estan = []
no_estan = []
for i in palabras_nuestras:
	if i in palabras_wiki:
		estan.append(i)	
	else:
		no_estan.append(i)

print "NO ESTAN", no_estan
print len(no_estan)
new_model = []
model_text = open("models/wiki_model.txt").readlines()
cantidad_de_neuronas = model_text[0].split()[1]
print "cantidad de neuronas", cantidad_de_neuronas
cantidad_estan = 0

model_text = model_text[1:]
model_text_words = [i.split()[0] for i in model_text]

for index, word in enumerate(model_text_words):
	if(word in estan):
		cantidad_estan = cantidad_estan + 1
		new_model.append(model_text[index])


#import pdb; pdb.set_trace()
new_model_text = open("models/new_model.txt",'w')
new_model_text.write(str(cantidad_estan)+ " " + cantidad_de_neuronas + "\n")
for i in new_model:
	new_model_text.write(i)
new_model_text.close()



