while True:
    try:
        x = int(input('Please enter a number\n'))
        break
    except ValueError:
        print('值类型错误')