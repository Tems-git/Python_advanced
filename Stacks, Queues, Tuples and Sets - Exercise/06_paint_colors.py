from collections import deque

string = deque(x for x in input().split())

main_colors = {"red", "yellow", "blue"}
secondary_color = {"orange", "purple", "green"}
forming_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

colors = []

while string:
    if len(string) >= 2:
        start = string.popleft()
        end = string.pop()
    else:
        start = string.pop()
        end = ""

    current_color = start + end
    current_color_reversed = end + start
    if current_color in main_colors or current_color in secondary_color:
        colors.append(current_color)
    elif current_color_reversed in main_colors or current_color_reversed in secondary_color:
        colors.append(current_color_reversed)
    else:
        start = start[:-1]
        end = end[:-1]
        middle_of_string = len(string) // 2
        if start and end:
            string.insert(middle_of_string, start)
            string.insert(middle_of_string + 1, end)
        elif start:
            string.insert(middle_of_string, start)
        elif end:
            string.insert(middle_of_string, end)

# print(colors)
for color in colors:
    if color in secondary_color:
        if forming_colors[color][0] in colors and forming_colors[color][1] in colors:
            continue
        else:
            colors.remove(color)

print(colors)


