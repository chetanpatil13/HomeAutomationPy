class MainMenu:
    def __init__(self):
        self.room_number = None

    def show_menu(self):
        print("\nSelect the room ::")
        print("0. To exit")
        print("1. Hall")
        print("2. Kitchen")
        print("3. Master Bedroom")
        print("4. Second Bedroom")
        self.room_number = int(input())


class Rooms(MainMenu):
    def __init__(self):
        self.option = None
        self.appliance = {}
        super().__init__()

    def status(self):
        y = 1
        print("")
        for key in self.appliance:
            print(f"{y}. {key} :: {self.appliance[key]}")
            y += 1
        self.option = int(input("Choose number to control or enter 0 to exit to main menu :: "))

    def control(self):
        if self.option == 0:
            return self.option
        elif 1 <= self.option <= len(list(self.appliance.keys())):
            key = list(self.appliance.keys())[self.option - 1]
            if self.appliance[key] == "OFF":
                self.appliance[key] = "ON"
            elif self.appliance[key] == "ON":
                self.appliance[key] = "OFF"
            return 1
        else:
            return -1


class Hall(Rooms):
    def __init__(self):
        Rooms().__init__()
        self.appliance = {
            'TV': "OFF",
            'AC': "OFF",
            'FAN1': "OFF",
            'FAN2': "OFF",
            'LIGHT1': "OFF",
            'LIGHT2': "OFF"}


class Kitchen(Rooms):
    def __init__(self):
        super().__init__()
        self.appliance = {
            'FAN': "OFF",
            'LIGHT': "OFF",
            'CHIMNEY': "OFF"}


class MasterBedroom(Rooms):
    def __init__(self):
        super().__init__()
        self.appliance = {
            'TV': "OFF",
            'FAN': "OFF",
            'LIGHT': "OFF",
            'AC': "OFF"}


class SecondBedroom(Rooms):
    def __init__(self):
        super().__init__()
        self.appliance = {
            'FAN': "OFF",
            'LIGHT': "OFF",
            'AC': "OFF"}
