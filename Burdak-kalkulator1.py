def dodawnie(a, b):
    return



a=int(input("Podaj pierwsza liczba"))
print(a)

b=int(input("Podaj druga liczba"))
print(b)


dzialanie=input("Jakie dzalanie chcesz wykonac, + dodawanie - odejmowanie, * mnozenie, / dzielenie")
print(dzialanie)


if dzialanie=="+":
    wynik=a+b
    print(f"Wynik dzialania to {wynik}")
elif dzialanie=="-":
    wynik=a-b
    print(f"Wynik dzialania to {wynik}")
elif dzialanie=="*":
    wynik=a*b
    print(f"Wynik dzialania to {wynik}")
elif dzialanie=="/":

    while b==0:
        print("Nie dziel przez 0")
        b=int(input("Podaj liczbe jeszce raz :"))
    wynik=a/b
    print(f"Wynik dzialanai to {wynik}")
   # if b==0:
        #print("Nie mozna dzilic przez zero")
    #else:
        #wynik=a/b 
        #print(f"Wynik dzialania to {wynik}")
elif dzialanie=="^":
    wynik=a**b
    print(f"Wynik dzialania to {wynik}")
else:
    
    print(" Zle urzycie znakow")