class bcolors:
    RESET = "\033[0m"
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    WHITE = "\033[0;37m"
    BOLD_BLACK = "\033[1;30m"
    BOLD_RED = "\033[1;31m"
    BOLD_GREEN = "\033[1;32m"
    BOLD_YELLOW = "\033[1;33m"
    BOLD_BLUE = "\033[1;34m"
    BOLD_PURPLE = "\033[1;35m"
    BOLD_CYAN = "\033[1;36m"
    BOLD_WHITE = "\033[1;37m"

class LogSpecialMessages:
    def printColor(message:str, color:str):
        print(f'{color}{message}{bcolors.RESET}')

    def info(message:str):
        print(f'{bcolors.BOLD_BLUE}{message}{bcolors.RESET}')

    def debug(message:str):
        print(f'{bcolors.BOLD_BLACK}{message}{bcolors.RESET}')

    def success(message:str):
        print(f'{bcolors.BOLD_GREEN}{message}{bcolors.RESET}')

    def warning(message:str):
        print(f'{bcolors.BOLD_YELLOW}{message}{bcolors.RESET}')

    def error(message:str):
        print(f'{bcolors.BOLD_RED}{message}{bcolors.RESET}')

    def critical(message:str):
        print(f'{bcolors.BOLD_PURPLE}{message}{bcolors.RESET}')
