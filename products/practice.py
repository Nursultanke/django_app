# a = [i for i in range(10)]
#
# b = []
# for i in range(10):
#     b.append('q')
#
#
# print(a)
# print(b)
import random

my_list =[random.randint(1, 10) for i in range(10)]


def my_func(my_list):
    return my_list


print(my_func(my_list))