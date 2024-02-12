# object-oriented programming

class People:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


person1 = People("Reid", 20, "72kg", "178cm")
person2 = People("Fredrick", 21, "76kg", "180cm")
person3 = People("James", 19, "54kg", "170cm")

# print(person1.name, person1.age, person1.weight, person1.height)

print(f"Hi, my name is {person2.name}.")

