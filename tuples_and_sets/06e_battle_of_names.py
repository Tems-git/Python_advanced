# n = int(input())
#
# even_set = set()
# odd_set = set()
#
# for i in range(1, n + 1):
#     current_ascii_values = 0
#     for char in input():
#         current_ascii_values += ord(char)
#     current_ascii_values = int(current_ascii_values / i)
#     if current_ascii_values % 2 == 0:
#         even_set.add(current_ascii_values)
#     else:
#         odd_set.add(current_ascii_values)
#
# if sum(even_set) == sum(odd_set):
#     print(", ".join([str(x) for x in even_set.union(odd_set)]))
# elif sum(odd_set) > sum(even_set):
#     print(", ".join([str(x) for x in odd_set.difference(even_set)]))
# elif sum(even_set) > sum(odd_set):
#     print(", ".join([str(x) for x in even_set.symmetric_difference(odd_set)]))


# v.2
n = int(input())

even = set()
odd = set()

for row in range(1, n + 1):
    name = input()
    name_sum = sum([ord(x) for x in name]) // row
    if name_sum % 2 == 0:
        even.add(name_sum)
    else:
        odd.add(name_sum)

even_sum = sum(even)
odd_sum = sum(odd)

result = set()
if even_sum == odd_sum:
    result = odd.union(even)

elif even_sum > odd_sum:
    result = odd.symmetric_difference(even)

else:
    result = odd.difference(even)

print(", ".join([str(x) for x in result]))
