import json
from termcolor import colored

with open('src/tools/errors.json', 'r') as f:
    errors = json.load(f)

def str_hex(string):
    if isinstance(string, str):
        return string.encode().hex()
    else:
        raise TypeError(colored(errors["TypeError"]["msg"], "red"))
    
def int_hex(integer):
    if isinstance(integer, int):
        return hex(integer)
    else:
        raise TypeError(colored(errors["TypeError"]["msg"], "red"))
    

    