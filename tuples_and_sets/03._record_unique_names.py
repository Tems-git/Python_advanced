n = int(input())

unique_names = set()

for _ in range(n):
    unique_names.add(input())

print("\n".join(unique_names))

# v.2
import sys
from io import StringIO

test_input = '''8
Lee
Joey
Lee
Joe
Alan
Alan
Peter
Joey
'''

sys.stdin = StringIO(test_input)
n = int(input())
names = {input() for _ in range(n)}
# names = set()
#
# for _ in range(n):
#     names.add(input())
[print(name) for name in names]