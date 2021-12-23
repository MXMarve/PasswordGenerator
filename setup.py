import os
def main():
    try:
        import os
        print("OS  is installed!")
    except ImportError:
        raise RuntimeError("Unable to automatically install OS. Please run pip install OS in terminal.")
    try:
        import random
        print("Random is installed! ")
    except ImportError:
        raise RuntimeError("Random not installed! Installing Now... ")
        os.system("pip install random")
    try:
        import string
        print("String is installed")
    except ImportError:
        raise RuntimeError("String is not installed! Installing Now... ")
        os.system("pip install string")
def compute():
    for i in range(1):
        ...
        yield main()
from alive_progress import alive_bar

with alive_bar(1) as bar:
    for i in compute():
        bar()