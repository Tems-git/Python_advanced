# parentheses = input()
# stack = []
#
# balanced = True
#
# for paren in parentheses:
#     if paren in "{[(":
#         stack.append(paren)
#     elif paren in "}])":
#         if stack:
#             open_paren = stack.pop()
#         # if paren == "}" and open_paren == "{":
#         #     continue
#         # elif paren == "]" and open_paren == "{":
#         #     continue
#         # elif paren == ")" and open_paren == "(":
#         #     continue
#         # else:
#         #     balanced = False
#         #     break
#
#             if f"{open_paren}{paren}" not in ["{}", "[]", "()"]:
#                 balanced = False
#                 break
#         else:
#             balanced = False
#             break
#
# if balanced:
#     print("YES")
# else:
#     print("NO")


# v.2
expression = input()
stack = []
balanced = True

for ch in expression:
    if ch in "{[(":
        stack.append(ch)
    else:
        if len(stack) == 0:
            balanced = False
            break
        last_opening_bracket = stack.pop()
        pair = f"{last_opening_bracket}{ch}"
        if pair not in "()[]{}":
            balanced = False
            break

if balanced:
    print("YES")
else:
    print("NO")
