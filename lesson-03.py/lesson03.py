###########################
# Lesson 03 : les fonctions
###########################

# la factorisation

# fonction simple sans paramètre

def print_hello():
    print("Hello")
    print("World")

print_hello()
print_hello()

# Un fonction possède des "paramètres" qui constituent sa "signature"
# Quand on appelle une fonction, on lui passe en paramètre des "arguments" (= valeur des variables au moment de l'appel à fonction)

def say_hello(name):
    print("Hello %s" % name)

say_hello("bastien")
say_hello("remi")

names = ["bastien", "remi", "thibz"]
for name in names:
    say_hello(name)

# valeur de retour

def add_numbers(a, b):
    result = a + b
    return result

res = add_numbers(1, 2)
res = add_numbers(10, 5)
res = add_numbers(b=5, a=3)

# Fonction et arguments positionnels

# Fonction et arguments par mots clés

# Valeur par défaut des paramètres

def say_hello(name="World"):
    print("Hello %s" % name)

say_hello("bastien")
say_hello()
