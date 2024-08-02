from LibraryMenu import menu
from LibraryAdd import addbook
from LibraryDelete import deletebook
from LibraryUpdata import bookupdate
from LibraryView import viewbook,viewallbooks
while(True):
    menu()
    try:
        ch=int(input("Enter your choice:"))
        match(ch):
            case 1:
                addbook()
            case 2:
                deletebook()
            case 3:
                bookupdate()
            case 4:
                viewbook()
            case 5:
                viewallbooks()
            case 6:
                print("-"*50)
                print("****Thanks for using this APP.****")
                print("-" * 50)
                break
            case _:
                print("Invalid choice...Please try again")
    except ValueError:
        print("\tDon't enter str,symbol for integer choice..try again..")