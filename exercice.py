#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy

#1
def order(values: list = None) -> list:
    if values is None:
         # TODO: demander les valeurs ici
        values = []
        while len(values) < 10:
             values.append(input("Entrez une valeur:\n"))
        values = values.sort()

    return values #test failed, retourne None, ne retourne pas de liste ordonnée




#2
def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        mot_1 = list(input("Entrez un mot:\n"))
        print(mot_1)
        mot_2 = list(input("Entrez un autre mot:\n"))
        print(mot_2)

        mot_1 = mot_1.sort()
        mot_2 = mot_2.sort()

        if mot_1 == mot_2:
            print("Les mots sont des anagrammes")
            return True #retourne True quand la condition n'est pas respectée

        print("Les mot ne sont pas des anagrammes")
        return False


#3
def contains_doubles(items: list) -> bool:

    set = {}
    for elem in list: #comment stocker chaque élément de la liste dans l'ensemble
        set = set.add(elem)

    if set == list:
        return False




#4

Comment trouver la valeur la plus élevée de mon dictionnaire? -> sort by values
def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    moy = {}
    for nom, note in student_grades.items():
        moy[nom] = numpy.mean(note) #dict des moyennes
    print(moy)

    return moy

5
def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    # Comment sort by values un dict?
    # Est-ce que l'espace compte comme char?
    list_sentence = []
    for char in sentence:
        list_sentence.append(char)
    occurences = {}
    for elem in list_sentence:
        if list_sentence.count(elem) >= 5:
            occurences[elem] = list_sentence.count(elem)
    print(occurences)


    return occurences

#6
def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données

    recette = input("Entrez un nom de recette:\n")
    ingredients = []
    for i in range(6):
        ingredients.append(input("Entrez un ingrédient:\n"))
    livre_recettes = {recette: ingredients}
    print(livre_recettes)

#6
def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    recette_req = input("Entrez le nom d'une recette:\n")
    if recette_req in livre_recettes:
        print("Les ingrédients de", recette_req, "sont: \n", livre_recettes[recette])


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
