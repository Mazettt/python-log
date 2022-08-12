import datetime
import pytz
import glob, os

if __name__ == "__main__":
    from colors import bcolors, LogSpecialMessages
else:
    from .colors import bcolors, LogSpecialMessages

class LogClass:
    """A class to log messages in file and console"""

    def __defaultLogFileName__(self = 0) -> str:
        return "latest.log"

    def __defaultLogFolderPath__(self = 0) -> str:
        return "logs/"

    def getLogFolderPath(self) -> str:
        if (self.__logFolderPath__ == ""):
            return self.__defaultLogFolderPath__()
        else:
            return self.__logFolderPath__

    def setLogFolderPath(self, new:str) -> None:
        if (new != ""):
            if (new[-1] != '/'):
                new += '/'
            self.__logFolderPath__ = new

    def getLogFileName(self) -> str:
        if (self.__logFileName__ == ""):
            return self.getLogFolderPath() + self.__defaultLogFileName__()
        else:
            return self.getLogFolderPath() + self.__logFileName__

    def setLogFileName(self, new:str) -> None:
        if (new != ""):
            self.__logFileName__ = new

    def __init__(self, showInConsole:bool = False, logFileName:str = __defaultLogFileName__(), logFolderPath:str = __defaultLogFolderPath__()) -> None:
        if (logFolderPath != "" and logFolderPath[-1] != '/'):
            logFolderPath += '/'
        self.__showInConsole__ = showInConsole
        self.__logFileName__ = logFileName
        self.__logFolderPath__ = logFolderPath

    def __fileExists__(self, path:str) -> bool:
        return os.path.exists(path)

    def log(self, message:str, log_type:str, color:str = bcolors.RESET) -> None:
        currentTimeZone = pytz.timezone('Europe/Paris')
        log_date = datetime.datetime.now(tz=currentTimeZone).strftime("%Y-%m-%d %H:%M:%S")

        log_type = f'[{log_type.upper()}]'
        log_message = f'{log_date:21}{log_type:11}{message}'

        if not (self.__fileExists__(self.getLogFolderPath())):
            os.mkdir(self.getLogFolderPath())
        with open(self.getLogFileName(), "a") as f:
            f.write(f'{log_message}\n')
        if self.__showInConsole__:
            LogSpecialMessages.printColor(log_message, color)

    def info(self, message:str):
        self.log(message, 'info', bcolors.BOLD_BLUE)
    def debug(self, message:str):
        self.log(message, 'debug', bcolors.BOLD_BLACK)
    def success(self, message:str):
        self.log(message, 'success', bcolors.BOLD_GREEN)
    def warning(self, message:str):
        self.log(message, 'warn', bcolors.BOLD_YELLOW)
    def error(self, message:str):
        self.log(message, 'error', bcolors.BOLD_RED)
    def critical(self, message:str):
        self.log(message, 'crit', bcolors.BOLD_PURPLE)

    def __getLogCreatedDate__(self, path:str) -> str:
        with open(path, 'r') as f:
            firstLine = f.read().split('\n')[0]
            date = firstLine.split(' ')[0] + firstLine.split(' ')[1]
        return date

    def resetLogFile(self) -> None:
        if self.__fileExists__(self.getLogFileName()):
            createdDate = self.__getLogCreatedDate__(self.getLogFileName())
            createdDate = createdDate.replace(':', 'h', 1).replace(':', 'm', 1).replace(' ' ,'_')
            os.rename(self.getLogFileName(), self.getLogFolderPath() + createdDate + ".log")

    def deleteAllLogs(self) -> None:
        for f in glob.glob(self.getLogFolderPath() + "*.log"):
            os.remove(f)

def resetLogFile(logFileName: str = "", logFolderPath: str = "") -> None:
    logObj = LogClass(logFileName=logFileName, logFolderPath=logFolderPath)
    logObj.resetLogFile()

def log(message:str, showInConsole:bool = False, logFileName: str = "", logFolderPath: str = "") -> None:
    logObj = LogClass(showInConsole, logFileName, logFolderPath)
    logObj.log(message, 'log')
def info(message:str, logFileName: str = "", logFolderPath: str = "") -> None:
    logObj = LogClass(True, logFileName, logFolderPath)
    logObj.info(message)
def debug(message:str, logFileName: str = "", logFolderPath: str = "") -> None:
    logObj = LogClass(True, logFileName, logFolderPath)
    logObj.debug(message)
def success(message:str, logFileName: str = "", logFolderPath: str = "") -> None:
    logObj = LogClass(True, logFileName, logFolderPath)
    logObj.success(message)
def warning(message:str, logFileName: str = "", logFolderPath: str = "") -> None:
    logObj = LogClass(True, logFileName, logFolderPath)
    logObj.warning(message)
def error(message:str, logFileName: str = "", logFolderPath: str = "") -> None:
    logObj = LogClass(True, logFileName, logFolderPath)
    logObj.error(message)
def critical(message:str, logFileName: str = "", logFolderPath: str = "") -> None:
    logObj = LogClass(True, logFileName, logFolderPath)
    logObj.critical(message)

if __name__ == "__main__":
    resetLogFile()
    log("log")
    info("info")
    debug("debug")
    success("success")
    warning("warn")
    error("error")
    critical("crit")
