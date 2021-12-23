import os
def main():
    try:
        os.system("pip install random")
        print("OS  is installed!")
    except:
        print("Unable to automatically install OS. Please run pip install os in terminal.")
    try:
        os.system("pip install random")
        print("Random is installed! ")
    except:
        print("Random Install Failed! Please do so manually (Run pip install random in your terminal)")
    try:
        os.system("pip install string")
        print("String is installed")
    except:
        print("String Install Failed! Please do so manually (Run pip install string in your terminal)")
    try:
        os.system("pip install alive_progress")
        print("Alive Bar is installed!")
    except:
        print("Alive Progress Install Failed! Please do so manually (Run pip install alive_progress in your terminal)")
def compute():
    for i in range(1):
        ...
        yield main()
from alive_progress import alive_bar

with alive_bar(1) as bar:
    for i in compute():
        bar()