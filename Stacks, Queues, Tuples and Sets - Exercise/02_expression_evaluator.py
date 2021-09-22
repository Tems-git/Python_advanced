from collections import deque

string = deque(input(). split())
current_deque = deque()
result = 0

while string:
    el = string.popleft()
    if el not in ("*", "/", "+", "-"):
        current_deque.append(int(el))
    else:
        operator = el
        result = current_deque.popleft()
        while current_deque:
            current_num = current_deque.popleft()
            expression = str(result) + operator + str(current_num)
            result = int(eval(expression))
        current_deque.append(result)

print(result)


# v.2
from collections import deque

arithmetic_expresions = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,

}
characters = input().split()

numbers = deque()

for ch in characters:
    if ch in arithmetic_expresions:
        result = numbers.popleft()

        while numbers:
            number = numbers.popleft()
            result = arithmetic_expresions[ch](result, number)
        numbers.append(result)
    else:
        numbers.append(int(ch))

print(numbers.popleft())
