# username = "Raj"

# def func():
#     username = "Raj Mishra"
#     print(username)


# print(username)
# func()
# here we call the function so the function username will print. and it will print after the first user name.




x = 99
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# # here x is global variable it value comes from outside of the function



# def func3():
#     global x
#     x = 77
#     # here we have taken the value of the x globally from the inside of the function
# func3()    
# print(x)   


def f1():
    # x = 44
    def f2():
     print(x)
    f2()
f1()



def rajcoder (num):
   def actual(x):
      return x ** num
   return actual


f = rajcoder(2)
g = rajcoder(3)
print(f(2))
print(g(3))