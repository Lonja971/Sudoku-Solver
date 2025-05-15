import os

def show_title(title):
   return print(f"=== {title} ===")

def show_input():
    return input("> ").strip().lower()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_program(config):
   print("Tot ziens!")
   exit()