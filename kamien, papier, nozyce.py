import random
random.randint

print("Witaj w grze Papier kamien nozyce")
print("Zeby zcazcac gre wpisz x")

start=input("x")


if start=="x":
    ruch=input("Wyierz Papier=1, Kamien=2, Nozyce=3")
    #print(ruch)

while ruch!= "1" and ruch!= "2" and ruch!= "3":
    print("zle urzycie znakow ")
    ruch=input("Wpisz jeszcze raz poprawny znak: Papier=1, Kamien=2, Nozyce=3")
    

  

   



komputer=random.randint(1,3)
print(f"Ruch komputera to {komputer}")


if ruch=="1" and komputer==1: # ruch zamineiam na liczbe poerównoje z ruchem kompa essunia, jesli taki sam to remis i esssa 
    print("Papier vs Papier= remis")

elif ruch=="2" and komputer==2:
    print("Kamien vs Kamien= remis")

elif ruch=="3" and komputer==3:
    print("Norzyce vs Norzyce = remis")

elif ruch=="1" and komputer==3:
    print("Przegrales :(")

elif ruch=="3" and komputer==2:
    print("przegrales :(")

elif ruch=="1" and komputer==3:
    print("Przegrales :(")

elif ruch=="2" and komputer==1:
      print("Przegrales :(")
else:
    print("wygrales :)")






 




