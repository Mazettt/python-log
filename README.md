<h1 align="center">Python Log</h1>

A python module to log some messages easily into a file and in the console with helpful colors.

> Started august, 10 2022

## Requirements

- python3

## Install

```sh
cd root_of_your_project
[ -d .git ] && git submodule add https://github.com/Mazettt/python-log.git log || git clone https://github.com/Mazettt/python-log.git log
pip install -r log/requirements.txt
```

## Usage

First import it:
```py
import log.src.log as log
```

Then log your first message:
```py
# note: by default, it doesn't show the message in console
log.log("message")
# to show in console:
log.log("message", True)
```

There is also a set of different colored messages:
```py
# note: these functions print the message in the console by default
log.info("message")     # blue
log.debug("message")    # grey
log.success("message")  # green
log.warning("message")  # yellow
log.error("message")    # red
log.critical("message") # purple
```

By default, the log file is located in ./logs folder and is named "latest.log":
```sh
.
├── main.py         # your code
├── log             # log module
└── logs            # logs folder
    └── latest.log  # log file
```

But you can change it:
```py
log.log("message", logFileName="new.log", logFolderPath="my_logs")
```

If you want to reset your log file and keep a backup of the current one:
```py
log.resetLogFile()
# note: if you have changed the default file or folder name, you need to specify it:
log.resetLogFile(logFileName="new.log", logFolderPath="my_logs")
```
Now:
```sh
.
├── main.py                         # your code
├── log                             # log module
└── logs                            # logs folder
    └── 2022-12-31_08h44m01.log     # backup of latest.log
    └── latest.log                  # is now empty
```

Another way to use it is to declare an object that will always remember your settings, so you don't have to worry about specifiing it in the functions:
```py
myLog = log.LogClass(logFileName="new.log", logFolderPath="my_logs", showInConsole=True)
myLog.log("message")
myLog.resetLogFile()
```

***

## Authors

👤 **Martin d'Hérouville**

* Github: [@Mazettt](https://github.com/Mazettt)
* LinkedIn: [@martin-d-herouville](https://linkedin.com/in/martin-d-herouville)
