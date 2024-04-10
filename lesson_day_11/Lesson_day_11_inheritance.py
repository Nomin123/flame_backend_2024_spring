print("inheritance")





class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    
    def get_descriptive_name(self):
        long_name=f"{self.year}  {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading+=miles

    def fill_gas_tank(self):
        print("The car is full of gass!")


class ElectricCar(Car):
    def __init__(self,make, model,year):
        """Initialize attributes of the parent class."""
        super().__init__(make,model,year)
        #add more configuration to car
        self.battery_size=40
        self.battery=Battery()

    #create new method for this class
    def describe_battery(self):
        print(f"This car has a {self.battery_size}kWh  battery.")
    #override the existing method
        def fill_gas_tank(self):
            """Electric car has don't have gas tanks."""
            print("This car doesn't have a gas tank!")

#Instances as attributes
class Battery:
    def __init__(self, batery_size=40):
        self.battery_size=battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery.size}-kwh battery.")


car=Car('test','test',1992)
car.fill_gas_tank()

my_leaf=ElectricCar("nissan","leaf",2024)
priint(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.fill_gas_tank()
my_leaf.battery.describe_battery()

#battery=Battery()

#Importing module
#Using aliases