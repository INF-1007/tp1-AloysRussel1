# Exercice 02 – Ambiance autour du stade (sections A a H) (gabarit)
"""
Objectif :
- Lire 8 entiers (un par ligne) : personnes dans les sections A, B, C, D, E, F, G, H (dans cet ordre)
- Valider : chaque valeur est un entier >= 0
    -> sinon afficher EXACTEMENT : "Erreur - donnees invalides."
- Calculer l'intensite brute par section : intensite = personnes * facteur
- Normaliser sur 0..10 avec un arrondi half-up :
    - maxI = max(intensites)
    - si maxI == 0 : niveaux = [0]*8
    - sinon : niveau = int((intensite / maxI) * 10 + 0.5), borne dans [0,10]
- Afficher une grille verticale :
    - lignes 10 a 1
    - colonnes A a H
    - afficher "❚" si niveau_section >= niveau_ligne sinon "."
    - un espace entre chaque cellule
    - format de ligne : "{ligne:2} | <8 cellules>"
    - derniere ligne : "     A B C D E F G H"
"""


# TODO: Lire 8 entiers (un par ligne) dans une liste personnes
#       En cas d'erreur de conversion ou valeur negative -> afficher le message d'erreur et quitter

# TODO: Calculer les intensites brutes (liste de 8 floats)

# TODO: Calculer les niveaux normalises (liste de 8 entiers dans [0,10])

# TODO: Afficher la grille (10 lignes) puis la ligne des labels

###############################################################################################################################

# print ("_____***RESOLTION EXERCICE 2***_____")
FACTEURS = [1.30, 1.15, 1.05, 0.95, 0.95, 1.05, 1.15, 1.30]
personnes = []
for section in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
    nb_personnes = int(input(f"Entrez le nombre de personnes dans la section {section} : "))
    if nb_personnes < 0:
        print("Erreur - donnees invalides.")
        exit()
    personnes.append(nb_personnes)
intensites = [personnes[i] * FACTEURS[i] for i in range(8)]

max_intensite = max(intensites)
niveaux = [int((intensites[i] / max_intensite * 10 + 0.5)) if max_intensite != 0 else 0 for i in range(8)]

for ligne in range(10, 0, -1):
    s=""
    for i in range(8):
        if niveaux[i] >= ligne:
            s += "❚ "
        else:
            s += ". "
    print(f"{ligne:2} | {s.strip()}")
print("     A B C D E F G H")

