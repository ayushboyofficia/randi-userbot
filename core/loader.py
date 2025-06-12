import os
import importlib

def load_modules():
    for module in os.listdir("modules"):
        if module.endswith(".py") and not module.startswith("__"):
            importlib.import_module(f"modules.{module[:-3]}")
