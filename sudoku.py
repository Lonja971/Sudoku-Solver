from colorama import Fore, Style
import os, time, sys
from utils.screen_utils import show_input

class Sudoku:
    def __init__(self, size=9, config=None):
        self.size = size
        self.board = [
            [
                {"num": 0, "options": [], "tried_options": [], "primary": False} for _ in range(size)
            ]
            for _ in range(size)
        ]
        self.all_sudoku_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.current_point = {"row": 0, "col": 0}
        self.is_finished = False
        self.result = None
        self.attempts_number = 0
        self.animation_delay = config.get("animation_delay", 0.05)

    def display(self, param):
        if param["rewrite"]:
            os.system("cls" if os.name == "nt" else "clear")

        block_size = int(self.size ** 0.5)
        for i, row in enumerate(self.board):
            row_display = ""
            for j, cell in enumerate(row):
                value = cell["num"]
                if value == 0:
                    cell_str = Fore.WHITE + "•"
                else:
                    if cell["primary"]:
                        cell_str = Fore.CYAN + str(value)
                    else:
                        cell_str = Fore.GREEN + str(value)

                row_display += cell_str + " " + Style.RESET_ALL
                if (j + 1) % block_size == 0 and j + 1 < self.size:
                    row_display += Fore.WHITE + "| " + Style.RESET_ALL
            print(row_display.strip())

            if (i + 1) % block_size == 0 and i + 1 < self.size:
                print(Fore.WHITE + "-" * (self.size * 2 + block_size) + Style.RESET_ALL)

    def display_result(self):
         if (not self.result):
            print(f"\n\n{Fore.RED}There are no results yet.{Style.RESET_ALL}")
            return

         color_map = {
            "green": Fore.GREEN,
            "yellow": Fore.YELLOW,
            "red": Fore.RED
         }
         color = color_map.get(self.result["color"], Fore.WHITE)

         print(f"\n\n{color}{self.result['message']}{Style.RESET_ALL}")
         print(f"Aantal iteraties: {color}{self.result['attempts']}{Style.RESET_ALL}\n")

         while True:
            print("Om terug te keren naar het hoofdmenu, schrijf je `back`")
            inp = show_input()
            if inp == "back":
               return

    def update_cell(self, row, col):
        block_size = int(self.size ** 0.5)
        cell = self.board[row][col]
        value = cell["num"]

        cursor_row = row + (row // block_size)
        cursor_col = col * 2 + (col // block_size) * 2

        if value == 0:
            cell_str = Fore.WHITE + "•"
        else:
            cell_str = (Fore.CYAN if cell["primary"] else Fore.GREEN) + str(value)

        sys.stdout.write(f"\033[{cursor_row + 1};{cursor_col + 1}H{cell_str} {Style.RESET_ALL}")
        sys.stdout.flush()

    def set_values(self, values, is_primary=False):
        for value in values:
            if 0 <= value["row"] < self.size and 0 <= value["col"] < self.size:
                self.board[value["row"]][value["col"]]["num"] = value["num"]

                if value.get("options"):
                    self.board[value["row"]][value["col"]]["options"] = value["options"]
                    print(self.board[value["row"]][value["col"]]["options"])

                if is_primary == True:
                    self.board[value["row"]][value["col"]]["primary"] = is_primary

            else:
                raise ValueError("Row and column must be within the board size.")

    def set_options(self, row, col, options):
        if 0 <= row < self.size and 0 <= col < self.size:
            self.board[row][col]["options"] = options
        else:
            raise ValueError("Row and column must be within the board size.")
        
    def set_current_point(self, which="next"):
        if which == "next":
            if self.board[self.current_point["row"]][self.current_point["col"]]["num"] != 0:
                is_next_point = False
                current_point_data = {"row": self.current_point["row"], "col": self.current_point["col"]}
                while is_next_point == False:
                    current_point_data["col"] += 1

                    if len(self.board[current_point_data["row"]]) <= current_point_data["col"]:
                        current_point_data["row"] += 1
                        current_point_data["col"] = 0
                        
                        if len(self.board) <= current_point_data["row"]:
                            self.is_finished = True
                            is_next_point = True

                    if self.is_finished != True and self.board[current_point_data["row"]][current_point_data["col"]]["num"] == 0:
                        self.current_point["row"] = current_point_data["row"]
                        self.current_point["col"] = current_point_data["col"]
                        is_next_point = True
        
        elif which == "previous":
            is_previos_point = False
            current_point_data = {"row": self.current_point["row"], "col": self.current_point["col"]}

            while is_previos_point == False:
                current_point_data["col"] -= 1

                if current_point_data["col"] < 0:
                    current_point_data["row"] -= 1
                    current_point_data["col"] = len(self.board[current_point_data["row"]]) - 1 

                if current_point_data["row"] < 0:
                    print("Досягнуто межу початку дошки!")
                    break

                if self.board[current_point_data["row"]][current_point_data["col"]]["primary"] != True:
                    self.current_point["row"] = current_point_data["row"]
                    self.current_point["col"] = current_point_data["col"]
                    is_previos_point = True

        else:
            print(f"An error has occurred! Invalid type in set_current_point! You specified: {which}")

    def row_analysis(self, row, only_primary=True):
        result = []

        for point in self.board[row]:
            if point["primary"] == True or only_primary != True:
                result.append(point["num"])

        return result
    
    def col_analysis(self, col, only_primary=True):
        result = []

        for row in self.board:
            if row[col]["primary"] == True or only_primary != True:
                result.append(row[col]["num"])

        return result
    
    def square_analysis(self, row, col, only_primary=True):
        block_size = int(self.size ** 0.5)

        start_row = (row // block_size) * block_size
        start_col = (col // block_size) * block_size

        result = []

        for r in range(start_row, start_row + block_size):
            for c in range(start_col, start_col + block_size):
                if self.board[r][c]["primary"] == True or only_primary != True:
                    result.append(self.board[r][c]["num"])

        return result
    
    def set_point_options(self, row, col, only_primary=True):
        point = self.board[row][col]

        if point["primary"] != True:
            all_point_options = self.all_sudoku_numbers

            row_result = self.row_analysis(row, only_primary)
            col_result = self.col_analysis(col, only_primary)
            square_result = self.square_analysis(row, col, only_primary)

            excluded_numbers = set(row_result + col_result + square_result)
            all_point_options = [num for num in all_point_options if num not in excluded_numbers]

            return all_point_options  

    def set_all_options(self):
        for row_index, row in enumerate(self.board):
            for col_index, point in enumerate(row):
                all_point_options = self.set_point_options(row_index, col_index)   
                self.board[row_index][col_index]["options"] = all_point_options

    def delete_point_data(self, row, col):
        if self.board[row][col]["primary"] != True:
            self.board[row][col]["num"] = 0
            self.board[row][col]["tried_options"] = []

    def find_value(self):
        current_row = self.current_point["row"]
        current_col = self.current_point["col"]
        current_point = self.board[current_row][current_col]

        if current_point["primary"] != True:
            is_new_option = False
            current_option_index = 0
            all_point_options = self.set_point_options(current_row, current_col, False)

            while is_new_option == False:
                if current_option_index < len(all_point_options):
                    if all_point_options[current_option_index] not in current_point["tried_options"]:
                        self.board[current_row][current_col]["num"] = all_point_options[current_option_index]
                        self.board[current_row][current_col]["tried_options"].append(all_point_options[current_option_index])
                        self.set_current_point("next")
                        is_new_option = True
                    else:
                        current_option_index += 1
                else:
                    self.delete_point_data(current_row, current_col)
                    self.set_current_point("previous")
                    is_new_option = True

            self.update_cell(current_row, current_col)
            self.attempts_number += 1
            time.sleep(self.animation_delay)
    
    def start_decryption(self):
        self.set_all_options()
        self.set_current_point("next")

        while self.is_finished == False:
            self.find_value()


        if self.attempts_number < 500:
            message = "Ha, makkelijk! (～￣▽￣)～"
            color = "green"
        elif 500 <= self.attempts_number < 1000:
            message = "Haha, een goede warming-up!"
            color = "yellow"
        else:
            message = f"Ha, makkelijk, ik heb het in slechts {self.attempts_number} pogingen gedaan, STOP, HOEVEEL???"
            color = "red"

        self.result = {
            "attempts": self.attempts_number,
            "message": message,
            "color": color
        }

        self.display_result()
