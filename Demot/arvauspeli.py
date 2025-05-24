# Ohjelma, joka pyytää käyttäjää
# arvailemaan lukuja
from random import randint


while True:

    # Tämä arpoo satunnaisen luvun väliltä 1...1000
    luku = randint(1,1001)
    arvaukset = 0
    
    while True:
        arvaus = int(input("Arvaa luku: "))
        arvaukset += 1
        
        if luku < arvaus:
            print("Luku on pienempi!")
        elif luku > arvaus:
            print("Luku on suurempi!")
        else:
            print("Arvasit luvun!")
            print(f"Käytit {arvaukset} arvausta.")
            break
        
    uudestaan = input("Haluatko pelata uudestaan k/e: ")
    if uudestaan == "e":
        break
