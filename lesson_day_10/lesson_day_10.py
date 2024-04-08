class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"My name is {self.name}  Dog. I'm a age of a {self.age}.I'm a {self.gender} dog."


# Mongol Bankhar
bankhar = Dog("bankhar", 1, "male")
print(bankhar)

# dasgal 1
pudle=Dog("Amy", 2, "female")
print(pudle)

husky=Dog("Haska", 3, "male")
print(husky)

bulldog=Dog("Boss" , 2 , "male")
print(bulldog)

class Human:
    def __init__(self, name, job, gender):
        self.name=name
        self.job=job
        self.gender=gender
    
    def __str__(self):
        return f"My name is {self.name}. I'm a {self.job}.I'm a {self.gender}."
    

Tuya=Human("Tuya", "teacher", "female")
print(Tuya)

Boldoo=Human("Boldoo","doctor","male")
print(Boldoo)

class Zagas:
    def __init__(self, name, place, color, size):
        self.name=name
        self.place=place
        self.color=color
        self.size=size
    
    def __str__(self):
        return f"This is {self.name}. This fish in  {self.place}.This fish is a {self.color} and {self.size}."
    
whale=Zagas("Whale","ocean", "white","big")
print(whale)
    
class Fish:
    def __init__(self, name, fish_type):
        self.name=name
        self.fish_type=fish_type
    
    def __str_(self):
        return f"I'm a fish of {self.fish_type} amd my name is{self.name}"
    
    def swim_to_south_pole(self):
        return f"I'm a swimming and to southpole"
    
    def change_my_name(self, new_name):
        self.name=new_name

#objects
        
nemo=Fish("Nemo","Clown Fish")
print(nemo)
nemo.swim_to_south_pole()
nemo.change_my_name('Finding Nemo')
print(nemo)

moby_dick=Fish("Moby Dick", "Big White Whale")
print(moby_dick)
moby_dick.swim_to_south_pole()
print(moby_dick)

