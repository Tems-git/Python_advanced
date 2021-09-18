clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

current_rack_qty = []
rack_count = 1

while clothes:
    current_cloth = clothes.pop()
    if current_cloth + sum(current_rack_qty) <= rack_capacity:
        current_rack_qty.append(current_cloth)
    else:
        rack_count += 1
        current_rack_qty.clear()
        current_rack_qty.append(current_cloth)

print(rack_count)


# v.2
clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

used_racks = 1
current_rack_capacity = rack_capacity

while clothes:
    current_cloth = clothes[-1]
    if current_cloth > current_rack_capacity:
        used_racks += 1
        current_rack_capacity = rack_capacity
    else:
        current_rack_capacity -= current_cloth
        clothes.pop()

print(used_racks)
