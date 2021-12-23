import os
import random
import string
print("Welcome to Password Generator!")
print("Made by Marve")
print("Loading... ")
def checker():
  print("Checking Requirements...")
  try:
    os.system("setup.bat")
    os.system("reqcheck.py")  
  except:
    print("Not Windows. Trying Linux")
    try:
      os.system("setup.sh")
      os.system("reqcheck.py") 
    except:
      print("Unable to install requirements! Unknown Error Occured ")
checker()
print("-----------------------------------------------------------------------------------------------------------------")
length = int(input("Enter the length of the password you want (Recommended: 16): "))
a1 = input("Do you want numbers in your password? Y/N: ")
a2 = input("Do you want symbols in your password? Y/N: ")
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
if a1 == "y":
    if a2 == "n":
      c1 = lower + upper + numbers
      c2 = random.sample(c1, length)
      password = "".join(c2)
      print("Password: " + password)
      g1 = input("Save to file? (Recommeded so you don't forget) Y/N: ")
      if g1 == "y":
        f =  open("Passwords.txt", "w")
        f.write("\n" + password)
        f.close()
        print("Password saved to Passwords.txt")
      if g1 == "n":
          print("Not saving to file.")
if a1 == "y":
    if a2 == "y":
      b1 = lower + upper + numbers + symbols
      b2 = random.sample(b1, length)
      password = "".join(b2)
      print("Password: " + password)
      h1 = input("Save to file? (Recommeded so you don't forget) Y/N: ")
      if h1 == "y" or "Y":
        f =  open("Passwords.txt", "a")
        f.write("\n" + password)
        f.close()
        print("Password saved to Passwords.txt")
      if h1 == "n":
          print("Not saving to file.")
if a1 == "n":
    if a2 == "y":
      d1 = lower + upper + symbols
      d2 = random.sample(d1, length)
      password = "".join(d2)
      print("Password: " + password)
      n1 = input("Save to file? (Recommeded so you don't forget) Y/N: ")
      if n1 == "y":
        f =  open("Passwords.txt", "w")
        f.write("\n" + password)
        f.close()
        print("Password saved to Passwords.txt")
      if n1 == "n":
          print("Not saving to file.")
input("Press any key to exit")