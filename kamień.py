import random
random.randint
import urllib.request
import re, sys

print("Witaj w grze papier, kamien, nożyce")
start = input("Aby zacząć gre wpisz: " "Start")
print(start)


list_of_word = ["Kamień", "Papier", "Nożyce"]

draw = random.randint(0,2)
computers_turns = list_of_word[draw]



score_of_computer = 0

score_of_user = 0

if start != "Start":
    print("Błędny zapis")    
    while not start == "Start":
        start = input("Napisz jeszcze raz")
else:
    rules = input("Do wyboru masz: Papier or Kamień or Nożyce")
    print(rules)



counters = {
    "Kamień": "Nożyce",
    "Papier": "Kamień",
    "Nożyce": "Papier"
}






while score_of_computer <= 3 and score_of_user <= 3:
    if rules == "Papier" or rules == "Kamień" or rules == "Nożyce":
        print(f"Ruch komputera to {computers_turns}")
    else:
        print("Błędny napis")
        while not rules == "Papier" or rules == "Kamień" or rules == "Nożyce":
            rules = input("Napisz jeszcze raz")
            print(f"Ruch komputera to {computers_turns}")

    if rules == computers_turns:
        print("Remis")
        print(f"{score_of_user} - {score_of_computer} ")
    elif counters[rules] == computers_turns:
        print("Brawo zdobywasz 1 punkt")
        score_of_user += 1
        print(f"{score_of_user} -{score_of_computer} ")
    elif rules == counters[computers_turns]:
        print("Computer wygrał, dostaje 1 punkt")
        score_of_computer += 1
        print(f"{score_of_user} -{score_of_computer} ")

    rules = input("Podaj kolejny ruch: ")
    draw = random.randint(0,2)
    computers_turns = list_of_word[draw]
    
    print(rules)


    if score_of_computer >= 3 and score_of_user < score_of_computer:
        print("Koniec Gry przegrałeś")
        print(f"Wynik gry: Twój wynik-{score_of_user} Wynik Komputera-{score_of_computer} ")
    else:
        print("Koniec Gry Wygrałeś")
        print(f"Wynik gry: Twój wynik-{score_of_user} Wynik Komputera-{score_of_computer} ")
