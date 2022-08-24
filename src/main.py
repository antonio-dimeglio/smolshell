from typing import List

#Constants
EXIT_SUCCESS = 0 
EXIT_FAILURE = 1

def load_config():
    pass 

def parse_line(line:str) -> List[str]:
    
    line = line.replace('\n', '')
    line = line.replace('\r', '')
    line = line.replace('\t', ' ')

    args = line.split(' ')
    return args 

def execute(args:List[str]) -> int:
    pass

def command_loop():
    user_input = input("> ")
    parse_line(line = user_input)
    

def terminate(status:int):
    exit(status) 

def main():
    load_config()
    status = command_loop()
    terminate(status)
    

if __name__ == "__main__":
    main()