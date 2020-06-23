import fileinput
import os

from aeroflot import Aeroflot

from validators import validate_number, validate_string


def validate_is_all_correct(words):
    is_correct = True
    dict = {0: words[0], 1: words[1]}
    for i in dict:
        if not validate_string(dict.get(i)):
            print(dict.get(i) + "is incorrect")
            is_correct = False
    dict = {0: words[2], 1: words[3], 2: words[4]}
    for i in dict:
        if not validate_number(dict.get(i)):
            print(dict.get(i) + " is incorrect")
            is_correct = False

    return is_correct


class AeroflotCollection:

    def __init__(self, name_of_file):
        self.name_of_file = name_of_file
        self.aeroflot_list = self.read_file(name_of_file)

    def add_to_file(self, o):
        file = open(self.name_of_file, 'a+')
        if os.stat(self.name_of_file).st_size != 0:
            file.write('\n')

        file.write(o.destination + ' ')
        file.write(o.departure + ' ')
        file.write(str(o.flight_number) + ' ')
        file.write(str(o.capacity) + ' ')
        file.write(str(o.price) + ' ')

    def is_list_empty(self):
        return len(self.aeroflot_list) == 0

    def sort_by(self):
        while True:
            print(
                "please select by which criteria you want to sort(destination, departure, flight_number, capacity, price): ")
            value = input()
            if hasattr(self.aeroflot_list[0], value):
                return sorted(self.aeroflot_list, key=lambda x: getattr(x, value))
            else:
                print("incorrect criteria try again", "\n")
                continue

    def find_by(self, value):
        count = 0

        for i in range(0, len(self.aeroflot_list)):
            bool = False
            for attr in self.aeroflot_list[i].__dict__:
                if str(getattr(self.aeroflot_list[i], attr)).find(value) != -1:
                    bool = True
                    count += 1
            if bool:
                print(self.aeroflot_list[i])
        if count == 0:
            print('nothing was found by ', value)

    def create_new_object(self):
        o = Aeroflot()

        s = input('enter destination')

        a = input('enter departure day')

        b = input('enter flight number')

        f = input('enter capacity')

        r = input('enter price')
        iputs = [s, a, b, f, r]
        if validate_is_all_correct(iputs):
            o.destination = s
            o.departure = a
            o.flight_number = abs(int(b))
            o.capacity = abs(int(f))
            o.price = abs(int(r))
            return o
        else:
            print('incorrect inputs try again')
            self.create_new_object()

    def delete_object_from_file(self, value):
        with open(self.name_of_file, "r+") as f:
            lines = f.readlines()
        with open(self.name_of_file, "w") as f:
            for line in lines:
                if not line.strip("\n").__contains__(value):
                    f.write(line)

    def show_menu(self, s):
        while True:
            print(
                'choose what do you want to do(1 - sorting, 2 - search for value, 3 - change variable of any object, 4 - add object to file, 5-delete object from file 0 - exit)')
            choice = input()
            if choice == '1':
                self.aeroflot_list = self.sort_by()
                print(self.aeroflot_list)
                continue
            if choice == '2':
                print('enter value which you want to find: ')
                value = input()
                if value.isdigit():
                    value = int(value)
                self.find_by(value)
                continue
            if choice == '3':
                self.aeroflot_list = self.change_element_of_object(s)
                print(self.aeroflot_list)
                continue
            if choice == '4':
                self.add_to_file(self.create_new_object())
                self.aeroflot_list = self.read_file(s)
                print(self.aeroflot_list)
                continue
            if choice == '5':
                print('enter value which you want to delete')
                value = input()
                self.delete_object_from_file(value)
                self.aeroflot_list = self.read_file(s)
                print(self.aeroflot_list)
                continue
            if choice == '0':
                print('exit')
                break
            else:
                print('incorrect inputs try again')
                continue

    def read_file(self, s):
        aeroflot_list = []
        file = open(s, 'r+')
        for line in file:
            words = line.split()
            cur_aeroflot = Aeroflot()

            if validate_is_all_correct(words):
                cur_aeroflot.destination = words[0]
                cur_aeroflot.departure = words[1]
                cur_aeroflot.flight_number = words[2]
                cur_aeroflot.capacity = words[3] 
                cur_aeroflot.price = words[4]
            else:
                continue
            aeroflot_list.append(cur_aeroflot)
        file.close()
        return aeroflot_list

    def change_element_of_object(self, s):
        print("Text to search for:")
        text_to_search = input("> ")

        print("Text to replace it with:")
        text_to_replace = input("> ")

        print("File to perform Search-Replace on:")
        file_to_search = s

        temp_file = open(file_to_search, 'r+')

        for line in fileinput.input(file_to_search):
            if text_to_search in line:
                print('Match Found')
            else:
                print('Match Not Found!!')
            temp_file.write(line.replace(text_to_search, text_to_replace))
        temp_file.close()
        arr = self.read_file(file_to_search)

        return arr
