#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0 :
        number = number * -1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    nouvTab = []
    for i in prefixes:
        nouvTab.append(i + suffixe)
    return nouvTab

def est_premier(nombre : int) -> bool:
    for i in range(2, nombre//2):
        if nombre % i == 0:
            return False

    return True

def prime_integer_summation() -> int:
    nb_premiers = 3
    somme_premiers = 10
    i = 6

    while nb_premiers < 100:
        if est_premier(i):
            somme_premiers += i
            nb_premiers += 1
        i += 1

    # En python, il est possible de faire sum(tableau), ce qui additionne tous ses éléments
    return somme_premiers


def factorial(number: int) -> int:
    nouvNombre = 1
    for i in range(1, number+1):
        nouvNombre = nouvNombre * i
    return nouvNombre


def use_continue() -> None:
    for i in range(1, 10):
        if i == 5:
            continue
        print(i)
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:

    liste_fin = []

    for groupe in groups :
        if len(groupe) > 10 or len(groupe) <= 3:
            liste_fin.append(False)
            continue
        if 25 in groupe:
            liste_fin.append(True)
            continue

        plus_de_70 = False
        exactement_50 = False
        a_mineur = False

        if 50 in groupe:
            exactement_50 = True

        # Au lieu d'une autre boucle, il aurait été possible d'utiliser "max" et "min".
        # Wow les tableaux en Python. Enfin, les listes.

        for membre in groupe:
            if membre < 18:
                a_mineur = True
                break
            elif membre > 70:
                plus_de_70 = True

        if a_mineur or (plus_de_70 and exactement_50):
            liste_fin.append(False)
        else:
            liste_fin.append(True)

    return liste_fin


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
