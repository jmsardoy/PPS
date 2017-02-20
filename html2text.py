import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
import re
from num2words import num2words


def limpiarOracion(string):
	if(not string.endswith(".")):
		string += "."

	palabras = string.split()
	for i in palabras:
		if i.isdigit():
			string = string.replace(i,num2words(int(i)))
	string = string.replace('"','')
	string = string.replace(","," ,")
	string = string.replace("?", " ?")
	string = string.replace("(",", ")
	string = string.replace(")" ," ,")
	string = string.replace("!", "")
	string = string.replace(".", " .")
	string = string.replace(";", " ;")
	string = string.replace("-", " ")
	string = string.replace("'s", "")
	string = string.replace("'", "")
	string = string.replace("#", "number ")
	string = string.lower()
	m = re.search(" '[^']*' ", string)
	while(m):
		string_con_qoute = m.group(0)
		string_sin_qoute = string_con_qoute.replace(" '", " ").replace("' ", " ")
		string = string.replace(string_con_qoute,string_sin_qoute)
		m = re.search(" '[^']*' ", string)

	return string


html_file = open("files/flickr30k.html")
html_doc = html_file.read()
file_training = open("files/file_training.txt",'w')
file_training_image = open("files/file_training_image.txt",'w')
file_validate = open("files/file_validate.txt",'w')
file_validate_image = open("files/file_validate_image.txt",'w')
file_test = open("files/file_test.txt",'w')
file_test_image = open("files/file_test_image.txt",'w')
print "Leyendo archivo..."
soup = BeautifulSoup(html_doc,"html.parser")
table = soup.find("table").find_all("tr")
print "Lectura completada"
numero_foto = ""
skiplista = False
contador = -1
for i in table:
	if(i.find("ul") and not skiplista):
		for j in i.find_all("li"):
			oracion = j.getText()
			oracion = limpiarOracion(oracion)
			if(0 <= contador <=7):
				#print oracion + ":" + numero_foto+"---a"
				file_training.write(oracion+"\n")
				file_training_image.write(oracion + " - " + numero_foto+"\n")
			elif(contador == 8):
				#print oracion + ":" + numero_foto+"---b"
				file_validate.write(oracion+"\n")
				file_validate_image.write(oracion + " - " + numero_foto+"\n")
			elif(contador == 9):
				#print oracion + ":" + numero_foto+"---c"
				file_test.write(oracion+"\n")
				file_test_image.write(oracion + " - " + numero_foto+"\n")
	else:
		if(i.find("a")):
			numero_foto = i.find("a").getText()
			skiplista = False
			contador = (contador+1)%10
		else:
			skiplista = True

html_file.close()
file_training.close()
file_training_image.close()
file_validate.close()
file_validate_image.close()
file_test.close()
file_test_image.close()


