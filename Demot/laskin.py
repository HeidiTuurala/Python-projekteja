luku = 0
operaatio = 0

while True:
    
    print("Luku on" , luku,".")
    operaatio = input("Anna operaatio (tyhjä lopettaa): ")

    if operaatio [0] == "+":
        operaatio = int(operaatio[1:len(operaatio)])

        luku = luku + operaatio

    elif operaatio [0] == "-":
        operaatio = int(operaatio[1:len(operaatio)])

        luku = luku - operaatio
    
    elif operaatio [0] == "*":
        operaatio = int(operaatio[1:len(operaatio)])

        luku = luku * operaatio
    
    elif operaatio [0] == "/":
        operaatio = int(operaatio[1:len(operaatio)])

        luku = luku // operaatio

    else:
        print("Kiitos ja moi!")
        break
        