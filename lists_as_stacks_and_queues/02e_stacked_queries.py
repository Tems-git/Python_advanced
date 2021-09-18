sequence = []
n = int(input())
result = []

for _ in range(n):
    command = input().split()
    if command[0] == "1":
        sequence.append(int(command[1]))
    elif command[0] == "2":
        if sequence:
            sequence.pop()
    elif command[0] == "3":
        if sequence:
            print(max(sequence))
    elif command[0] == "4":
        if sequence:
            print(min(sequence))
while len(sequence) > 0:
    result.append(str(sequence.pop()))
print(", ".join(result))