import datetime
from email import message
import pytz
import glob, os

class Log:
    """A class to log messages in file and console"""

    def __defaultLogFileName__() -> str:
        return "latest.log"

    def __defaultLogFolderPath__() -> str:
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
        self.__showInConsole__ = showInConsole
        self.__logFileName__ = logFileName
        self.__logFolderPath__ = logFolderPath

    def __fileExists__(self, path:str) -> bool:
        return os.path.exists(path)

    def log(self, message:str, showInconsole:bool = False) -> None:

        currentTimeZone = pytz.timezone('Europe/Paris')
        log_date = datetime.datetime.now(tz=currentTimeZone).strftime("%Y-%m-%d %H:%M:%S\t")

        if not (self.__fileExists__(self.getLogFolderPath())):
            os.mkdir(self.getLogFolderPath())
        with open(self.getLogFileName(), "a") as f:
            f.write(log_date + message + '\n')
        if self.__showInConsole__ or showInconsole:
            print(log_date + message)

    def __getLogCreatedDate__(self, path:str) -> str:
        with open(path, 'r') as f:
            firstLine = f.read().split('\n')[0]
            date = firstLine.split('\t')[0]
        return date

    def resetLogFile(self) -> None:
        if self.__fileExists__(self.getLogFileName()):
            createdDate = self.__getLogCreatedDate__(self.getLogFileName())
            createdDate = createdDate.replace(':', 'h', 1).replace(':', 'm', 1).replace(' ' ,'_')
            os.rename(self.getLogFileName(), self.getLogFolderPath() + createdDate + ".log")

    def deleteAllLogs(self) -> None:
        for f in glob.glob(self.getLogFolderPath() + "*.log"):
            os.remove(f)

if __name__ == "__main__":
    log = Log()
    log.resetLogFile()
    for i in range(5):
        log.log("oui")
