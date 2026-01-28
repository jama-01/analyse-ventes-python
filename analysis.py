import os

base_dir = os.path.dirname(__file__)

csv_path = os.path.join(base_dir, "data", "ventes.csv")

donnees = []

with open(csv_path, "r", encoding="utf-8") as file:
    next(file)
    for line in file:
        colonnes = line.strip().split(",")
        if len(colonnes) == 4:
            colonnes[3] = float(colonnes[3])
            donnees.append(colonnes)

total_ca = 0
nb_commande = 0

for line in donnees:
    montant = line[3]
    total_ca = total_ca + montant
    nb_commande += 1

panier_moyen = total_ca / nb_commande

ventes_par_pays = {}

for line in donnees:
    pays = line[2]
    montant = line[3]
    if pays not in ventes_par_pays:
        ventes_par_pays[pays] = {
            "commandes": 0,
            "total": 0
        }

    ventes_par_pays[pays]["commandes"] += 1
    ventes_par_pays[pays]["total"] += montant

ventes_par_client = {}

for line in donnees:
    client = line[1]
    montant = float(line[3])
    if client not in ventes_par_client:
        ventes_par_client[client] = {
            "total": 0
        }
    ventes_par_client[client]["total"] += montant

max_client = None
max_total = 0

for client, i in ventes_par_client.items():
    if i["total"] > max_total:
        max_total = i["total"]
        max_client = client

print("\n============================== \nRAPPORT D'ANALYSE DES VENTES \n==============================")

print(
    f"\nChiffre d'affaires total : {total_ca} €\nNombre de commande : {nb_commande} \nPanier moyen : {panier_moyen} €")

print("\nVentes par pays :")
for pays, infos in ventes_par_pays.items():
    print(f"- {pays} : {infos['commandes']} commandes - {infos['total']} €")

print("\nVentes par client :")
for client, i in ventes_par_client.items():
    print(f"- {client} : {i['total']} total - €")

print(
    f"\nClient ayant le plus dépensé : \n -Nom : {max_client}\n- Total : {max_total} €")
