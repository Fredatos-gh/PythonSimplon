import plotly.express as px
import pandas as pd

# Vu la PR pour travailler en local, mais vu aussi que ça juste marche online :p)
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Exercice 6
# Volume des ventes
volumeVente = données.groupby("produit")[["qte"]].agg(["mean", "median", "std", "var"])

# Résultat : mean -> moyenne, median -> médiane, std -> écart type, var -> variance
print("Volumes des ventes")
print(volumeVente)

# Chiffre Affaire
données["Chiffre_Affaires"] = données["prix"] * données["qte"]
ChiffreAffaire = données.groupby("produit")[["Chiffre_Affaires"]].agg(["mean", "median", "std", "var"])

print("")
print("Chiffres d'affaires")
print(ChiffreAffaire)

# Exercice 7
ventesProduit = {}

# Cumul par produit
for _, ligne in données.iterrows():
    produit = ligne["produit"]
    quantite = ligne["qte"]

    if produit in ventesProduit:
        ventesProduit[produit] += quantite
    else:
        ventesProduit[produit] = quantite

# Recherche min et max
produitMin = None
quantiteMin = None

produitMax = None
quantiteMax = None

for produit, quantite in ventesProduit.items():

    # Mini
    if quantiteMin is None or quantite < quantiteMin:
        produitMin = produit
        quantiteMin = quantite

    # Maxi
    if quantiteMax is None or quantite > quantiteMax:
        produitMax = produit
        quantiteMax = quantite


print ("")
print ("Python natif")
print("Mini -> ", produitMin, " : ", quantiteMin)
print("Maxi -> ", produitMax, " : ", quantiteMax)

# Exercice 8 
# 8.a : Les ventes par produit (par Barre c'est plus sympa)
barreVentesParProduit = px.bar(données, x='produit', y='qte',  title="ventes par produit")
barreVentesParProduit.write_html('vente-par-produit.html')

print('vente-par-produit.html généré avec succès !')

# 8.b : Chiffres d'affaires par produit : Camembert
camembertCAParProduit = px.pie(données, values='Chiffre_Affaires', names='produit', title="chiffre d'affaires par produit")
# libellé produit pour lisibilité
camembertCAParProduit.update_traces(
    texttemplate="%{label}<br>%{percent:.0%}",
    textposition="inside"
)
camembertCAParProduit.write_html('ca-par-produit.html')

print('ca-par-produit.html généré avec succès !')


# figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')
# figure.write_html('ventes-par-region.html')

# print('ventes-par-région.html généré avec succès !')
