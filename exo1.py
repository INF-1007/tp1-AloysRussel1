# -*- coding: utf-8 -*-
# Exercice 01 - Bilan de visionnage Carabins (gabarit)
"""
Objectif :
- DEMANDER : nom complet, matchs football, duree football, matchs soccer, duree soccer
- Valider : matchs >= 0 et durees > 0 (entiers)
- Convertir les minutes en format HhMM (minutes sur 2 chiffres)
- Afficher EXACTEMENT 4 lignes :
    Bonjour {nom}
    Football (Carabins): {A} match(s), {Hf}h{Mf:02d} de visionnage
    Soccer (Carabins): {B} match(s), {Hs}h{Ms:02d} de visionnage
    Total: {Ht}h{Mt:02d}

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS a utiliser :
1) "Entrez votre nom complet : "
2) "Entrez le nombre de matchs de football des Carabins suivis cet automne : "
3) "Entrez la duree moyenne d'un match de football suivi (en minutes) : "
4) "Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "
5) "Entrez la duree moyenne d'un match de soccer suivi (en minutes) : "
"""

# TODO: Lire le nom (str)

# TODO: Lire les 4 valeurs (int)

# TODO: Valider les donnees (matchs >= 0, durees > 0)

# TODO: Calculer les minutes totales (football, soccer, total)

# TODO: Convertir en heures/minutes et afficher exactement 4 lignes

##############################################################################################################################

print ("_____***RESOLTION EXERCICE 1***_____")
nom = input("Entrez votre nom complet : ")
nb_matchs_foot = int(input("Entrez le nombre de matchs de football des Carabins suivis cet automne : "))
duree_match_foot = int(input("Entrez la duree moyenne d'un match de football suivi (en minutes) : "))
nb_matchs_soccer = int(input("Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "))
duree_match_soccer = int(input("Entrez la duree moyenne d'un match de soccer suivi (en minutes) : "))
if nb_matchs_foot < 0 or duree_match_foot <= 0 or nb_matchs_soccer < 0 or duree_match_soccer <= 0:
    print("Erreur - donnees invalides.")
else:
    total_minutes_foot = nb_matchs_foot * duree_match_foot
    total_minutes_soccer = nb_matchs_soccer * duree_match_soccer
    total_minutes = total_minutes_foot + total_minutes_soccer

    heures_foot = total_minutes_foot // 60
    minutes_foot = total_minutes_foot % 60

    heures_soccer = total_minutes_soccer // 60
    minutes_soccer = total_minutes_soccer % 60

    heures_total = total_minutes // 60
    minutes_total = total_minutes % 60

    print(f"Bonjour {nom}")
    print(f"Football (Carabins): {nb_matchs_foot} match(s), {heures_foot}h{minutes_foot:02d} de visionnage")
    print(f"Soccer (Carabins): {nb_matchs_soccer} match(s), {heures_soccer}h{minutes_soccer:02d} de visionnage")
    print(f"Total: {heures_total}h{minutes_total:02d}")
