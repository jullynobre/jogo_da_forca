import pickle

palavras1 = ["predio","caderno","lapis","corrida","cubo"]
palavras2 = ["computador","lamparina","gasolina","concreto","desmatamento"]
palavras3 = ["contrapartida","condizente","sintetizar","inerente","paradigma"]

output = open("palavras.pkl", "wb")

pickle.dump(palavras1, output)
pickle.dump(palavras2, output)
pickle.dump(palavras3, output)

output.close()

