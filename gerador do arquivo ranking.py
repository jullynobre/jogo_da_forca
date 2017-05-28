import pickle

jog = ["Guedes","Jully","Shirley","Afonso","Joãozinho"]
pon = [3100,3000,2600,2000,1500]



output = open("ranking.pkl",'wb')

pickle.dump(jog, output)
pickle.dump(pon, output)

output.close()
