n = int(input())

usernames = set()

for _ in range(n):
    usernames.add(input())

[print(x) for x in usernames]