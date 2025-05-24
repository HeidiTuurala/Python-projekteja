def laske_yhteen(eka: float, toka: float):
    summa = eka + toka
    return summa
    
def vahenna(eka: float, toka: float):
    erotus = eka - toka
    return erotus

def kerro(eka: float, toka: float):
    tulo = eka * toka
    return tulo

def jaa(eka: float, toka: float):
    osam = eka / toka
    return osam

def menu():
    print("Mitä haluat tehdä?")
    print("1 Laske yhteen")
    print("2 Vähennä")
    print("3 Kerro")
    print("4 Jaa")
    print("0 Lopeta")

def kysy_luku():
    luku = float(input("Anna luku: "))
    return luku

tulos = 0


while True:
    print("Tulos on", tulos)
    menu()
    valinta = int(input("Valinta: "))
    if valinta == 0:
        break
    
    if valinta == 1:
        luku = kysy_luku()
        tulos = laske_yhteen(tulos, luku)
    elif valinta == 2:
        luku = kysy_luku()
        tulos = vahenna(tulos, luku)
    elif valinta == 3:
        luku = kysy_luku()
        tulos = kerro(tulos, luku)
    elif valinta == 4:
        luku = kysy_luku()
        tulos = jaa(tulos, luku)
