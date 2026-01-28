# -*- coding: utf-8 -*-
# Exercice 03 - Choisir le meilleur trajet vers le CEPSUM (gabarit)
"""
Objectif :
- DEMANDER : distance (km, float), attente_navette (min, float), temps_metro (min, float), controle (min, float)
- Valider : toutes les valeurs >= 0
- Calculer les temps bruts (minutes) :
    marche  = distance * 60 / 5 + controle
    navette = attente_navette + distance * 60 / 18 + controle
    metro   = temps_metro + controle
- Arrondir chaque temps a la minute superieure (ceil)
- Determiner la/les option(s) minimale(s)

Sortie :
- 1 option gagnante : "Option la plus rapide : marcher." ou "navette." ou "metro."
- 2 options ex-aequo (ordre : marcher, navette, metro) : "Egalite : X et Y."
- 3 options ex-aequo : "Egalite : marcher, navette et metro."

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS :
1) "Entrez la distance jusqu'au CEPSUM (en kilometres) : "
2) "Entrez le temps d'attente de la navette (en minutes) : "
3) "Entrez le temps du trajet en metro (en minutes) : "
4) "Entrez le temps de controle a l'entree (en minutes) : "
"""

# TODO: Importer math

# TODO: Lire les 4 valeurs

# TODO: Validation

# TODO: Calculer, arrondir (ceil) et determiner le(s) meilleur(s)

# TODO: Afficher la phrase exacte


#############################################################################################################

print ("_____***RESOLTION EXERCICE 3***_____")
import math
distance = float(input("Entrez la distance jusqu'au CEPSUM (en kilometres) : "))
attente_navette = float(input("Entrez le temps d'attente de la navette (en minutes) : "))
temps_metro = float(input("Entrez le temps du trajet en metro (en minutes) : "))
controle = float(input("Entrez le temps de controle a l'entree (en minutes) : "))
if distance < 0 or attente_navette < 0 or temps_metro < 0 or controle < 0:
    print("Erreur - donnees invalides.")
else:
    temps_marche = math.ceil(distance * 60 / 5 + controle)
    temps_navette = math.ceil(attente_navette + distance * 60 / 18 + controle)
    temps_metro_total = math.ceil(temps_metro + controle)
    temps_options = {
        "marcher": temps_marche,
        "navette": temps_navette,
        "metro": temps_metro_total
    }
    print(temps_options)
    temps_minimal = min(temps_options.values())
    meilleures_options = []
    for option, temps in temps_options.items():
        if temps == temps_minimal:
            meilleures_options.append(option)

    if len(meilleures_options) == 1:
        print(f"Option la plus rapide : {meilleures_options[0]}.")
    elif len(meilleures_options) == 2:
        print(f"Egalite : {meilleures_options[0]} et {meilleures_options[1]}.")
    else:
        print("Egalite : marcher, navette et metro.")