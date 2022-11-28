'''
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
'''
import random

# zmienne stałe
NUMBER_AMOUNT = 100 # ilość liczb wylosowanych przez komputer
NUMBER_RANGE = 1000 # zakres liczb wylosowanych przez komputer (0 do NUMBER_RANGE)
GUESS_AMOUNT = 10 # ilość liczb, które może podać użytkownik (nie może wynosić 0)
BASE_REWARD = 100 # nagroda za zgadnięcie jednej liczby

# funkcja zwracająca listę o długości NUMBER_AMOUNT z losowymi liczbami z zakresu 0 do NUMBER-RANGE
def generate_numbers():

    result = []

    for i in range(NUMBER_AMOUNT):

        result.append(random.randint(0, NUMBER_RANGE)) # do wyniku dodajemy losową liczbę

    return result

# funkcja pobierająca dane od użytkownika i weryfikująca je. Zwraca listę z wybranymi przez użytkownika liczbami
def get_guesses():

    guesses = []

    count = 0 # licznik śledzący, ile liczb podał użytkownik

    while True: # nieskończona pętla

        guess = input(f"Podaj liczbę {count}: ")

        if not guess.isdigit(): # jeśli tekst od użytkownika nie da zamienić się na liczbę całkowitą
            print("Musisz podać liczbę całkowitą!")
            continue # wróć na początek pętli

        guess = int(guess) # zamieniamy tekst na liczbę

        if guess < 0 or guess > NUMBER_RANGE: # jeśli liczba użytkownika nie jest w zakresie 0 do NUMBER_RANGE
            print(f"Musisz podać liczbę z przedziału 0 do {NUMBER_RANGE}!")
            continue # wróć na początek pętli

        if guess not in guesses: # jeśli liczba nie jest już w wprowadzonych przez użytkownika liczbach
            guesses.append(guess) # dodaj liczbę do wprowadzonych liczb
            count += 1 # zwiększ licznik wprowadzonych liczb
        else:
            print("Nie możesz podać tej samej liczby drugi raz!")
            # można tu też dać continue, ale nie jest potrzebne

        if len(guesses) == GUESS_AMOUNT: # jeśli otrzymaliśmy tyle liczb, ile potrzebujemy
            return guesses # zwracamy liczby wprowdzone przez użytkownika

# funkcja zwracająca, ile liczb poprawnie zgadł użytkownik
def check_score(numbers, guesses): # numbers - liczby wylosowane przez komputer; guesses - liczby wprowadzone przez użytkownika

    score = 0

    for guess in guesses:

        if guess in numbers: # jeśli zgadnięta liczba należy do wylosowanych przez komputer liczb
            score += 1

    return score # zwracamy wynik

######################################################################################################
# Faktyczna gra
#######################################################################################################

print("Lotto")
print(f"Podaj {GUESS_AMOUNT} liczb:")

guesses = get_guesses() # zdobywamy liczby od użytkownika
numbers = generate_numbers() # zdobywamy liczby od komputera
score = check_score(numbers, guesses) # sprawdzamy wynik

print(f"Podane przez ciebie liczby: {guesses}")
print(f"Zgadłeś poprawnie {score} liczb!")
print(f"Wygrałeś {BASE_REWARD * score} bobuksów!") # mnożymy nagrodę, za jedno zgadnięcie przez liczbę poprawnych zgadnięć






