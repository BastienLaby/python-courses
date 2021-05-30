# Ecrire un programe qui demande à l'utilisateur:
# - un premier chiffre
# - un deuxieme chiffre
# - une opération à effectuer dans la liste : add, sub, mult, div ou div-entiere
# Afficher le résultat de l'opération entre les deux chiffres
# Le programme doit gérer le cas où l'opération spécifiée par l'utilisateur n'est pas connue en affichant "Cette opération n'est pas reconnue"
# Le programme doit gérer le cas où l'utilisateur veut diviser par zéro en affichant "Impossible de diviser par zéro"

# cas à tester :
# 1, 2, "add" > 3
# 1, 2, "sub" > -1
# 2, 3, "mult" > 6
# 3, 2, "div" > 1.5
# 3, 2, "div-entiere" > 1
# 3, 0, "div" > "Impossible de diviser par zéro"
# 3, 2, "toto" > "Cette opération n'est pas reconnue"
# 1, 0.5, "add" > 1.5