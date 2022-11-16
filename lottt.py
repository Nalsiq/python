import random
random.randint
# losowanie z ilu tam liczb, i porowaninie jes z liczbami od uzytkownika, robie uzytkownik ma kase, i ma do wyboru trzy kupony, o roznej wartosci, losowanie numerow, lista uzywaj
# jesli masz te same numery wygrales
def sprawdzanie(uzytkownik, komputer):
    return
def stworz_liste():
    lista=[]
    for a in range(1,11):
        lista.append(a)
    return lista

poprawne_liczby= stworz_liste()


print(f"Podaj trzy liczby z {poprawne_liczby}")


liczby= [
     int(input("Podaj liczbe1: ")),
     int(input("Podaj liczbe2: ")),
     int(input("Podaj liczbe3: "))
]

zgadza= True

for liczba in liczby:
    if not (liczba in poprawne_liczby):
        zgadza= False

if zgadza:
    print(f"Twoje liczby {liczby}")
else:
    while True:
   
        cos=int(input(f"Podaj  jeszcze raz"))

        if cos in poprawne_liczby:
            break
print(cos)






