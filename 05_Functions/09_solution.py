def even_generator(limit):
    for i in range(2, limit + 1, 2):
     yield i

for num in even_generator(10):
   print(num)


#    here yeild also return the value but it diiferent from the return
# this will return the value of the even no upto 10



# def even_generator(limit):
#    for i in range(2, limit+ 1, 2):
#       yield i

# for num in even_generator(10):
#    print(num)      

