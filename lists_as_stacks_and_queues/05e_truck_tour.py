from collections import deque

number_of_pumps = int(input())

queue = deque()
for _ in range(number_of_pumps):
    command = input().split()
    petrol = int(command[0])
    distance = int(command[1])
    queue.append([petrol, distance])

for i in range(number_of_pumps):
    fuel_tank = 0
    pump_travel = 0
    for pump in queue:
        fuel, distance_to_next = pump[0], pump[1]
        fuel_tank += fuel
        if fuel_tank < distance_to_next:
            queue.rotate(-1)
            break
        pump_travel += 1
        fuel_tank -= distance_to_next
    if pump_travel == len(queue):
        print(i)
        break


# v.2
from collections import deque

queue = deque()
pumps_count = int(input())
for _ in range(pumps_count):
    pump = [int(x) for x in input().split()]
    queue.append(pump)

for index in range(pumps_count):
    car_fuel = 0
    completed = True

    for petrol, distance in queue:
        car_fuel += petrol
        if distance > car_fuel:
            completed = False
            break
        car_fuel -= distance

    if completed:
        print(index)
        break
    queue.append(queue.popleft())

