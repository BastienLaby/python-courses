## Les listes

# structure d'une liste

my_list = [1, 2, 3]
print(my_list)

# accès aux éléments d'une liste

# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[-1])
# print(my_list[-2])
# print(my_list[-3])
# print(my_list[-4])  # out of range

# modification d'un élément d'une liste

my_list[0] = "abc"
print(my_list)

# ajout d'éléments dans une liste (append, insert)

my_list.append('b')
print(my_list)

my_list.insert(10, 'b')
print(my_list)

# suppression d'éléments dans une liste

my_list.pop()
my_list.pop()
print(my_list)

del my_list[0]
print(my_list)

my_list.append(3)
print(my_list)

my_list.remove(3)
print(my_list)

# additionner deux liste

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

# trier une liste

my_list = [7, 4, 5, 3, 9]
my_list.sort()
print(my_list)

my_list = ["e", "c", "d"]
my_list.sort()
print(my_list)

my_list = [7, 4, 5, 3, 9]
my_list_sorted = sorted(my_list)

# inverser une liste

my_list.reverse()
# my_list = reversed(my_list)

# min, max, sum

print(min(my_list))
print(max(my_list))
print(sum(my_list))

# savoir si un element est dans une liste

numbers = [1, 2, 3, 4]
is4inList = 4 in numbers

## La boucle for

# syntaxe de la boucle for

for num in [1, 2, 3, 4]:
    print(num)

# le mot clé "break"

names = ["bastien", "remi", "thibz", "kano", "toto"]

n = ""
for name in names:
    if name == "remi":
        n = name
        print(name)
        break

print(n)

# /!\ une variable déclarée dans une boucle for, ou dans un bloc if ne doit jamais être utilisée en dehors de ces blocs (au risque de ne pas exister)
