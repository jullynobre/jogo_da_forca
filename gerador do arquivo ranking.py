import pickle

jog = []
pon = []



output = open("ranking.pkl",'wb')

pickle.dump(jog, output)
pickle.dump(pon, output)

output.close()
