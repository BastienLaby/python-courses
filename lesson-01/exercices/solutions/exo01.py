# Ecrire un programe qui demande à l'utilisateur:
# - son nom
# - son age
# Puis qui affiche un message le saluant, en précisant son age en années et aussi en mois et en jours.
# On considèrera qu'il y a 31 jours dans tous les mois de l'année

# cas à tester :
# "Bastien", 30 > "Enchanté Bastien, tu as 30 ans, soit 360 mois ou 11160 jours"
# "Rémi", 12 > "Enchanté Bastien, tu as 12 ans, soit 144 mois ou 4464 jours"

print("Quel est ton nom ?")
name = input()
print("Et quel est ton âge ?")
age = int(input())

months = age * 12
days = months * 31
print(f"Enchanté %s, tu as %s ans, soit %s mois ou %s jours" % (name, age, months, days))
