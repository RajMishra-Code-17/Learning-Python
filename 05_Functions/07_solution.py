def sum_all(*args):
    print(*args)
    return sum (args)


print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3,4))
print(sum_all(1, 2, 3,4,5))

# we can use anything in the palce of the args but it is not a good practice you should you use args and the sign astic is necessary to use..

# as i am am learning this first time its little good to know about args which can handle multiple value together
# def sum_all_value(*args):
#     print(args)
#     return sum (args)

# print(sum_all_value(1, 2, 3))
# print(sum_all_value(1, 2 , 3, 4))
# print(sum_all_value(1, 2, 3, 4,5))
