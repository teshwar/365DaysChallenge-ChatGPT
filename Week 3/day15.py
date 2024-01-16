class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f"{self.name} says meow!")

    def get_age(self):
        return self.age
    
    def set_age(self,new_age):
        if new_age > 0:
            self.age = new_age
        else:
            print("Age must be a positive number.")

#Creatning an instance of Cat class
my_cat = Cat(name="Garfield", age = 7)

#Accessing attributes and methods
print(f"My cat's name is {my_cat.name}") #should not access class value directly
my_cat.meow()
print(f"My cat is {my_cat.get_age()} years old.")

#Changing the age using the setter method
my_cat.set_age(3)
print(f"My cat is {my_cat.get_age()} years old.")