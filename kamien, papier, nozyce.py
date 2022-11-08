import random
random.randint

print("Witaj w grze Papier kamien nozyce")
print("Zeby zcazcac gre wpisz x")

start=input("x")


if start=="x":
    ruch=input("Wyierz Papier=1, Kamien=2, Nozyce=3")
    #print(ruch)
   

    #if ruch=="P" or ruch=="K" or ruch=="N":
       #  print("Teraz kolej komputera")
    if ruch=="1":
        print("Kolej komputera")
    elif ruch=="2":
        print("Kolej komputera")
    elif ruch=="3":
        print("Kolej Komputera")

    else:("Zle urzycie znakow")



komputer=random.randrange(1,3)
print(f"Ruch komputera to {komputer}")


if ruch=="1" and komputer=="1":
    print("Papier vs Papier= remis")

elif ruch=="2" and komputer=="2":
    print("Kamien vs Kamien= remis")

elif ruch=="3" and komputer=="3":
    print("Norzyce vs Norzyce = remis")

elif ruch=="1" and komputer=="3":
    print("Przegrales :(")

elif ruch=="2" and komputer=="3":
    print("Przegrales :(")

elif ruch=="1" and komputer=="2":
    print("Przegrales :(")

else:
    print("wygrales :)")







 




