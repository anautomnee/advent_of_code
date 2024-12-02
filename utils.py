import os

def read_input(filepath, filename: str = "input.txt") -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, filepath, filename)) as file:
        input = file.read()
    return input