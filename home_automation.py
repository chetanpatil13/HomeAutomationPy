# MIT License
#
# Copyright (c) 2022 Chetan Patil
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
