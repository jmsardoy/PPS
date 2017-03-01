import gensim
from random import randint

model = gensim.models.Word2Vec.load("models/new_model.mod")

sentences = open("files/file_training_image.txt").readlines()

data = open("files/data_vectors_image.txt","w")

def escribitBloque(frase,image,result):
	data.write(image.replace("\n",""))
	data.write("-----")
	for word in frase.split():
		try:
			data.write(model[word].tostring())
			data.write("-----")
		except:
			pass
	data.write(result)
	data.write("*****")


ultima_imagen = sentences[0].split(" . - ")[1]
contador = 0
for sentence in sentences:
	frase = sentence.split(" . - ")[0]
	image = sentence.split(" . - ")[1]
	if image==ultima_imagen:
		contador = contador+1
		escribitBloque(frase=frase,image=image,result="1")
	else:
		for i in range(contador):
			new_frase=""
			new_image = ultima_imagen
			while new_image == ultima_imagen:
				index_random = randint(0,len(sentences))
				sentence = sentences[index_random]
				new_frase = sentence.split(" . - ")[0]
				new_image = sentence.split(" . - ")[1]
			escribitBloque(frase=new_frase,image=ultima_imagen,result="0")
		contador = 1
		ultima_imagen = image
		escribitBloque(frase=frase,image=image,result="1")
for i in range(contador):
	new_frase=""
	new_image = ultima_imagen
	while new_image == ultima_imagen:
		index_random = randint(0,len(sentences))
		sentence = sentences[index_random]
		new_frase = sentence.split(" . - ")[0]
		new_image = sentence.split(" . - ")[1]
	escribitBloque(frase=new_frase,image=ultima_imagen,result="0")
