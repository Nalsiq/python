import urllib.request
import re, sys
import random
import webbrowser


alphabet = ["a", "A","Ą", "ą", "B", "b","C", "c","Ć","ć" ,"D", "d","E", "e","Ę", "ę", "F", "f","G", "g","H", "h","I", "i","J", "j","K", "k","L", "l","Ł", "ł","M", "m","N", "n","Ń","ń", "O", "o","P", "p","R", "r","S", "s","Ś", "ś", "T", "t","Q", "q","U", "u","W", "w","Y", "y","Z", "z","Ż", "ż","Ź" "ź", "x", "X"]


list_of_words = ["kajak","Karol","Ania","Andrzej"]#lista słów

draw = random.randint(0,3)#losuje miejsce słowa z listy
word = list_of_words[draw]#wyciąga dane słowo z listy

length = len(word)# liczy ile liter ma słowo

mysterious_word = "_" * length#zamienia na podłogi

url = f"https://sjp.pwn.pl/slowniki/{word}.html"
###
print("Witaj w wisielcu")
print("Możesz wybrac 3 poziomy trdności")
level_of_difficulty = input("Aby wybrać poziom trudnośći, wpisz:  Easy or Medium or Hard")
print(level_of_difficulty)

hangman4 = (""" 
          +---+  
              |
              |
              |
             === """)

hangman3 = (""" 
          +---+  
          O   |
          |   |
              |
             === """)
hangman2 = (""" 
          +---+  
          O   |
         /|\  |
              |
             === """)
hangman1 = ("""
          +---+  
          O   |
         /|\  |
         /    |
             === """)
hangam0 = ("""
          +---+  
          O   |
         /|\  |
         / \  |
             === """)



if level_of_difficulty == "Easy":
    print("Wybrałeś poziom łatwy, masz 5 szans")    
    number_of_tries = 5
    
elif level_of_difficulty == "Medium":
    print("Wybrałeś poziom średni, masz 3 szanse")
    number_of_tries = 3

elif level_of_difficulty == "Hard":
    print("Wybrałeś poziom trudny, masz 1 szanse")
    number_of_tries = 1
else:
    print("Błedny zapis")
    while not (level_of_difficulty == "Easy" or  level_of_difficulty == "Medium" or level_of_difficulty == "Hard"):
          level_of_difficulty = input("Napisz jeszcze raz")

    



def read_until_div_closed(string, start):
    result = ""
    s = string[start:]
    for i in range(0, len(s)):
        if s[i:i+6] == "</div>":
            return result
        result += s[i]

def strip_of_shit(string):
    result = ""
    began_traversing = False
    for i in range(0, len(string)):
        if (string[i] == "«"):
            began_traversing = True
        elif (string[i] == "»"):
            return result
        elif began_traversing:
            result += string[i]
    return ''

def get_definition(link):
  fp = urllib.request.urlopen(link)
  mybytes = fp.read()

  mystr = mybytes.decode("utf8")
  fp.close()

  pattern = "<div class=\"znacz\">"

  out = []

  for i in re.finditer(pattern, mystr):
    out.append(strip_of_shit(read_until_div_closed(mystr, i.end(0))))

  return out


definition = get_definition(url)

print(definition)

while len(definition) == 0:
    draw = random.randint(0,3)
    word = list_of_words[draw]
    url = f"https://sjp.pwn.pl/slowniki/{word}.html"
    definition = get_definition(url)
    print(definition)
    length = len(word)
    mysterious_word = "_" * length

    
    

used_letters = []
user_word = ["_"] * length

def find_indexes(word,letter):
    indexes = []

    for index, letter_word in enumerate(word):
        if letter == letter_word:
                indexes.append(index)

    return indexes



while True:
    letter = input("Podaj litere: ")
    while letter not in alphabet:
        print("Złe użycie znaków")
        letter = input("Napisz litere jeszcze raz: ")
    while len(letter) != 1:
        letter = input("Napisz jedną litere jeszcze raz:  ")
       

    used_letters.append(letter)

    print(f"Użyte litery: {used_letters} ")



   

    letter_indexes = find_indexes(word,letter)

    if len(letter_indexes) == 0:
        print("Nie ma tej litery w słowie")
        number_of_tries = number_of_tries -1 
        if number_of_tries == 4:
            print(hangman4)
        elif number_of_tries == 3:
            print(hangman3)
        elif number_of_tries == 2:
            print(hangman2)
        elif number_of_tries == 1:
            print(hangman1)
        elif number_of_tries == 0:
            print(hangam0)
        print("Ilość szans:", number_of_tries)

        if number_of_tries == 0:
            print("Przegrałeś")
            sys.exit(0)
    else:
        for index in letter_indexes:
            user_word[index] = letter
        print(user_word)
            
        if "".join(user_word) == word:
            print("Wygrałeś")
            sys.exit(0)
