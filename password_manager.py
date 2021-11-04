from os import makedirs


user = input("What's your name? ")

def mode():
    mode = input("Would you like to view or add password? ")
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please try again.")

def view():
    with open('pwd.txt', 'r') as f:
        for line in f.readlines():
            print(line)

def add():
    name = input("Enter your name/username/number/email: ")
    type = input("Type of account: ")
    pwd = input("Password: ")

    with open('pwd.txt', 'a') as f:
        f.write(name + "|" + type + "|" + pwd + "\n")
while True:
    masterpass = input("Hi " + user + "!" + " Enter the master password to have an access: ")
    if masterpass == "gemini":
       mode()
    else:
        print("You entered the wrong master password.")
        continue