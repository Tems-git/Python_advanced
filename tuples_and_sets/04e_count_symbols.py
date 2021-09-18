# text = input()
# result = {}
#
# for char in text:
#     if char not in result:
#         result[char] = 0
#     result[char] += 1
#
# sorted_result = dict(sorted(result.items(), key=lambda x: x[0]))
#
# for key, value in sorted_result.items():
#     print(f"{key}: {value} time/s")

# v.2
text = input()
words = {}
for ch in text:
    if ch in words:
        words[ch] += 1
    else:
        words[ch] = 1

for letter, count in sorted(words.items()):
    print(f"{letter}: {count} time/s")