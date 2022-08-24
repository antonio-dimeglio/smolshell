import json
import os
from termcolor import colored

#Constants
EXIT_SUCCESS = 0 
EXIT_FAILURE = -1
BUILTINS = ["ls", "cd", "help", "exit"]

#Global variables 
configs = {}
current_dir = ""
current_status = 0

#Bultin commands 
def listing():
    content = [f for f in os.listdir('.')]
    
    print(f"> Current directory: {os.getcwd()}")
    for f in content:
        color = "white"

        if os.path.isdir(f):
            color = "green"
        if os.path.isfile(f):
            color = "blue"

        print(f"> {colored(f, color)}")

def change_dir(path:str):
    try:
        os.chdir(path)
        current_dir = os.getcwd()
    except FileNotFoundError:
        print("> " + colored(f"Could not find folder at path {path}", "red"))
    except PermissionError:
        print("> " + colored(f"Could not access folder at path {path} due to permission error", "red"))
    except NotADirectoryError:
        print("> " + colored(f"Path {path} is not a directory", "red"))

def console_help():
    b = ", ".join(BUILTINS)
    print(f"> Built-in supported commands: {b}")

#Program functions
def load_config() -> dict:
    # The config file is used to map all (implemented) tools 
    # to a precise .py file and to also set up some variables
    # such as current_dir
    with open('./map.json') as f:
        data = json.load(f)
    configs = data

    current_dir = os.getcwd()

def parse_line(line:str) -> list[str]:
    # This function is used to perform a very basic line parsing to split 
    # all the args onto a list 
    line = line.replace('\n', '')
    line = line.replace('\r', '')
    line = line.replace('\t', ' ')

    args = line.split(' ')
    return args 

def execute(args:list[str]) -> int:
    
    match args[0]:

        case "ls":
            listing()
        case "cd":
            change_dir(path=args[1])
        case "help":
            console_help()
        case "exit":
            terminate()
        case _:
            print("TODO")


def terminate():
    print(f"Terminated with status {current_status}")
    exit(current_status)

def command_loop():
    try:

        while True:
            user_input = input("> ")
            args = parse_line(line=user_input)
            execute(args=args)

            if current_status != EXIT_SUCCESS:
                terminate()

    except KeyboardInterrupt:
        print()
        exit()

def main():
    #Main console loop
    load_config()
    command_loop()

if __name__ == "__main__":
    main()