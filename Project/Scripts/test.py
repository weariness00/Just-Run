import enum as Enum

# class keyType(Enum):
#     Left = 0
#     Right = 1
#     UP = 2
#     Down = 3
#     pass

idle = dict()
for i in range(4):
    idle[i] = False

items = [item for item in idle.values()]
items[1] = True
print(items)
print(any(items))