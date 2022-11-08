

import random 


def powitanie(imie):
    print("Czesc", imie)

imie=input("AJk masz na imie?")
powitanie(imie)




def wartoscbezwzgledna(liczba):
    if liczba>=0:
        return liczba
    else:
        return -liczba

print(wartoscbezwzgledna(-10))
