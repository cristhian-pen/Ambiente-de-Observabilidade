import csv, os

def CadastrarNovaSkin(nome, modelo, statrack, souvenir):
    if not os.path.exists("skinsDatabase.csv"):
        with open("skinsDatabase.csv", "a", newline='', encoding='utf-8') as arquivo:
            gravador = csv.writer(arquivo)
            gravador.writerow(["nome", "modelo", "statrack", "souvenir"])
    
    with open("skinsDatabase.csv", "a", newline='', encoding='utf-8') as arquivo:
            gravador = csv.writer(arquivo)
            gravador.writerow([nome, modelo, statrack, souvenir])
        