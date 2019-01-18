from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

class VIP1(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

# print(VIP.GREEN.name)
# print(VIP.GREEN)
# print(VIP['GREEN'])
result = VIP.GREEN == VIP1.GREEN
print(result)