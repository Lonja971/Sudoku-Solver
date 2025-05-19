import os, time
from config.manager import save_config
from sudoku import Sudoku
from utils.file_utils import list_json_files, load_json_file
from colorama import Fore, Style
from utils.screen_utils import clear_screen, show_title, show_input

def change_speed_menu(config):
   clear_screen()
   show_title("Snelheidsverandering")
   print(f"Huidige snelheid: {config['animation_delay']}")

   while True:
         print("\nVoer de nieuwe snelheid (float) in of `back` om terug te gaan:")
         inp = show_input()
         if inp == "back":
            return
         
         try:
            config["animation_delay"] = float(inp)
            save_config(config)
            print(f"Snelheid bijgewerkt: {config['animation_delay']}")
            time.sleep(2)
            return
         except ValueError:
            print("Ongeldig getal.")

def start_solver(config):
   clear_screen()
   files = list_json_files("boards")
   
   show_title("Een Sudoku-bord kiezen")
   for i, file in enumerate(files):
      print(f"{i + 1}. {file}")
   
   while True:
      # My changes in test branch
      print("\nVoer het bordnummer in of `back`:")
      inp = show_input()
      if inp == "back":
         return
      
      try:
         if 1 <= int(inp) <= len(files):
            sudoku_data = load_json_file(os.path.join(config["boards_json_path"], files[int(inp) - 1]))
            sudoku = Sudoku(size=9, config=config)
            
            if not sudoku.is_valid_sudoku_json(sudoku_data):
               print("Het Sudoku-bord heeft gebreken!")
               continue

            sudoku.set_values(sudoku_data, is_primary=True)
            sudoku.display({"rewrite": True})
            time.sleep(2)
            sudoku.start_decryption()
            return
         else:
             print("Het ingevoerde nummer is onjuist. Probeer het opnieuw.")
      except ValueError:
         print("Onjuist bestandsnummer.")

def unknown_command(*args):
   print("Onbekend actie.")
