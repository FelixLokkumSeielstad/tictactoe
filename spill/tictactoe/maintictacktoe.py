import mysql.connector
import os
import sys
import hashlib

#connecter til databasen
connect = mysql.connector.connect(
    host='localhost',
    user='FelixAdmin',
    password='FelixAdmin',
    database='mywbsdb'
) 

#def tegn_brett(spots, størelse):
#    for i in range(1, størelse * størelse + 1):
#        print(f"|{spots[i]}", end="")
#        if i % størelse == 0:
#           print("|")

#def tegn_board(spots):
#  board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
#             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
#             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
#  print(board)størelse

#her tegner jeg brettet med en 
def tegn_brett(spots, størelse):

    board_størelse = størelse * størelse
    brett = ""

    for i in range(1, board_størelse + 1):#iterates board_størelse antall ganger
        brett += "|" + str(spots[i])# Legger til verdien av spots[i] i brettet med "|" i mellom

        if i % størelse == 0: #Sjekker om i er et multiplum av størelse. Hvis det er tilfellet, betyr det at vi har nådd slutten av en rad.
            brett += "|\n" # Legger til "|" for å avslutte raden og "\n" for å gå til neste linje
    print(brett)

def hvem_tur(turn):
  if turn % 2 == 0:#Skall være ærlig vet ikke hvordan men gir meg et partall eller odetall
    return 'X'
  else:
    return 'O'
  
#sjekker alle mulige måter å vinne
def sjekkwin(spots):

    winmotr = {}

    antall_spots = len(spots) #finner antall spots
    spotsi2 = antall_spots ** 0.5 #finner kvadratrotten av antall_spots
    board_size = int(spotsi2) #gjør square_root til int

    if board_size == 3: # lagger vinner kombiasjoner for kart 4
        winmotr[(1, 2, 3)] = True
        winmotr[(4, 5, 6)] = True
        winmotr[(7, 8, 9)] = True
    elif board_size == 4:# lagger vinner kombiasjoner for kart 4
        winmotr[(1, 2, 3, 4)] = True
        winmotr[(5, 6, 7, 8)] = True
        winmotr[(9, 10, 11, 12)] = True
        winmotr[(13, 14, 15, 16)] = True
        winmotr[(1, 5, 9, 13)] = True
        winmotr[(2, 6, 10, 14)] = True
        winmotr[(3, 7, 11, 15)] = True
        winmotr[(4, 8, 12, 16)] = True
        winmotr[(1, 6, 11, 16)] = True
        winmotr[(4, 7, 10, 13)] = True
    else:# lagger vinner kombiasjoner for kart 5
        winmotr[(1, 2, 3, 4, 5)] = True
        winmotr[(6, 7, 8, 9, 10)] = True
        winmotr[(11, 12, 13, 14, 15)] = True
        winmotr[(16, 17, 18, 19, 20)] = True
        winmotr[(21, 22, 23, 24, 25)] = True
        winmotr[(1, 6, 11, 16, 21)] = True
        winmotr[(2, 7, 12, 17, 22)] = True
        winmotr[(3, 8, 13, 18, 23)] = True
        winmotr[(4, 9, 14, 19, 24)] = True
        winmotr[(5, 10, 15, 20, 25)] = True
        winmotr[(1, 7, 13, 19, 25)] = True
        winmotr[(5, 9, 13, 17, 21)] = True

# Gå gjennom hvert vindu og resultat i winmotr
    for winmotr, result in winmotr.items():
        all_match = True
        #gå gjennom hver posisjon i vinduet
        for position in winmotr:
            if spots[position] != spots[winmotr[0]]:#sjekk om verdien i posisjonen ikke matcher verdien i den første posisjonen i vinduet
                all_match = False
                break
        #Hvis alle posisjonene i vinduet matcher, returner resultatet
        if all_match:
            return result

    return False


def spillet():
    #allt her runner bare en gang
    print("velg en størelse på brettet mellom 3 og 5")
    board_størelse = int(input())
    
    #Ser om user input er 3,4 eller 5
    if board_størelse in [3, 4, 5]:
        spots = {}
        for i in range(1, board_størelse ** 2 + 1):
            spots[i] = str(i)
    else:
        print("kan ikke lage dette prøv igjen")
        spillet()

    spiller, complete = True, False
    turn = 1
    prev_turn = -1
    vinner = []

    while spiller:
        #her runner spillet flere ganger
        os.system('cls' if os.name == 'nt' else 'clear')#denne coden renser skjermen
        tegn_brett(spots, board_størelse)
        if prev_turn == turn:
            print("Ugjyldig plass. velg en annen")
        prev_turn = turn
        print("Spiller " + str((turn % 2) + 1) + "'s tur: Trykk s for å stoppe å spille")#samme her trenger coden får å bytte tur

        choice = input()
        if choice == 's':
            spiller = False

        elif str.isdigit(choice) and int(choice) in spots: #sjekker om choice er en string med bruk av isdigit
            if not spots[int(choice)] in {"X", "O"}: #sjekker om av spotsa er fylt med X eller O
                turn += 1
                spots[int(choice)] = hvem_tur(turn)# skriver in x eller o på spillerens valg eller spots[int(choice)]

        #denne koden regner ut hvor lenge spille kan vare basert på størelsen på kartet
        if sjekkwin(spots):
            spiller, complete = False, True
        if turn > board_størelse * board_størelse:
            spiller = False

    os.system('cls' if os.name == 'nt' else 'clear')
    tegn_brett(spots, board_størelse)
    if complete:
        if hvem_tur(turn) == 'X':
            print("Spiller 1 vant")
            erklærtvinner()
        else:
            print("Spiller 2 vant")
            erklærtvinner()
    else:
        print("ingen vinner")
        spilligjen()

#er en funksjon som runner i spilligjen() får å opprette en bruker  
def oppretbruker(spiller_name):
    print("Du må lage et bruker navn")
    name =  input()
    print("Skriv passord til brukeren")
    passwd =  input()
    hashed_passwd = hashlib.sha256(passwd.encode()).hexdigest()
    score = 1
    #lagger en insertkomando med tomme values jeg kan sette senere før jeg executer får å hindre sql injektions 
    lagbruker = "INSERT INTO gamepoints (name, score, passwd) VALUES (%s, %s, %s)"
    cursor = connect.cursor()
    cursor.execute(lagbruker, (name, score, hashed_passwd))
    connect.commit()
    cursor.close()
    spilligjen()


#denne funksjonen kan starte 
def spilligjen():
    print("Takk for at du spilte!")
    print("Vil du spille igjen? (yes/no)")
    spill_igjen_input = input()
    if spill_igjen_input.lower() == 'yes':
        spill_igjen = False
    elif spill_igjen_input.lower() == 'no':
        sys.exit()
        
def erklærtvinner():
        print("Skriv navn på spiller som vant")
        
        spiller_name = input()
        if spiller_name.lower() != "":
            print (spiller_name)
            cursor = connect.cursor()
            navnidb = "SELECT * FROM gamepoints WHERE name = %s"
            cursor.execute(navnidb, (spiller_name,))
            navnerdb = cursor.fetchone()
            
            if navnerdb:
                print("Navn er tatt. Er dette deg")
                print("(yes/no)")
                opptare_bruker = input()
                if opptare_bruker == "yes":
                    print("skriv passord for denne brukeren")
                    checkpasswd = input()
                    hashed_passwd = hashlib.sha256(checkpasswd.encode()).hexdigest()
    
                    cursor = connect.cursor()
                    sql = "SELECT passwd FROM gamepoints WHERE name = %s"
                    cursor.execute(sql, (spiller_name,))
                    hash_passwd = cursor.fetchone()
                    stored_hashed_passwd = hash_passwd[0] if hash_passwd else None
    
                    if stored_hashed_passwd and stored_hashed_passwd == hashed_passwd:
                        print("Login successful")
                        hentscore = "SELECT score FROM gamepoints WHERE name = %s"
                        cursor.execute(hentscore, (spiller_name,))
                        getscore = cursor.fetchone()
                        scorena = getscore[0]
                        new_score = scorena + 1

                        oppdater_score = "UPDATE gamepoints SET score = %s WHERE name = %s"
                        cursor.execute(oppdater_score, (new_score, spiller_name))
                        connect.commit()
                        spilligjen()
                    else:
                        print("Invalid username or password")
    
                    cursor.close()
                else: 
                    print("oppret bruker")
                    oppretbruker(navnerdb)
            else:
                print("Du har ikke bruker. lage en. nå")
                oppretbruker(navnerdb)
        else:
            print("du må skrive et navn")
            erklærtvinner()


    
spill_igjen = True

while spill_igjen:
        spillet()
