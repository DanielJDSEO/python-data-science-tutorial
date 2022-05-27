#cunt = "Hello World"
#print(cunt)

# stringVar = "testicles"
# intVar = 1
# floatVar = 2.0
# boolVar = True 

# counter = 0

# while counter < 10:
#     print("balls")
#     counter += 1

# choice = 0
# print(isinstance(choice, int))


# while choice != 1 and choice != 2 and choice != 3 and choice != 4:

#     print("\nThis Program will compute how far a sound wave has traveled through different mediums.")
#     print("Select which gas the sound wave traveled through (1, 2, 3, or 4).")
#     print("=================================================================")
#     print("1: Carbon Dioxide")
#     print("2: Air")
#     print("3: Helium")
#     print("4: Hydrogen")
#     choice = input()

#     try:
#         choice = int(choice)
#     except:
#         print("Error. Cannot convert input to int")

#     try:
#         choice = float(choice)
#     except:
#         print("Error. Cannot convert input to float")   

def myFunction():
    print("Hello from a function")

# myFunction()


# def testes(a,b):
#     print("I Love", a,b)

# testes("lefty and ","righty")


# class - a blueprint used to create objects
# object - an instance of a class 

class Bird:
    # attribute = a variable inside a class
    kingdom = "bird"
    def __init__(self):
        pass 

    def fly(self):
        print("fly fly")

class Parrot(Bird):

    species = "parrot"

    # constructor
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age 

    # method = a function inside a class
    def sayName(self):
        print(self.name)

parrot1 = Parrot("jeffrey", 5)
print(parrot1.species)
print(parrot1.name)
parrot1.sayName()
parrot1.fly()
print(parrot1.kingdom)

