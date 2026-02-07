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

total_ca = sum(line[3] for line in donnees)
nb_commande = len(donnees)
panier_moyen = total_ca / nb_commande

ventes_par_pays = {
    pays: {
        "commandes": sum(1 for line in donnees if line[2] == pays),
        "total": sum(line[3] for line in donnees if line[2] == pays)
    }
    for pays in set(line[2] for line in donnees)
}

ventes_par_client = {
    client: {
        "total": sum(line[3] for line in donnees if line[1] == client)
    }
    for client in set(line[1] for line in donnees)
}
max_client, max_total = max(ventes_par_client.items(), key=lambda item: item[1]["total"])

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
