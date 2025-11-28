import csv, json

def ListarSkins():

    data = []

    with open("skinsDatabase.csv", encoding="utf-8") as r:
            arquivo = csv.DictReader(r)
            for l in arquivo:
                  data.append(l)
            
    return data
            