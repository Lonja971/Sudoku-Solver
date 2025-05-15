from colorama import init
from config.manager import load_config
from menu.loop import main_menu_loop

def main():
    init()
    config = load_config()
    main_menu_loop(config)

if __name__ == "__main__":
    main()