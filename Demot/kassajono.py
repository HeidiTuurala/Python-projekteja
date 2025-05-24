def shopping_queue(clients, new_clients):
    queue = []

    #Lisätään asiakkaita jonoon:
    while len(clients) > 0:
        queue.insert(0, clients.pop())
    
    print("Jonossa on asiakkaita:", queue)
    while queue:
        print("Palvellaan kassalla asiakas", queue.pop(0))

    #Käsitellään uudet asiakkaat

    while len(new_clients) > 0:
        queue.insert(0, new_clients.pop())
    print("Uudet asiakkaat ovat jonossa: ", queue)

    while queue:
        print("Palvellaan uudet asiakkaat: ", queue.pop(0))
    
    print("Jono on nyt tyhjä.")

def main():
    clients=[("Pekka", 56.6), ("Marita", 70.18), ("Ritva", 32.67)]

    clients2=[("Jukka", 16.30), ("Jartsa", 40.14), ("Leena", 6.35)]

    shopping_queue(clients, clients2)

if __name__ == '__main__':
    main()

