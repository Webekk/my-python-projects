class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_level = 100

    def car_info(self):
        print(self.make, self.model, self.year, self.color)

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine roars to life!!!")

    def accelerate(self):
        print(f"The {self.color} {self.make} {self.model} picks up speed!")

    def brake(self):
        print(f"The {self.make} {self.model} comes to a smooth stop.")

    def check_fuel_level(self):
        if self.fuel_level > 100:
            print(f"Incorrect fuel level!!!.")
        if self.fuel_level < 50:
            print(f"The fuel level is getting low, {self.fuel_level}!")
        if self.fuel_level == 0:
            print(f"The fuel tank is empty, {self.fuel_level}!")

class Honda(Car):
    def __init__(self, make, model, year, color, safe_for_kids : bool):
        super().__init__(make, model, year, color)
        self.safe_for_kids = safe_for_kids

    def honk(self):
        print(f"{self.make} {self.model} honk!!!!!!!!!!")

    def is_the_car_safe(self):
        if self.safe_for_kids:
            print("The car is safe for kids.")

class Driver():
    def __init__(self, name, surname, age, gender, driving_skill, driving_licence : bool):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.driving_skill = driving_skill
        self.driving_licence = driving_licence

    def is_legal_to_drive(self):
        if self.driving_licence and self.age >= 18:
            print("This person is able to drive")
        elif self.age < 18:
            print("This person is too young to drive")
        else:
            print("This person is not able to drive")

class Animal:
    def __init__(self, name: str, nature: str) -> None:
        self.name = name
        self.nature = nature

# Add your class definition here (steps 1-3)
class Dog(Animal):
    def sound(self):
        print(f"{self.name} gives a sound, and he is {self.nature} by nature.")

    def bark(self):
        print(f"woof {self.name}, {self.nature}")


# Creating the instance of the Dog class (step 4)
my_dog = Dog("Buddy", "Golden Retriever")
# Directing the dog to bark (step 5)
my_dog.bark()

