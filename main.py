# pagrindinis kodas

import board_utilities as bu 

def get_valid_input(prompt: str) -> int:
#    fukncija gauti teisingą vartotojo įvestį, tik skaičius 1, 2 arba 3 arba „pabaiga“ norint užbaigti žaidimą.
# Jei vartotojas įveda „pabaiga“, funkcija grąžina 'Žaidimo pabaiga'. Jei įvedamas skaičius, jis konvertuojamas į indeksą, pritaikytą žaidimo lentai (0–2 diapazone).

    while True:   #loop funkcija patikrina ar įvestis atitinka reikalavimus ir kartoja veiksmą, kol bus įvestas tinkamas skaičius arba žodis 'pabaiga'.
        user_input = input(prompt)
        if user_input in ("1", "2", "3"): ## in tikrina ar įvesta reikšmė yra user_input sąraše. 
            return int(user_input) - 1  # indeksą konvertuoja į nulį
        elif user_input == "pabaiga":
            print("Žaidimas baigtas")
            return None
        else:
            print("Netinkama įvestis. Įvesk (1, 2, 3) arba 'pabaiga' norint užbaigti žaidimą")

def kryziukai_nuliukai() -> None:
    board = bu.create_board()  
    # tai alternatyvi funkcija  vietoje 'current_player = "X"', loop funkcija leidžia pradedančiam žaidėjui pasirinkti simbolį. 
    while True:

        symbol = input("Pasirink simbolį (X arba 0): ").upper()

        if symbol in ["X", "0"]:
            current_player = symbol
            break
        elif symbol == "PABAIGA":
            print("Žaidimas baigtas")
            return
        else:
            print("Prašau pasirinkti 'X' arba '0'.")

    while True:  # loop naudoja get_valid_input funkciją eilutės ir stulpelio įvedimui užtikrinti, kad būtų priimami tik tinkami skaičiai arba komanda 'pabaiga'
        bu.print_board(board)

        row = get_valid_input(f"žaidėjau {current_player}, norėdamas pasirinkti eilutę, įvesk (1, 2, 3) arba 'pabaiga' norint užbaigti žaidimą: ")

        # if row == "pabaiga":
        #     print("Žaidimas baigtas")
        #     break
        #Tikrinimas dėl None. Vietoje tikrinimo if row == "pabaiga", tikrinama su if row is None.
             #Taip yra todėl, kad funkcija get_valid_input grąžina None, kai vartotojas įveda „pabaiga“.

        if row is None:  
            return

        col = get_valid_input(f"žaidėjau {current_player}, norėdamas pasirinkti stulpelį, įvesk (1, 2, 3) arba 'pabaiga' norint užbaigti žaidimą: ")

        if col is None:
            return   

        if board[row][col] == " ":
            board[row][col] = current_player

            if bu.check_winner(board, current_player):
                bu.print_board(board)
                print(f"Žaidėjas {current_player} laimėjo!") #jeigu check winner funkcija nustato laimėtoją, naudojama string informuoti kuris žaidėjas laimėjo.
                break
            elif bu.is_full(board):
                bu.print_board(board)
                print("Lygiųjų rezultatas!") #jeigu nustatoma, kad lenta pilna išspausdinamas "lygiųjų rezultato įrašas".
                break
            

            current_player = "O" if current_player == "X" else "X"
            # Switch players
            # if current_player == "X":
            #     current_player = "O"
            # else:
            #     current_player = "X"
        else:
            print("langelis užimtas, pasirink kitą")

if __name__ == "__main__":
    kryziukai_nuliukai()
