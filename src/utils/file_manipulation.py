import fileinput
from .logging import log_error

def get_file(path):
    try:
        return fileinput.input(path, encoding="utf-8")
    except:
        log_error()
