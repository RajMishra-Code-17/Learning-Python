def factorial(n):
    if n == 0:
        return 1
    # return because the factorial of 0 is 1
    else:
        return n * factorial(n-1) 
print(factorial(5))


# for the practice
# def factorial (n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial (n-1)
#     print(factorial(23))