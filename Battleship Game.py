from __future__ import print_function
import time

gameover = False

P1_turn = True
P1_turn_boats = True
P2_turn_boats = True
fight = True
player_won = False


# Grids
P1_grid = [["  ", "🅐 ", "🅑 ", "🅒 ", "🅓 ", "🅔 ", "🅕 ", "🅖 ", "🅗 ", "🅘 ", "🅙 "],
           ["1 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["2 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["3 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["4 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["5 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["6 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["7 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["8 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["9 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["10", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"]]

P2_grid = [["  ", "🅐 ", "🅑 ", "🅒 ", "🅓 ", "🅔 ", "🅕 ", "🅖 ", "🅗 ", "🅘 ", "🅙 "],
           ["1 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["2 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["3 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["4 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["5 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["6 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["7 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["8 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["9 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
           ["10", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"]]

P1_grid_missed = [["  ", "🅐 ", "🅑 ", "🅒 ", "🅓 ", "🅔 ", "🅕 ", "🅖 ", "🅗 ", "🅘 ", "🅙 "],
                  ["1 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["2 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["3 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["4 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["5 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["6 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["7 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["8 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["9 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["10", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"]]

P2_grid_missed = [["  ", "🅐 ", "🅑 ", "🅒 ", "🅓 ", "🅔 ", "🅕 ", "🅖 ", "🅗 ", "🅘 ", "🅙 "],
                  ["1 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["2 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["3 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["4 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["5 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["6 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["7 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["8 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["9 ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"],
                  ["10", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "▢ ", "-"]]
# Boats
raw_inputs_P1 = []
raw_inputs_P2 = []


def small_space():
    print("\n")


def space():
    print("----\n----\n----\n----\n----\n----\n----\n----\n----\n----\n----\n----\n----\n----\n----\n----\n----\n----")
    print("----\n----\n----\n")


def print_grid(grid):
    line_ver = 0
    finished = False
    while finished is False:
        print(*grid[line_ver], sep='')
        line_ver += 1
        if line_ver == 11:
            finished = True


def boat_pos(boat, grid, raw_inputs):
    run_times_insert_boat = 0
    run_times_remove = 0
    let_to_num = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    func_is_over = False
    run_times_append_boat = 0
    run_times_checked_boat = 1

    while func_is_over is False:
        boat_pos_input_let = str(input("Enter the position of the boat from A-J\n"))
        boat_pos_input_num = int(input("Enter the position of the boat from 1-10\n"))
        cap_boat_pos_input_let = boat_pos_input_let.capitalize()
        if cap_boat_pos_input_let not in letters:
            print("Enter a letter from A-J")
            continue
        if boat_pos_input_num <= 0 or boat_pos_input_num >= 11:
            print("Enter a number from 1-10")
            continue
        posx_let = let_to_num[cap_boat_pos_input_let]
        strip_boat = len(boat)
        hor_or_ver = input("Do you want the ship to be horizontal?\n")
        ver_boat_pos = boat_pos_input_num
        append_var = posx_let
        append_var2 = boat_pos_input_num
        append_of_var = (str(append_var) + str(boat_pos_input_num))
        append_of_var2 = (str(posx_let) + str(append_var2))
        checked = False

        while strip_boat > run_times_checked_boat and checked is False:
            # checks if list raw_input has the same position
            if hor_or_ver == "y":
                if append_of_var in raw_inputs:
                    checked = True
                append_var += 1
                run_times_checked_boat += 1
                append_of_var = (str(append_var) + str(boat_pos_input_num))
            else:
                if append_of_var2 in raw_inputs:
                    checked = True
                append_var2 += 1
                run_times_checked_boat += 1
                append_of_var2 = (str(posx_let) + str(append_var2))

        if checked is True:
            print("This space is al ready filled!")
            continue
        # Resets
        append_var = posx_let
        append_var2 = boat_pos_input_num
        append_of_var = (str(posx_let) + str(boat_pos_input_num))
        append_of_var2 = (str(posx_let) + str(boat_pos_input_num))
        # inserts raw_input to list so it can be checked
        while strip_boat > run_times_append_boat:
            if hor_or_ver == "y":
                raw_inputs.append(append_of_var)
                append_var += 1
                run_times_append_boat += 1
                append_of_var = (str(append_var) + str(boat_pos_input_num))
            else:
                raw_inputs.append(append_of_var2)
                append_var2 += 1
                run_times_append_boat += 1
                append_of_var2 = (str(posx_let) + str(append_var2))

        if hor_or_ver == "y":
            while strip_boat > run_times_insert_boat:
                grid[boat_pos_input_num].insert(posx_let, boat[run_times_insert_boat])   # adds boat to list horizontal
                run_times_insert_boat += 1

            while strip_boat > run_times_remove:
                grid[boat_pos_input_num].pop(posx_let + len(boat) + run_times_remove)  # removes left spaces
                run_times_remove += 1
            grid[boat_pos_input_num][11] = "-"
        else:
            while strip_boat > run_times_insert_boat:
                grid[ver_boat_pos].insert(posx_let, boat[run_times_insert_boat])   # adds boat to list vertical
                run_times_insert_boat += 1
                ver_boat_pos += 1
            ver_boat_pos = boat_pos_input_num  # resets ver_boat_pos
            while strip_boat > run_times_remove:
                grid[ver_boat_pos].pop(posx_let + 1)  # removes left spaces
                run_times_remove += 1
                ver_boat_pos += 1
        print_grid(grid)
        func_is_over = True


def shot_pos(grid, raw_inputs, grid_missed):
    let_to_num = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    func_is_over = False
    mark = "☉ "
    times_checked = 1
    not_in_grid = 0
    file = open("Txt Wins", "a")

    while func_is_over is False:

        shot_pos_input_let = str(input("Enter the position of the shot from A-J\n"))
        shot_pos_input_num = int(input("Enter the position of the shot from 1-10\n"))
        cap_boat_pos_input_let = shot_pos_input_let.capitalize()
        if cap_boat_pos_input_let not in letters:
            print("Enter a letter from A-J")
            continue
        if shot_pos_input_num <= 0 or shot_pos_input_num >= 11:
            print("Enter a number from 1-10")
            continue
        posx_let = let_to_num[cap_boat_pos_input_let]
        check_of_var = (str(posx_let) + str(shot_pos_input_num))
        # checks if list raw_input has the same position
        if check_of_var in raw_inputs:
            raw_inputs.remove(check_of_var)
            print("Direct impact!")
            mark = "✘ "
        else:
            print("Miss!")
            pass
        append_of_var = (str(posx_let) + str(shot_pos_input_num) + "Shot")
        # inserts raw_input to list so it can be checked
        raw_inputs.append(append_of_var)
        grid[shot_pos_input_num][posx_let] = mark   # adds shot to list
        grid_missed[shot_pos_input_num][posx_let] = mark  # adds shot to list of misses
        while times_checked <= 10:
            if "◼ " not in grid[times_checked]:
                not_in_grid += 1
            if not_in_grid == 10:
                player_won = True
                print("Game")
                if grid == P2_grid:
                    print("P1 Won!")
                    file.write("P1 Won!\n")
                    file.close()
                else:
                    print("P2 Won!")
                    file.write("P2 Won!\n")
                    file.close()
                exit()
            times_checked += 1
        grid[shot_pos_input_num][11] = "+"
        time.sleep(3)
        print_grid(grid_missed)
        func_is_over = True


def place_boats(turn, what_grid, raw_inputs):
    carrier = ["◼ ", "◼ ", "◼ ", "◼ ", "◼ "]
    battleship = ["◼ ", "◼ ", "◼ ", "◼ "]
    cruiser = ["◼ ", "◼ ", "◼ "]
    submarine = ["◼ ", "◼ ", "◼ "]
    destroyer = ["◼ ", "◼ "]
    boat_list = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
    boat_want = 0
    while turn is True:
        end_detect = False
        list_translate_boat = {5: "carrier", 4: "battleship", 3: "cruiser", 2: "submarine", 1: "destroyer"}
        small_space()
        raw_wanted_boat = input("What Boat?\n Carrier = 5\n Battleship = 4\n Cruiser = 3\n Submarine = 3\n Destroyer = 2\n")
        if raw_wanted_boat.isnumeric() is False:
            wanted_boat = raw_wanted_boat.lower()
        else:
            wanted_boat = list_translate_boat.get(int(raw_wanted_boat))
        while end_detect is False:
            if wanted_boat in boat_list:
                if wanted_boat == "carrier":
                    boat_want = carrier
                if wanted_boat == "battleship":
                    boat_want = battleship
                if wanted_boat == "cruiser":
                    boat_want = cruiser
                if wanted_boat == "submarine":
                    boat_want = submarine
                if wanted_boat == "destroyer":
                    boat_want = destroyer
                boat_list.remove(wanted_boat)
                boat_pos(boat_want, what_grid, raw_inputs)
            if not boat_list:
                turn = False
                print("P1: All boats have been placed")
            end_detect = True


place_boats(P1_turn_boats, P1_grid, raw_inputs_P1)
time.sleep(3)
space()
place_boats(P2_turn_boats, P2_grid, raw_inputs_P2)
time.sleep(3)
space()
while fight is True:
    print("P1 Turn")
    print("P1 Boats: ")
    print_grid(P1_grid)
    small_space()
    print("P1 Enemy's board: ")
    print_grid(P1_grid_missed)
    shot_pos(P2_grid, raw_inputs_P2, P1_grid_missed)
    print("P1 Enemy's board after shot: ")
    time.sleep(7)
    space()
    print("P2 Turn")
    print("P2 Boats: ")
    print_grid(P2_grid)
    small_space()
    print("P2 Enemy's board: ")
    print_grid(P2_grid_missed)
    shot_pos(P1_grid, raw_inputs_P1, P2_grid_missed)
    print("P2 Enemy's board after shot: ")
    time.sleep(7)
    space()

# Thx for playing this game!
# No coping and republishing!!
# If you see a bug please report it to me!
# This is my 4th program, 2nd game.
# By Henri Ruben
