import json, os

CONFIG_DIR = "config"
CONFIG_PATH = os.path.join(CONFIG_DIR, "config.json")
DEFAULT_CONFIG_PATH = os.path.join(CONFIG_DIR, "default_config.json")

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return create_default_config()
    
def create_default_config():
    if not os.path.exists(DEFAULT_CONFIG_PATH):
        raise FileNotFoundError("default_config.json ontbreekt!")

    with open(DEFAULT_CONFIG_PATH, 'r', encoding='utf-8') as default_file:
        default_config = json.load(default_file)

    save_config(default_config)
    return default_config

def save_config(config):
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)
