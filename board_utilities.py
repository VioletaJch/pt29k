# board_utilities.py

def create_board() -> list:
    # Sukuria tuščią 3x3 žaidimo lentą. Dvimatė matrica (sąrašas sąraše)
    return [[" " for _ in range(3)] for _ in range(3)]
# [
#     [" ", " ", " "],  
#     [" ", " ", " "], 
#     [" ", " ", " "]  
# ]

def print_board(board: list) -> None:
    # Atspausdina 3x3 žaidimo lentą.
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board: list, player: str) -> bool:
    #  Patikrina, ar dabartinis žaidėjas laimėjo
    # Tikrinamos eilutės, stulpeliai ir įstrižainės
    for i in range(3): # for cikle funkcija tikrina visas tris lentos eilutes.
        if all([cell == player for cell in board[i]]):  # Tikrina eilutes. Funkcija naudoja all metodą su list comprehention, kad patikrintų , ar visi elementai board[i] yra vienodi ir atitinka žaidėjo simbolį.
            return True
        if all([board[j][i] == player for j in range(3)]):  # Tikrina stulpelius
            return True
    if all([board[i][i] == player for i in range(3)]):  # Tikrina įstrižainę
        return True
    if all([board[i][2-i] == player for i in range(3)]):  # Tikrina anti-įstrižainę. Apskaičiuojamas priešingas indeksas 2-i.
        return True
    return False

def is_full(board: list) -> bool:
    # Patikrina, ar lenta pilna (nėra tuščių langelių) nustato ar reikia skelbti lygiasias ar žaidėją.
    return all(cell != " " for row in board for cell in row)

