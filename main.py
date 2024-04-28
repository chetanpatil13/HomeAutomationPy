# Project :: Home Automation
# Date    :: 25 April 2024
# Author  :: Chetan Patil

from home_automation import MainMenu, Hall, Kitchen, MasterBedroom, SecondBedroom


def main():
    print("Welcome to Home Automation !!!")
    menu = MainMenu()
    hall = Hall()
    kitchen = Kitchen()
    master_bedroom = MasterBedroom()
    second_bedroom = SecondBedroom()

    rooms = [hall, kitchen, master_bedroom, second_bedroom]

    while True:
        menu.show_menu()
        if menu.room_number == 0:
            break
        elif not (1 <= menu.room_number <= len(rooms)):
            print("\nInvalid entry, please enter correct number !!!")
        else:
            while True:
                rooms[menu.room_number - 1].status()
                option = rooms[menu.room_number-1].control()

                if option == 0:
                    break
                elif option == -1:
                    print("\nInvalid entry, please enter correct number !!!")


if __name__ == '__main__':
    main()







