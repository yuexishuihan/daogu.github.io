from enum import Enum
from enum import IntEnum,unique

@unique
class VIP(IntEnum):
    YELLOW = 1
    YELLOW_ALIAS = 1
    BLACK = 2
    RED = 3
    GREEN = 4

# for v in VIP.__members__:
#     print(v)

a = 1
print(VIP(a))