user = []
class User():
    def __init__(self,username,register_time):
        self.username = username
        self.register_time = register_time

user.append(User('A','23'))
user.append(User('D','15'))
user.append(User('Z','8'))
user.append(User('H','10'))
user.append(User('B','17'))

print('排序前:')
for x in user:
    print(x.username + ':' + x.register_time)

user.sort(key = lambda x: x.username)
print('username排序后：')
for x in user:
    print(x.username + ':' + x.register_time)

user.sort(key=lambda x:int(x.register_time),reverse=False)
print('time排序后：')
for x in user:
    print(x.username + ':' + x.register_time)