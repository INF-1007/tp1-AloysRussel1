# -*- coding: utf-8 -*-
# Exercice 05 - Planification d'achat de billets (gabarit)
"""
Objectif :
- DEMANDER : n (int) et statut etudiant (O/N)
- Options :
    24 billets : 66.00$
    12 billets : 36.00$
     5 billets : 15.75$
     1 billet  :  3.60$
- Reduction : si etudiant = O, appliquer 12% de reduction sur le cout des forfaits uniquement.
  Les billets unitaires ne sont pas reduits.

But :
- Acheter au moins n billets
- Minimiser le prix total
- En cas d'egalite sur le prix : choisir le plus petit total de billets, puis le plus petit nombre de billets unitaires

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Sinon, afficher EXACTEMENT 6 lignes :
    Forfaits de 24 billets - A
    Forfaits de 12 billets - B
    Forfaits de 5 billets - C
    Billets unitaires - D
    Total billets - T
    Prix total - PPP.PP$

Prompts EXACTS :
1) "Entrez le nombre de billets necessaires : "
2) "Entrez le statut etudiant (O/N) : "

Conseil :
- Une solution simple consiste a tester plusieurs combinaisons de forfaits avec des boucles (bruteforce).
"""

# TODO: Lire n (int) et statut (str)

# TODO: Validation (n >= 0 et statut dans {O, N})

# TODO: Chercher la meilleure combinaison (A, B, C, D)

# TODO: Calculer et afficher le resultat exact (6 lignes)

# print ("_____***RESOLTION EXERCICE 5***_____")
n = int(input("Entrez le nombre de billets necessaires : ")) 
statut = input("Entrez le statut etudiant (O/N) : ")
if n < 0 or statut not in {'O', 'N'}:
    print("Erreur - donnees invalides.")
else:
    prix_forfait_24 = 66.00
    prix_forfait_12 = 36.00
    prix_forfait_5 = 15.75
    prix_billet_unitaire = 3.60

    if statut == 'O':
        prix_forfait_24 *= 0.88
        prix_forfait_12 *= 0.88
        prix_forfait_5 *= 0.88
    meilleur_prix = float('inf')
    meilleure_combinaison = (0, 0, 0, 0)
    for A in range((n // 24) + 2):
        for B in range((n // 12) + 2):
            for C in range((n // 5) + 2):
                D = max(0, n - (A * 24 + B * 12 + C * 5))
                total_billets = A * 24 + B * 12 + C * 5 + D
                prix_total = (A * prix_forfait_24 +
                              B * prix_forfait_12 +
                              C * prix_forfait_5 +
                              D * prix_billet_unitaire)
                if (prix_total < meilleur_prix or
                    (prix_total == meilleur_prix and total_billets < sum(meilleure_combinaison[i] * [24, 12, 5, 1][i] for i in range(4))) or
                    (prix_total == meilleur_prix and total_billets == sum(meilleure_combinaison[i] * [24, 12, 5, 1][i] for i in range(4)) and D < meilleure_combinaison[3])):
                    meilleur_prix = prix_total
                    meilleure_combinaison = (A, B, C, D)
   
    A, B, C, D = meilleure_combinaison
    print(f"Forfaits de 24 billets - {A}")
    print(f"Forfaits de 12 billets - {B}")
    print(f"Forfaits de 5 billets - {C}")
    print(f"Billets unitaires - {D}")
    print(f"Total billets - {A * 24 + B * 12 + C * 5 + D}")
    print(f"Prix total - {meilleur_prix:.2f}$")