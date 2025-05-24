"""Ohjelma mallintaa yksinkertaista varastokirjanpitoa"""

def nayta_UI():
    """Näyttää käyttöliittymän"""
    while True:
        print("Valitse toiminto:")
        print("1. Lataa tuotteet tiedostosta")
        print("2. Tallenna tuotteet tiedostoon")
        print("3. Lisää tuote")
        print("4. Ota tuotetta varastosta")
        print("5. Etsi tuote")
        print("6. Listaa kaikki tuotteet")
        print("7. Listaa vähissä olevat tuotteet")
        print("0. Poistu")
        
        valinta = int(input("Valintasi: "))
        
        if valinta == 1:
            lataa_tiedot()
            print("Tiedot ladattu!")
        elif valinta == 2:
            tallenna_tiedot()
            print("Tiedot tallennettu!")
        elif valinta == 3:
            nimi = input("Anna tuotteen nimi:")
            maara = int(input("Anna määrä: "))
            lisaa_tuote(nimi, maara)
            print("Tuote lisätty!")
        elif valinta == 4:
            nimi = input("Anna tuotteen nimi:")
            maara = int(input("Anna määrä: "))
            if ota_tuotetta(nimi, maara):
                print("Tuotetta otettu!")
            else:
                print("Tuotetta ei ollut tarpeeksi varastossa.")
        elif valinta == 5:
            tuotteet = etsi_tuotteet(input("Anna hakutermi: "))
            # Jos tuotelista ei ollut tyhjä...
            if tuotteet:
                print(tuotteet)
            else:
                print("Tuotteita ei löytynyt.")
        elif valinta == 6:
            print(listaa_tuotteet())

        elif valinta == 7:
            print(vahissa_olevat())
            

        elif valinta == 0:
            break
        
        # Ylimääräinen rivinvaihto
        print()        

def lataa_tiedot() -> list:
    """Lataa varaston tuotetiedot tiedostosta"""
    # tyhjennetään ensin kaikki nykyiset tuotteet
    global tuotteet
    tuotteet.clear()
    
    # Tiedoston nimi on aina sama
    with open("tuotteet.csv") as tiedosto:
        for rivi in tiedosto:
            tiedot = rivi.strip().split(",")
            # rivillä on ensin nimi, sitten kappalemäärä
            tuotteet[tiedot[0]] = int(tiedot[1])
            
def tallenna_tiedot():
    """Tallentaa varaston tuotetiedot tiedostoon"""
    # Tiedoston nimi on aina sama
    with open("tuotteet.csv", "w") as tiedosto:
        for nimi, maara in tuotteet.items():
            rivi = f"{nimi},{maara}\n"
            tiedosto.write(rivi)
              
def lisaa_tuote(nimi: str, maara: int):
    """Lisää annetun tuotteen varastoon"""
    global tuotteet
    # Tarkistetaan, onko tuote jo varastossa
    if nimi in tuotteet:
        # Jos on, lisätään saldoa
        tuotteet[nimi] += maara
    else:
        # Jos ei, lisätään uusi tuote
        tuotteet[nimi] = maara
    
def ota_tuotetta(nimi: str, maara: int) -> bool:
    """Ottaa tuotetta varastosta annetun määrän, jos sitä on tarpeeksi

    Args:
        nimi (str): tuotteen nimi
        maara (int): kuinka paljon tuotetta otetaan

    Returns:
        bool: True, jos tuotetta oli varastossa tarpeeksi, muuten False
    """
    global tuotteet
    if nimi in tuotteet:
        # onko varastossa tarpeeksi...
        if tuotteet[nimi] >= maara:
            tuotteet[nimi] -= maara
            return True
            # Tuotetta ei ollut (tarpeeksi) varastossa
    return False
    
def etsi_tuotteet(hakutermi: str) -> str:
    """Hakee annettuja tuotteita varastosta"""
    # iteroidaan tuotteet läpi, tallennetaan merkkijonoon sopivat
    tulos = ""
    # dictin ei tarvitse olla global, koska sitä ei muuteta
    for nimi in tuotteet:
        if hakutermi in nimi:
            # Rivinvaihto perässä tekee siistimmän tulosteen
            tulos += f"{nimi}, {tuotteet[nimi]} kpl.\n"
            
    return tulos
    
def listaa_tuotteet() -> str:
    """Listaa kaikki varaston tuotteet"""
    
    # hyödynnetään etsi_tuotteet -funktiota tyhjällä hakutermillä,
    # joka löytää siis kaikki tuotteet
    return etsi_tuotteet("")

def vahissa_olevat() -> list:
    """Listaa vähissä olevat tuotteet"""
    tmaara = int(input("Anna enimmäismäärä: "))
    lista = []

    for avain, arvo in tuotteet.items():
        if arvo < tmaara:
            print(f"{avain}, {arvo} kpl.")
    
# ------------------    
# PÄÄOHJELMA
# ------------------

# Varastotiedot ovat tallessa globaalissa sanakirjassa
# Avaimena on tuotteen nimi ja arvona sen määrä kokonaislukuna
tuotteet = {}
nayta_UI()