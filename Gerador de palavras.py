import pickle

palavras1 = ["predio","caderno","lapis","corrida","cubo"]
dicas1 = ["residencia","folhas","riscar","rápido","seis"]
palavras2 = ["computador","lamparina","gasolina","concreto","desmatamento"]
dicas2 = ["calculos","luz","explosão","duro","floresta"]
palavras3 = ["contrapartida","condizente","sintetizar","inerente","paradigma"]
dicas3 = ["contra","coerente","resumir","ligado","exemplo"]

output = open("palavras.pkl", "wb")

pickle.dump(palavras1, output, pickle.HIGHEST_PROTOCOL)
pickle.dump(palavras2, output, pickle.HIGHEST_PROTOCOL)
pickle.dump(palavras3, output, pickle.HIGHEST_PROTOCOL)
pickle.dump(dicas1, output, pickle.HIGHEST_PROTOCOL)
pickle.dump(dicas2, output, pickle.HIGHEST_PROTOCOL)
pickle.dump(dicas3, output, pickle.HIGHEST_PROTOCOL)

output.close()
