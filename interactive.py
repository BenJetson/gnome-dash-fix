#!/usr/bin/python3

import os
import sys

if sys.version_info < (3,0):
    print("""ERROR: Python 3 is required to run this script.

Is python3 installed? Try running the script
as 'python3 interactive.py' instead.

If this doesn't work, you may need to install
the Python 3 interpreter from GNOME Software.

Exiting.""")
    sys.exit(1)

class Folder:
    def __init__(self, name, categories):
        self.title = name
        self.name = "".join(i for i in name.lower() if i.isalnum())
        self.categories = ""

        for cat in categories:
            self.categories += "'{}', ".format(cat)

        self.categories = "[" + self.categories[:-2] + "]"


def ynQuery(question):
    while True:
        print()
        print(question)
        choice = input("[y/n] >>> ")

        if choice.isalpha():
            if choice.lower() == "y":
                return True
            elif choice.lower() == "n":
                return False

        print("ERROR: Invalid choice.")


def menu():
    while True:
        print()
        print("""---Main Menu---
        1. Set folders to default categories.
        2. Customize folders and categories before applying.
        3. Remove all existing folders from dashboard.
        4. Cancel and exit.""")
        print()

        choice = input("What do you want to do? >>> ")

        if choice.isnumeric() and int(choice) in range(1, 5):
            return int(choice)
        else:
            os.system("clear")
            for i in range(2): print()
            print("ERROR: Invalid choice.")


def doReset():
    os.system("gsettings reset-recursively org.gnome.desktop.app-folders")


def resetAll():
    os.system("clear")
    for i in range(2): print()
    print("""WARNING! This will erase ALL folders you have
    in your apps dashboard and return all apps
    to an unsorted state. 

    This includes user-created folders as well as
    any created by this script or other means.""")

    if ynQuery("Are you sure you wish to do this?"):
        os.system("clear")
        for i in range(2): print()
        doReset()
        print("Your apps dashboard is now free of all folders.")
    else:
        print("Reset not performed. Exiting.")
        sys.exit()


def writeSettings(inputArray):
    masterList = ""

    for item in inputArray:
        masterList += "'{}', ".format(item.name)

    masterList = "[" + masterList[:-2] + "]"

    os.system("gsettings set org.gnome.desktop.app-folders folder-children \"{}\"".format(masterList))

    for item in inputArray:
        os.system(
            "gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/{}/ name \"{}\"".format(
                item.name, item.title))
        os.system(
            "gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/{}/ categories \"{}\"".format(
                item.name, item.categories))


def setSorted():
    os.system("clear")
    for i in range(2): print()
    print("""WARNING! This will erase ALL folders you have
        in your apps dashboard and sort your apps
        based upon a predefined set of basic
        categories. 

        The folders erased will include user-created
        folders as well as any created by other means.""")

    if ynQuery("Are you sure you wish to do this?"):
        print()
        doReset()
        writeSettings([Folder("Accessories", ['Utility']),
                       Folder("Chrome Apps", ['chrome-apps']),
                       Folder("Games", ['Game']),
                       Folder("Graphics", ['Graphics']),
                       Folder("Internet", ['Network', 'WebBrowser', 'Email']),
                       Folder("Office", ['Office']),
                       Folder("Programming", ['Development']),
                       Folder("Science", ['Science']),
                       Folder("Sound & Video", ['AudioVideo', 'Audio', 'Video']),
                       Folder("System Tools", ['System', 'Settings']),
                       Folder("Universal Access", ['Accessibility']),
                       Folder("Wine", ['Wine', 'Wine-Programs-Accessories'])])
        os.system("clear")
        for i in range(2): print()
        print("Your apps dashboard is now sorted by the predefined categories.")
    else:
        print()
        print("Sort not performed. Exiting.")
        sys.exit()

def listCats(cats):
    print("Your current folders are:")

    for i in range(len(cats)):
        print()
        print("{}. TITLE:      {}".format(i + 1, cats[i].title))
        print("    CATEGORIES: {}".format(cats[i].categories[1:-1]))

def editMenu():
    while True:
        for i in range(2): print()
        print("""--Edit Menu--
        ** You may need to scroll to view all current folders.
        1. Add a new folder
        2. Delete an existing folder
        3. Delete all existing folders
        4. Finished editing, write to disk""")

        choice = input("What do you want to do? >>> ")

        if choice.isnumeric() and int(choice) in range(1,5):
            if int(choice) == 1:
                return "add"
            elif int(choice) == 2:
                return "delete"
            elif int(choice) == 3:
                return "delete-all"
            elif int(choice) == 4:
                return "done"
        else:
            print("ERROR: Invalid choice.")

def addFolder():
    print("Enter a folder title.")
    title = input(">>> ")

    adding = True
    cats = []

    while adding:
        print()
        print("Current categories: {}".format(cats))
        print("""Enter text to add a category.
To remove previous, type 'r'
To remove all, type 'x'
When done, type 'q'""")
        userinput = input(">>> ")
        if userinput == "q":
            adding = False
        elif userinput == 'r':
            cats.remove(cats[-1])
        elif userinput == 'x':
            cats = []
        else:
            cats.append(userinput)

    return Folder(title, cats)


def removeFolder(folders):
    while True:
        if len(folders) > 0:
            print("Enter the number of the folder you wish to remove.")
            userinput = input(">>> ")

            if userinput.isnumeric() and int(userinput) in range(1, len(folders)+1):
                return folders[int(userinput) - 1]
            else:
                print("ERROR: Invalid choice.")
        else:
            print("ERROR! No folders left to delete.")
            return -1



def customBuild():

    os.system("clear")

    userFolders = [Folder("Accessories", ['Utility']),
                   Folder("Chrome Apps", ['chrome-apps']),
                   Folder("Games", ['Game']),
                   Folder("Graphics", ['Graphics']),
                   Folder("Internet", ['Network', 'WebBrowser', 'Email']),
                   Folder("Office", ['Office']),
                   Folder("Programming", ['Development']),
                   Folder("Science", ['Science']),
                   Folder("Sound & Video", ['AudioVideo', 'Audio', 'Video']),
                   Folder("System Tools", ['System', 'Settings']),
                   Folder("Universal Access", ['Accessibility']),
                   Folder("Wine", ['Wine', 'Wine-Programs-Accessories'])]

    for i in range(2): print()
    print("The default folders are preloaded and will be listed for you.")
    print("After listing all preloads, you will be given the opportunity to edit.")
    print("** You might want to maximize your terminal window to get a better view.")
    print()
    input("PRESS RETURN TO CONTINUE... ")

    stillEditing = True

    while stillEditing:
        os.system("clear")
        for x in range(2): print()
        listCats(userFolders)
        choice = editMenu()

        if choice == "add":
            userFolders.append(addFolder())
        elif choice == "delete":
            deleteChoice = removeFolder(userFolders)
            if deleteChoice != -1:
                userFolders.remove(deleteChoice)
        elif choice == "delete-all":
            if ynQuery("Really delete all existing folders?"):
                userFolders = []
            else:
                print("Cancelled.")
        elif choice == "done":
            if len(userFolders) == 0:
                os.system("clear")
                for i in range(2): print()
                print("ERROR: You must have at least one folder.")
                print("To delete all, use reset function in main menu.")
                print("Exiting.")
                sys.exit()

            os.system("clear")
            listCats(userFolders)
            if ynQuery("""
-------------------------------------------------

Please confirm that your categories are correctly
formatted before continuing. Failing to do so may
cause damage to your system configuration.
Make sure there aren't any duplicate entries
or misspellings.

Furthermore, be mindful that any previously created
folders, by user or other means will be permanently
erased and replaced with the configuration here.

Are you sure the information above is correct and that
you want to write these changes to disk?"""):
                stillEditing = False


    doReset()
    writeSettings(userFolders)
    os.system("clear")
    for i in range(2): print()
    print("Changes written to disk.")







# Main code execution begins below this line.

os.system("clear")
for i in range(2): print()
print("""GNOME DASH FIX
Copyright (c) 2017 Ben Godfrey

Welcome! This script can help you organize
your GNOME Apps Dashboard into categories.""")
print()
input("PRESS RETURN TO BEGIN...")

os.system("clear")
for i in range(2): print()
print("""This software is currently in beta and may
not function as intended. You use this software
at your own risk -- you are responsible for
any damages that occur.

This software is licensed under the MIT License.
For full license terms, see the project's
GitHub page (https://github.com/benjetson/gnome-dash-fix)
""")
if not ynQuery("Do you agree to the terms and conditions?"):
    for i in range(2): print()
    print("ERROR: You cannot run this software without agreeing to the terms.")

os.system("clear")
choice = menu()

if choice == 1:
    setSorted()
elif choice == 2:
    customBuild()
    #print("Sorry! This feature is currently planned, but not yet implemented.")
elif choice == 3:
    resetAll()
elif choice == 4:
    print("Goodbye.")
    sys.exit()