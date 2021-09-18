# n = int(input())
# longest_intersection = set()
#
# for _ in range(n):
#     range_1, range_2 = input().split("-")
#     first_start, first_end = range_1.split(",")
#     second_start, second_end = range_2.split(",")
#     current_range_1 = set()
#     current_range_2 = set()
#
#     for i in range(int(first_start), int(first_end) + 1):
#         current_range_1.add(i)
#
#     for i in range(int(second_start), int(second_end) + 1):
#         current_range_2.add(i)
#
#     current_intersection = current_range_1.intersection(current_range_2)
#     if len(current_intersection) > len(longest_intersection):
#         longest_intersection = current_intersection
#
# longest_intersection = [str(x) for x in longest_intersection]
# print(f"Longest intersection is [{', '.join(longest_intersection)}] with length {len(longest_intersection)}")

# v.2
n = int(input())

longest_intersection = set()
for _ in range(n):
    first, second = input().split("-")
    first_start, first_end = [int(x) for x in first.split(",")]
    second_start, second_end = [int(x) for x in second.split(",")]
    first_range = set(range(first_start, first_end + 1))
    second_range = set(range(second_start, second_end + 1))

    current_intersection = first_range.intersection(second_range)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection
print(f"Longest intersection is [{', '.join([str(x) for x in longest_intersection])}] with length {len(longest_intersection)}")

