import random
from time import sleep

# A list of Valid coordinates
coord_map = {
    "A1": (0, 0), "A2": (0, 1), "A3": (0, 2), "A4": (0, 3), "A5": (0, 4),
    "A6": (0, 5), "A7": (0, 6), "A8": (0, 7), "A9": (0, 8), "A10": (0, 9),

    "B1": (1, 0), "B2": (1, 1), "B3": (1, 2), "B4": (1, 3), "B5": (1, 4),
    "B6": (1, 5), "B7": (1, 6), "B8": (1, 7), "B9": (1, 8), "B10": (1, 9),

    "C1": (2, 0), "C2": (2, 1), "C3": (2, 2), "C4": (2, 3), "C5": (2, 4),
    "C6": (2, 5), "C7": (2, 6), "C8": (2, 7), "C9": (2, 8), "C10": (2, 9),

    "D1": (3, 0), "D2": (3, 1), "D3": (3, 2), "D4": (3, 3), "D5": (3, 4),
    "D6": (3, 5), "D7": (3, 6), "D8": (3, 7), "D9": (3, 8), "D10": (3, 9),

    "E1": (4, 0), "E2": (4, 1), "E3": (4, 2), "E4": (4, 3), "E5": (4, 4),
    "E6": (4, 5), "E7": (4, 6), "E8": (4, 7), "E9": (4, 8), "E10": (4, 9),

    "F1": (5, 0), "F2": (5, 1), "F3": (5, 2), "F4": (5, 3), "F5": (5, 4),
    "F6": (5, 5), "F7": (5, 6), "F8": (5, 7), "F9": (5, 8), "F10": (5, 9),

    "G1": (6, 0), "G2": (6, 1), "G3": (6, 2), "G4": (6, 3), "G5": (6, 4),
    "G6": (6, 5), "G7": (6, 6), "G8": (6, 7), "G9": (6, 8), "G10": (6, 9),

    "H1": (7, 0), "H2": (7, 1), "H3": (7, 2), "H4": (7, 3), "H5": (7, 4),
    "H6": (7, 5), "H7": (7, 6), "H8": (7, 7), "H9": (7, 8), "H10": (7, 9),

    "I1": (8, 0), "I2": (8, 1), "I3": (8, 2), "I4": (8, 3), "I5": (8, 4),
    "I6": (8, 5), "I7": (8, 6), "I8": (8, 7), "I9": (8, 8), "I10": (8, 9),

    "J1": (9, 0), "J2": (9, 1), "J3": (9, 2), "J4": (9, 3), "J5": (9, 4),
    "J6": (9, 5), "J7": (9, 6), "J8": (9, 7), "J9": (9, 8), "J10": (9, 9),
}

# My special print
def dprint(word):
    print(word)
    print("-"*30)
    sleep(1)

# Values of valid coors
coors = list(coord_map.values())
coor_names = list(coord_map.keys())

# Ships
ships = [
    ["C", "C", "C", "C", "C"],   # Carrier
    ["B", "B", "B", "B"],        # Battleship
    ["R", "R", "R"],             # Cruiser
    ["S", "S", "S"],             # Submarine
    ["D", "D"]                   # Destroyer
]

# Initial board
board = [["~" for _ in range(10)] for _ in range(10)]

# Enemy boards
fake_board = [["~" for _ in range(10)] for _ in range(10)]
real_board = [["~" for _ in range(10)] for _ in range(10)]

def ship(size, ship, drawn_board):
    my_coors = []
    while True:
        start = random.choice(coors)
        if start[1] > (10 - size) or drawn_board[start[0]][start[1]] != "~":
            continue
        else:
            my_index = coors.index(start)
            for i in range(size):
                point = coors[my_index]
                if drawn_board[point[0]][point[1]] != "~":
                    break
                else:
                    my_coors.append(coors[my_index])
                    my_index += 1
            if len(my_coors) == size:
                break
            else:
                continue

    i = 0
    for coor in my_coors:
        drawn_board[coor[0]][coor[1]] = ship[i]
        i += 1

    return my_coors

# Ships coordinates
user_cruizer_coors = ship(3, ships[2], board)
user_battleship_coors =ship(4, ships[1], board)
user_carrier_coors = ship(5, ships[0], board)
user_submarine_coors = ship(3, ships[3], board)
user_destroyer_coors = ship(2, ships[4], board)

user_ships_names ={
    "Cruizer" : user_cruizer_coors,
    "Battleship": user_battleship_coors,
    "Carrier" : user_carrier_coors,
    "Submarine" : user_submarine_coors,
    "Destroyer" : user_destroyer_coors
}

user_ships = list(user_ships_names.values())

# Enemy coordinates
enemy_cruizer_coors = ship(3, ships[2], real_board)
enemy_battleship_coors =ship(4, ships[1], real_board)
enemy_carrier_coors = ship(5, ships[0], real_board)
enemy_submarine_coors = ship(3, ships[3], real_board)
enemy_destroyer_coors = ship(2, ships[4], real_board)

enemy_ships_names = {
    "Battleship":enemy_battleship_coors,
    "Carrier":enemy_carrier_coors,
    "Cruizer":enemy_cruizer_coors,
    "Destroyer":enemy_destroyer_coors,
    "Submarine":enemy_submarine_coors
}

enemy_ships = list(enemy_ships_names.values())

############################################################################################################################

# Remove coor from ship
def remove_coor(my_coor, my_ships):
    ship = next((ship for ship in my_ships if my_coor in ship), None)
    if ship is not None:
        ship.remove(my_coor)
    else:
        pass

# Check lose condition
def is_lose(my_ships_names):
    if not my_ships_names:
        dprint("Your ships are all damaged")
        dprint("You lose ❌")
        return 'lose'
    else:
        pass

# Check winning condition
def is_win(my_ships_names):
    # Check whether all ships were damaged
    if not my_ships_names:
        dprint("Oh you damaged all my ships")
        dprint("You win ✅")
        return "win"
    else:
        pass

# Check if a certain ship is sunk
def is_sunk(my_ships, ships_names):
    sunk_ships = []

    for ship in my_ships:
        if not ship:  # Ship has no coordinates left
            # Find the ship name corresponding to this sublist
            ship_name = next((k for k, v in ships_names.items() if v == ship), None)
            if ship_name:
                dprint(f"{ship_name} is sunk!")
                sunk_ships.append(ship_name)
                ships_names.pop(ship_name)  # Remove to avoid repeated messages
                sleep(1)  # Optional pause for user to read
            # else: ship already reported, do nothing

    return sunk_ships

# Draw the player board (Including ships , water)
def draw_board(drawn_board):
    columns = ["A", "B", "C", "D", "E" , "F", "G", "H", "I", "J"]
    print("    1 2 3 4 5 6 7 8 9 10 ")
    for i in range(len(drawn_board)):
        print(f"{columns[i]} | {" ".join(drawn_board[i])} |")
    print("    "+"-"*20)

# Hit or miss (User)
def hit_or_miss_user(coor):
    my_coor = coord_map[coor]
    if real_board[my_coor[0]][my_coor[1]] == "~":
        dprint("Miss ❌❌")
        real_board[my_coor[0]][my_coor[1]] = "O"
        fake_board[my_coor[0]][my_coor[1]] = "O"
        return
    elif real_board[my_coor[0]][my_coor[1]] in ["X", "O"]:
        dprint("Already fired here ❌❌")
        return
    else:
        dprint("Hit ✅✅")
        real_board[my_coor[0]][my_coor[1]] = "X"
        fake_board[my_coor[0]][my_coor[1]] = "X"
        remove_coor(my_coor, enemy_ships)
        sunk_ships = is_sunk(enemy_ships, enemy_ships_names)

    status = is_win(enemy_ships_names)
    return status

# Hit or miss (AI)
def hit_or_miss_comp(coor):
    my_coor = coord_map[coor]
    if board[my_coor[0]][my_coor[1]] == "~":
        dprint("Miss ❌❌")
        board[my_coor[0]][my_coor[1]] = "O"
        return
    else:
        dprint("Hit ✅✅")
        board[my_coor[0]][my_coor[1]] = "X"
        remove_coor(my_coor, user_ships)
        sunk_ships = is_sunk(user_ships, user_ships_names)

    status = is_lose(user_ships_names)
    return status

# Print Out the user's board
dprint("Your Board")
draw_board(board)

# Print Out the enemy board
dprint("Enemy Board")
draw_board(fake_board)

# Main game loop
while True:
    # User's turn
    shot = input("Give your shot: ").strip().upper()
    print("-"*30)
    if shot not in coor_names:
        dprint("Not a valid coordinate ❗❗")
        continue
    else:
        status = hit_or_miss_user(shot)
        if status == "win":
            sleep(2)
            break
    
    # Redraw the board
    dprint("Your Board")
    draw_board(board)
    sleep(1)
    dprint("Enemy Board")
    draw_board(fake_board)
    sleep(1)

    # Computer's turn
    dprint("The enemy is now choosing his shot please wait ...")
    while True:
        comp_shot = random.choice(coor_names)
        my_coor = coord_map[comp_shot]
        if board[my_coor[0]][my_coor[1]] not in ("X", "O"):
            break
        else:
            continue
    dprint(f"The computer has chosen {comp_shot}")
    comp_status = hit_or_miss_comp(comp_shot)
    if comp_status == 'lose':
        sleep(2)
        break

    # Redraw the board
    dprint("Your Board")
    draw_board(board)
    sleep(1)
    dprint("Enemy Board")
    draw_board(fake_board)
    sleep(1)