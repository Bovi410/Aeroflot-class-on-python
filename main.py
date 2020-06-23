import sys

from aeroflot_collection import AeroflotCollection
from myFile import create_new_file
from validators import validate_number

print('enter name of file')
s = str(input())
if not str.endswith(s, '.txt'):
    print('incorrect file')
    sys.exit(0)
file = create_new_file(s)
aeroflot = AeroflotCollection(s)
while True:
    print('how many object you want to add?')
    count = input()
    if not validate_number(count):
        print('incorrect inputs try again')
        continue
    count = abs(int(count))
    break
for i in range(count):
    aeroflot.add_to_file(aeroflot.create_new_object())
aeroflot = AeroflotCollection(s)

if aeroflot.is_list_empty():
    print("error empty list")
    sys.exit(0)
for o in aeroflot.aeroflot_list:
    print(o)
aeroflot.show_menu(s)
