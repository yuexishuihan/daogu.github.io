#列表推导式
# set\dict\tuple都可以被推导
# a = [1,2,3,4,5,6,7,8]
# b = [i*i for i in a if i>= 5]
# print(b)

student = {
    '喜小乐': 18,
    '石干丹':20,
    '很小五':15
}
b = {value:key for key,value in student.items()}
print(b)