def main():
    try:
        import os
        print("OS Installed")
    except:
        print("Requirement not met! OS Not Installed!")
    try:
        import random
        print("Random Installed")
    except:
        print("Requirement not met! Random Not Installed!")
    try:
        import string
        print("String Installed")
    except:
        print("Requirement not met! String Not Installed!")
    try:
        import alive_progress
        print("Alive Progress Installed")
    except:
        print("Requirement not met! Alive Progress Not Installed!")
main()