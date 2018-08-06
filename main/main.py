import logging 
from logging.handlers import TimedRotatingFileHandler
import sys
from input_pkg.user_input import handle_input


FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")
LOG_FILE = "logs/log_one.log"


def get_console_handler():
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(FORMATTER)
    return h

def get_file_handler():
    h = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    h.setFormatter(FORMATTER)
    return h

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())

    logger.propagate=False
    return logger

logger = get_logger('test logger')


def setup_logger():
    logger = get_logger('test_logger')
    logger.info('Logger setup complete')
    return logger

if __name__ == '__main__':
    logger = setup_logger()
    logger.info('main method running')
    handle_input()

