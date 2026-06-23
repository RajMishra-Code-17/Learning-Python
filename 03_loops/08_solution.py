number = 2

is_prime = True

if number > 1:
    for i in range(2, number):
    #   for is for the loop and we have defind the range here ..
      if (number%i)==0:
        is_prime =False
        break
print(is_prime)


# for the practice
# num = 2334

# prime_check = True

# if num > 1:
#     for i in range (2, num):
#         if (num%i)==0:
#             prime_check = False
#             break
# print(prime_check)

