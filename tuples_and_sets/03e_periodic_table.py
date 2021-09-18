n = int(input())
unique_elements = set()

for _ in range(n):
    [unique_elements.add(x) for x in input().split()]

[print(x) for x in unique_elements]


# v.2
n = int(input())

elements = set()

for _ in range(n):

    current_elements = set(input().split())
    elements = elements.union(current_elements)

[print(x) for x in elements]

