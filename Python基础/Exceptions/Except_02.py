try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print('OS error:{0}'.format(err))
except ValueError:
    print("目标不能被转换为int")