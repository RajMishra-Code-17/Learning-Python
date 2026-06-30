file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')
    # here i have made the the thing which have to write inside the file
finally:
    file.close()
    # this is file handling 

    # one more method to file handling

with open('youtube.txt', 'w') as file:
    file.write('chai aur python')
    # in this syntax you dont need to close the file.


# try:
#         pass
#     except:
#         pass
#     finally:
#         pass

# this is the try except method used in python