######################
# Les trucs de base
######################

# afficher un message à l'écran

print("Hello World")

# Créer une variable et lui assigner une valeur

name = "Bastien"
age = 12

# demander un input à l'utilisateur

name = input("Quel est ton nom ? ")

######################
# Les types de données
######################

# les types de données de base en python

number = 1  # int (Entier Naturel)
floating = 1.5  # float (Entier Flotant)
phrase = "salut les nobbs du python"  # str (chaine de charactères)
c = "s"  # str (une chaine de charactères de 1 seul élément est aussi une chaine de charactères)
c = ""  # une chaine de charactères vides est quand même une chaine de charactères
is_noob = True  # bool (un booléen représentant une valeur Vraie ou Fausse)
is_not_noob = False

# On peut transformer un type en un autre type en appelant la fonction du type souhaité.
# On appelle cette opération : "caster". Exemple : caster un int en str

my_int = 12
my_str = str(my_int)
my_int = int(my_str)  # operation inverse

# On ne peut pas caster n'importe quel type vers n'importe quel type

my_int = str("douze")  # va lever une erreur

# On peut afficher le type d'une variable

print(type("Bastien"))  # va afficher "<class 'str'>
print(type(12))  # va afficher "<class 'int'>

######################
# Conditions
######################

# Un bloc de condition permet d'executer une série d'instructions à condition qu'une condition soit vraie
# La sytaxe globale est :

condition = True

if condition:
    print("La condition est vraie")
    ... faire d'autres trucs
else:
    print("La condition est fausse")
    
# on peut intercaler un "elif" pour tester plusieurs conditions à la suite
    
if name == "bastien":
    print("Salut bastien")
elif name == "remi":
    print("Salut remi")
else:
    print("Tu n'es ni Bastien ni Rémi !")
    
###########################
# Opérateurs de comparaison
###########################

# Les opérateurs de comparaison renvoient True ou False en fonction de la valeur des termes de ces opérateurs

price = 5

if price > 10:
    print("C'est trop cher !")

if price <= 2:
    print("C'est vraiment une bonne affaire !")

# Liste des opérateurs logiques :

# == permet de tester si les deux valeurs sont égales
print(1 + 2 == 3)  # True
print(1 + 2 == 4)  # False

# >, <, >= et <= permettent de tester si les valeurs sont plus grands, moins grands, plus grands ou égaux, etc.
price = 5
print(price > 3)  # True
print(price < 3)  # False
print(price >= 5)  # True
print(price <= 6)  # False

# != permet de tester si deux valeurs sont différents
price = 5
print(price != 5)  # True
print(price != 4)  # False

# On peut chainer les opérateurs avec "and" et "or" (qu'on appelle des "opérateurs logiques")

price = 5

if price >= 3 and price <= 7:
    print("C'est dans ma tranche de prix !")
    
if price == 3 or price == 7:
    print("C'est pile à la limite de ma tranche de prix !")

# Les opérateurs sont évalués dans l'ordre des parenthèses, puis de gauche à droite :

print(True and False and True)  # False
print(True or False and True)  # True

# Plus d'infos : https://www.w3schools.com/python/python_operators.asp
