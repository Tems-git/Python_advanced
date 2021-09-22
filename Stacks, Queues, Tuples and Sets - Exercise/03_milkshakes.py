from collections import deque

chocolate = deque(int(x) for x in input().split(", "))
milk = deque(int(x) for x in input().split(", "))

milkshakes_count = 0


while chocolate and milk:
    chocolate_qty = chocolate.pop()
    milk_qty = milk.popleft()

    if chocolate_qty == milk_qty:
        milkshakes_count += 1
    elif chocolate_qty <= 0:
        milk.appendleft(milk_qty)
    elif milk_qty <= 0:
        chocolate.append(chocolate_qty)

    else:
        milk.append(milk_qty)
        chocolate_qty -= 5
        chocolate.append(chocolate_qty)
    if milkshakes_count == 5:
        break

if milkshakes_count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join([str(x) for x in milk])}")
else:
    print("Milk: empty")

