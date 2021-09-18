from collections import deque

food = int(input())
queue = deque(int(x) for x in input().split())

print(max(queue))

while queue:
    order = queue.popleft()
    if food >= order:
        food -= order
    else:
        queue.appendleft(order)
        break

if not queue:
    print("Orders complete")
else:
    print("Orders left:"," ".join([str(order) for order in queue]))

# v.2
from collections import deque

total_food = int(input())
orders = deque(map(int, input().split()))

max_order = max(orders)

while orders:
    current_order = orders[0]
    if current_order > total_food:
        break
    else:
        total_food -= current_order
        orders.popleft()

print(max_order)
if orders:
    print(f"Orders left: {' '.join(map(str, orders))}")
else:
    print("Orders complete")