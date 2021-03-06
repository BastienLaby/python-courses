numbers = list(range(10))

# 1) Faire une boucle qui affiche chaque chiffre ainsi que ce même chiffre au carré

for num in numbers:
    print("%s power of 2 = %s" % (num, num ** 2))

# 1) Faire une boucle qui affiche, pour chaque chiffre, si ce chiffre est pair ou impair

for num in numbers:
    if num % 2 == 0:
        print("%s is even" % num)
    else:
        print("%s is odd" % num)

# Exercice plus difficle :

import random

numbers = list(range(1000))
del numbers[random.randint(0, len(numbers) - 1)]
random.shuffle(numbers)

# Etant donné la liste "numbers" modifiée ci dessus, trouver et afficher le chiffre manquant

numbers.sort()
i = 0
for num in numbers:
    if num == i:
        i += 1
    else:
        print("%s is missing" % i)
        break

# solution utilisant des "sets"
# Un Set est une structure de données similaire à la liste mais où un même élément ne peut être présent qu'une seule fois

numbers = set(numbers)
expectedNumbers = set(range(1000))
print(expectedNumbers.difference(numbers))