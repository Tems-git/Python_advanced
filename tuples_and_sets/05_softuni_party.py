n = int(input())

regular_reservations = set()
vip_reservations = set()

for _ in range(n):
    reservation = input()
    first_char = reservation[0]
    if first_char.isdigit():
        vip_reservations.add(reservation)
    else:
        regular_reservations.add(reservation)

command = input()
while not command == "END":
    if command in regular_reservations:
        regular_reservations.remove(command)
    else:
        vip_reservations.remove(command)

    command = input()

vip_sorted = sorted(vip_reservations)
regular_sorted = sorted(regular_reservations)

print(f"{len(vip_sorted)+len(regular_sorted)}")
[print(x) for x in vip_sorted]
[print(x) for x in regular_sorted]


# v.2
import sys
from io import StringIO

test_input1 = '''5
7IK9Yo0h
9NoBUajQ
Ce8vwPmE
SVQXQCbc
tSzE5t0p
9NoBUajQ
Ce8vwPmE
SVQXQCbc
END
'''

test_input2 = '''6
UgffRkOn
m8rfQBvl
fc1oZCE0
7ugX7bm0
9CQBGUeJ
2FQZT3uC
2FQZT3uC
9CQBGUeJ
fc1oZCE0
END
'''

# sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)

n = int(input())

guest_list = {input() for _ in range(n)}

while True:
    command = input()
    if command == 'END':
        break
    guest_list.remove(command)


def is_vip(guest):
    return guest[0].isdigit()


vip_guests = sorted([g for g in guest_list if is_vip(g)])

regular_guests = sorted([g for g in guest_list if not is_vip(g)])

print(len(guest_list))
[print(g) for g in vip_guests]
[print(g) for g in regular_guests]