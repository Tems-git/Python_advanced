# len_of_sets = [int(x) for x in input().split()]
#
# first_set = set()
# second_set = set()
#
# for _ in range(len_of_sets[0]):
#     first_set.add(input())
#
# for _ in range(len_of_sets[1]):
#     second_set.add(input())
#
# [print(x) for x in first_set.intersection(second_set)]


# v.2
n, m = [int(x) for x in input().split()]

first_set = set()
second_set = set()

for _ in range(n):
    first_set.add(input())

for _ in range(m):
    second_set.add(input())

result = first_set.intersection(second_set)
for el in result:
    print(el)