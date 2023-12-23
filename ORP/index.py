# class Employee:
    
#     num_of_emps = 0
#     raise_amount = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '_' + last + '@company.com'

#         Employee.num_of_emps +=1

#     def fullname(self):
#         return '{} {}' .format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)


# print(Employee.num_of_emps)

# emp_1 = Employee('Farzel', 'Acheampong', 5000)
# emp_2 = Employee('Test', 'User', 6000)

# print(Employee.num_of_emps)



        # Exercise 1

# class restaurant:s

#     def __init__(self, name, type):
#         self.name = name
#         self.type = type
    
#     def describe_restaurant(self):
#         return f"\nRestuarant Name: {self.name}, \nRestuarant Type: {self.type}"
    
#     def open_restuarant(self):
#         return f"\nThe {self.name} is now opened"
    
# my_restuarant = restaurant('Pizza Palace', 'African')
# my_restuarant1 = restaurant('FusionFlare', 'Global Fusion')
# my_restuarant2 = restaurant('ZenBowl', 'Asain Inspired-Bowls')

# print(my_restuarant.describe_restaurant())
# print(my_restuarant.describe_restaurant())
# print(my_restuarant2.describe_restaurant())
# print(my_restuarant2.open_restuarant())
# print(my_restuarant.open_restuarant())
# print(my_restuarant1.open_restuarant())

            # Exercise

# class User:
#     def __init__(self, f_name, l_name):
#         self.f_name = f_name
#         self.l_name = l_name

#     def describe_user(self):
#         return f"\nFirst Name: {self.f_name} \nLast Name: {self.l_name}"
    
#     def greet_user(self):
#         return f"\nGreeting to you {self.f_name} {self.l_name}!!!"
    
# person = User('Farzel', 'Acheampong')
# person1 = User('Masood', 'Acheampong')

# print(person.describe_user())
# print(person1.describe_user())
# print(person1.greet_user())


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_dis_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        reading = f"This car has {self.odometer_reading} mileage."
        return reading
    
    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def incre_odometer(self, miles):
        self.read_odometer += miles

used_car = Car('Subaru', 'M20', 2017)
print(used_car.get_dis_name())

used_car.update_odometer(23_500)
used_car.read_odometer()

used_car.incre_odometer(100)
used_car.read_odometer()

# new_car = Car('Audi', 'a4', 2023)
# print(new_car.get_dis_name())
# print(new_car.read_odometer())