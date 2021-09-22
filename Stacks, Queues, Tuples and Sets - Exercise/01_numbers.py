first_sequence = {int(x) for x in input().split()}
second_sequence = {int(x) for x in input().split()}

n = int(input())

for _ in range(n):
    line = input().split()
    command_1, command_2 = line[0], line[1]
    current_nums = {int(x) for x in line[2:]}

    if command_1 == "Add" and command_2 == "First":
        first_sequence = first_sequence.union(current_nums)
    elif command_1 == "Add" and command_2 == "Second":
        second_sequence = second_sequence.union(current_nums)
    elif command_1 == "Remove" and command_2 == "First":
        first_sequence = first_sequence.difference(current_nums)
    elif command_1 == "Remove" and command_2 == "Second":
        second_sequence = second_sequence.difference(current_nums)
    elif command_1 == "Check" and command_2 == "Subset":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

print(", ".join([str(x) for x in sorted(first_sequence)]))
print(", ".join([str(x) for x in sorted(second_sequence)]))