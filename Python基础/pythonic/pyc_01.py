def get_sunday():
    return 'Sundan'
def get_monday():
    return 'Monday'
def get_tuesday():
    return 'Tuesday'
def get_default():
    return 'Unkonw'
day = 0
switcher = {
    0:get_sunday,
    1:get_monday,
    2:get_tuesday
}
day_name = switcher.get(day,get_default)()
print(day_name)