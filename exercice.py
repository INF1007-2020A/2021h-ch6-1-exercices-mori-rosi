#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy

#1
def order(values: list = None) -> list:
    if values is None:
         # TODO: demander les valeurs ici
        values = []
        while len(values) < 3:
             values.append(input("Entrez une valeur:\n"))
        values = values.sort()

    return values


    #     valeurs = input("Entrez 10 valeurs:\n")
    #     print(valeurs)
    #
    #     liste = valeurs.split()
    #     liste_modifiee = liste.sort()
    #
    # return liste_modifiee

# #2
# def anagrams(words: list = None) -> bool:
#     if words is None:
#         # TODO: demander les mots ici
#         mot_1 = list(input("Entrez un mot:\n"))
#         print(mot_1)
#         mot_2 = list(input("Entrez un autre mot:\n"))
#         print(mot_2)
#
#         mot_1.sort()
#         mot_2.sort()
#
#         if not mot_1 == mot_2:
#             return False




        # list_mots = [mot_1, mot_2]
        # for letter in mot_1:
        #     liste_mot1.append()
        #     print(liste_mot1.reverse())
        #
        # from collections import deque
        #
        # mot_1_mod = deque(mot_1)
        # for i in range(len(mot_1_mod)):
        #     print(mot_1_mod.append(mot_1_mod.popleft()))




# #3
# def contains_doubles(items: list) -> bool:
#
#     set = {}
#     for elem in list:
#         set = set.add()
#
#     if set == list:
#         return False

# #4**
# def best_grades(student_grades: dict) -> dict:
#     # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
#     for nom, note in student_grades.items():
#         moy = {nom, numpy.mean(note)}
#     moyenne_pre = numpy.mean()
#     for nom, moyenne in moy.items():
#         if moyenne < moyenne_pre:
#             moyenne_pre=moyenne
#             continue
#     meilleure_note = {nom: moyenne}
#
#     return meilleure_note
#
# #5
# def frequence(sentence: str) -> dict:
#     # TODO: Afficher les lettres les plus fréquentes
#     #       Retourner le tableau de lettres
#
#     return {}
#
# #6
# def get_recipes():
#     # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
#     pass
#
# #6?
# def print_recipe(ingredients) -> None:
#     # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
#     pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    # print(f"On vérifie les anagrammes...")
    # anagrams()
    #
    # my_list = [3, 3, 5, 6, 1, 1]
    # print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    # grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    # best_student = best_grades(grades)
    # print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")
    #
    # sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    # frequence(sentence)
    #
    # print("On enregistre les recettes...")
    # recipes = get_recipes()
    #
    # print("On affiche une recette au choix...")
    # print_recipe(recipes)


if __name__ == '__main__':
    main()
