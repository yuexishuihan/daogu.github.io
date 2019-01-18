def log(func):
    def wrapper(*args,**kw):
        print('call %s()' %func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print("时间：2019年1月2日16:38:25")

now()