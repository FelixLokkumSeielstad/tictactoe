import mysql.connector
import os
import sys
import hashlib

def draw_brett(spots):
  brett = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
  print(brett)
 

def hvem_tur(turn):
  if turn % 2 == 0:
    return 'X'
  else:
    return 'O'
  
#sjekker alle mulige måter å vinne
def sjekkwin(spots):

    win_conditions = {
        (1, 2, 3): True,  
        (4, 5, 6): True,
        (7, 8, 9): True,
        (1, 4, 7): True, 
        (2, 5, 8): True,
        (3, 6, 9): True,
        (1, 5, 9): True,  
        (3, 5, 7): True
    }

    for condition, result in win_conditions.items():
        if all(spots[position] == spots[condition[0]] for position in condition):
            return result

    return False

connect = mysql.connector.connect(
    host='localhost',
    user='FelixAdmin',
    password='FelixAdmin',
    database='mywbsdb'
) 


def play_game():
    spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
             6: '6', 7: '7', 8: '8', 9: '9'}

    spiller, complete = True, False
    turn = 1
    prev_turn = -1
    vinner = []

    while spiller:
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_brett(spots)
        if prev_turn == turn:
            print("Ugjyldig plass. velg en annen")
        prev_turn = turn
        print("Spiller " + str((turn % 2) + 1) + "'s tur: Trykk s for å stoppe å spille")

        choice = input()
        if choice == 's':
            spiller = False
        elif str.isdigit(choice) and int(choice) in spots:
            if not spots[int(choice)] in {"X", "O"}:
                turn += 1
                spots[int(choice)] = hvem_tur(turn)

        if sjekkwin(spots):
            spiller, complete = False, True
        if turn > 8:
            spiller = False

    os.system('cls' if os.name == 'nt' else 'clear')
    draw_brett(spots)
    if complete:
        if hvem_tur(turn) == 'X':
            print("Spiller 1 vant")
        else:
            print("Spiller 2 vant")
    else:
        print("ingen vinner")


def oppretbruker(spiller_name):
    print("Du må lage et bruker navn")
    name =  input()
    print("Skriv passord til brukeren")
    passwd =  input()
    hashed_passwd = hashlib.sha256(passwd.encode()).hexdigest()
    score = 1
    lagbruker = "INSERT INTO gamepoints (name, score, passwd) VALUES (%s, %s, %s)"
    cursor = connect.cursor()
    cursor.execute(lagbruker, (name, score, hashed_passwd))
    connect.commit()
    cursor.close()
    spilligjen()

    
def spilligjen():
    print("Takk for at du spilte!")
    print("Vil du spille igjen? (yes/no)")
    spill_igjen_input = input()
    if spill_igjen_input.lower() == 'yes':
        spill_igjen = False
    elif spill_igjen_input.lower() == 'no':
        sys.exit()

        
spill_igjen = True

while spill_igjen:
        play_game()
        print("Skriv navn på spiller som vant")
        print("hvis uavgjort ikke skriv noe")
        
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
                        current_score = getscore[0]
                        new_score = current_score + 1

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
            spilligjen()



