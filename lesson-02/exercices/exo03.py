numbers = list(range(10))

# 1) Faire une boucle qui affiche chaque chiffre ainsi que ce même chiffre au carré

# 2) Faire une boucle qui affiche, pour chaque chiffre, si ce chiffre est pair ou impair

# 3) Exercice plus difficle :

import random

numbers = list(range(1000))
del numbers[random.randint(0, len(numbers) - 1)]
random.shuffle(numbers)

# Etant donné la liste "numbers" modifiée ci dessus, trouver et afficher le chiffre manquant
