import logging # Imports Python's built-in logging module – This allows us to record messages (info, warnings, errors) to a file or console
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #Creates a unique log file name based on the current date and time
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) #os.getcwd() → gets the current working directory and os.path.join(...) → safely joins folder names to build the path
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH =os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
# | Part            | Meaning                              |
# | --------------- | ------------------------------------ |
# | `%(asctime)s`   | Time when the log was recorded       |
# | `%(lineno)d`    | Line number where logging was called |
# | `%(name)s`      | Name of the logger/module            |
# | `%(levelname)s` | INFO, DEBUG, WARNING, ERROR, etc.    |
# | `%(message)s`   | The actual message you write         |

    level=logging.INFO,

)

