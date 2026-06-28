class car:

    total_car = 0
    def __init__(self, brand, model):
       self.__brand = brand
       self.model = model
       car.total_car += 1
    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
         return f"{self.__brand} {self.model}"
    def fuel_type(self):
        return "petrol or diseal"
    def general_discription():
        return "cars are means of transport"
    
class Electriccar(car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size 

    def fuel_type(self):
        return "Electric charge"       

my_tesla = Electriccar("Tesla","Model s","85KWH")
print(my_tesla.full_name())
# print(my_tesla.__brand)
print(my_tesla.get_brand())   
print(my_tesla.fuel_type())
print(car.total_car)
safari = car("tata", "safari") 
print(safari.fuel_type())
print(safari.total_car)






# my_car = car("Fortuner","Defender")
# # here the my_car denotes the object of the code
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())



# my_new_car = car("Tata","safari")
# print(my_new_car.model)


# the init is called as a constructor when the object is created this method is called.


# this is for the practice


# class car:
#     def __init__(self, brand,model):
#         # here we have defined the value of the brand and the model
#         self.brand = brand
#         self.model = model
# my_car = car("tata","thar")
# # here we have defined the class value
# print(my_car.model)
# print(my_car.brand)


# my_old_car = car ("tata","nano")
# print(my_old_car.model)
# print(my_old_car.brand)

