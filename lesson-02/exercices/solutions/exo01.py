numbers = [0, 1, 2, 4]

# 1) Modifier la variable "numbers" pour qu'elle contienne : [0, 1, 2, 3]

numbers[3] = 3

# 2) inverser la liste "numbers" et l'afficher
# Résultat attendu : [3, 2, 1, 0]
numbers.reverse()
print(numbers)  # [3, 2, 1, 0]

# 3) ajouter les éléments 4, 5, -1 et -2 à la liste "numbers"
# Résultat attendu : [3, 2, 1, 0, 4, 5, -1, -2]

numbers.append(4)
numbers.append(5)
numbers.append(-1)
numbers.append(-2)
print(numbers)  # [3, 2, 1, 0, 4, 5, -1, -2]

# 4) trier la liste "numbers" et l'afficher

numbers.sort()
# ou
numbers = sorted(numbers)
print(numbers)  # [-2, -1, 0, 1, 2, 3, 4, 5]

# 5) trier la liste "numbers" dans le sens inverse et l'afficher

numbers.sort(reverse=True)
# ou
numbers = sorted(numbers, reverse=True)
print(numbers)  # [5, 4, 3, 2, 1, 0, -1, -2]

# 6) Supprimer les deux derniers éléments de la liste

numbers.pop()
numbers.pop()
print(numbers)  # [5, 4, 3, 2, 1, 0]

# 7) Afficher le maximum de la liste, le minimum, et la somme des chiffres

print(max(numbers))
print(min(numbers))
print(sum(numbers))