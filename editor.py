import sys  #contains system-level information, such as the version of Python you're running
import os
import shutil  #shutil module helps you automate copying files and directories

# created by prabhat #

def leave():
    sys.exit("You are leaving CUI Text Editor: ")


def read():
    try:
        filename = raw_input("Enter file name: ")
        with open(filename, "r") as target:
            print(target.read())
    except Exception as e:
        print("There was a problem: {0}" .format(e))


def delete():
    filename = raw_input("Enter file name: ")
    try:
        os.unlink(filename)
        print("File hasbeen deleted")
    except Exception as e:
        print("There was a problem: {0}" .format(e))


def write():
    try:
        filename = raw_input("Enter file name: ")
        with open(filename, "a") as target:
            while True:
                append = raw_input()
                if append.lower() == "menu":
                    break
                target.write(append)
                target.write("\n")
            
    except Exception as e:
        print("There was a problem: {0}" .format(e))


def cwd():
    try:
        print(os.getcwd())
        change = raw_input("Change Y/N: ")
        if change.startswith("Y"):
            path = raw_input("New CWD: ")
            os.chdir(path)
            print("Path hasbeen Changed Successfully")
    except Exception as e:
        print("There was a problem: {0}" .format(e))


def rename():
    try:
        filename = raw_input("Enter current file name: ")
        new = raw_input("Enter new file name: ")
        shutil.move(filename, new)
        print("File hasbeen rename Successfully")
    except Exception as e:
        print("There was a problem: {0}" .format(e))

while True:           ##while loop will run as long as the conditional expression evaluates to True
    print("Options: write, read, cwd, exit, delete, rename")
    do = raw_input("So, what are you wishing for today: ")
    if do.lower() == "write":
        write()
    elif do.lower() == "read":
        read()
    elif do.lower() == "delete":
        delete()
    elif do.lower() == "exit":
        leave()
    elif do.lower() == "cwd":
        cwd()
    elif do.lower() == "rename":
        rename()
    else:
        print("#You Entered wrong Input Dear#")