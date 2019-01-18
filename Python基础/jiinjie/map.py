list_x = [1,2,3,4,5,6,7,8,9]
list_y = [1,2,3,4,5,6,7]

r = map(lambda x,y:x*x+y,list_x,list_y)
print(list(r))