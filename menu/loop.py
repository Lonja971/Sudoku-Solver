import time
from menu.routes import COMMANDS
from colorama import Fore, Style
from utils.screen_utils import clear_screen
from utils.screen_utils import show_title, show_input

def main_menu_loop(config):
   name = config["project"].get("name", "Sudoku Solver")
   version = config["project"].get("version", "")
   version_str = f" v{version}" if version else ""

   while True:
      clear_screen()
      show_title(f"{name}{version_str}")
      print("\nBeschikbare commando's:")
      for cmd in COMMANDS:
         print(f"  {cmd}")

      print("\nVoer de actie in")
      action = show_input()
      handler = COMMANDS.get(action)
      if handler:
            handler(config)
      else:
         print(f"{Fore.RED}Onbekende actie.{Style.RESET_ALL}")
         time.sleep(2)
