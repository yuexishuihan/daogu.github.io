import time
class User():
    username = 'cy'
    register_time = time.localtime(time.time())
    def f(self):
        print(self.username)
        print(time.asctime(self.register_time))

user = User()
user.f()