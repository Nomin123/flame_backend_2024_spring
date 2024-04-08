#dasgal 1
class Restaurant:
    def __init__(self, restaurant_name , cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    # def __str__(self):
        

    def describe_restaurant(self):
        print(f"Our restaurant name is {self.restaurant_name}. We make {self.cuisine_type}")

    def open_restaurent(self ,open_0r_close):
        print(f'Our restaurant is {open_0r_close}')

JapaneseRestaurant=Restaurant("Hana", "Sushi")

        
JapaneseRestaurant.describe_restaurant()


JapaneseRestaurant.open_restaurent('open')

# dasgaln 2

ItalianFood=Restaurant("Roma","pasta")

ItalianFood.describe_restaurant()

ItalianFood.open_restaurent('close')

# Dasgal 3

class User:
    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
    
    def describe_user(self):
        print(f"My first name is {self.first_name} and my last name is {self.last_name}.")

    def great_user(self):
        print(f"Hi! {self.first_name}.")

Boldoo=User("Boldoo", "Bataa")


Boldoo.describe_user()

Boldoo.great_user()

#dasgal 4
class Restaurant:
    def __init__(self, restaurant_name , cuisine_type, number_served):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=number_served

    # def __str__(self):
        

    def describe_restaurant(self):
        print(f"Our restaurant name is {self.restaurant_name}. We make {self.cuisine_type}")

    def open_restaurent(self ,open_0r_close):
        print(f'Our restaurant is {open_0r_close}')

    def set_number_served(self):
        print(f"Our restaurant served {self.number_served} custumers.")

    def increment_number_served(self):
        self.number_served+=1

JapaneseRestaurant=Restaurant("Hana", "Sushi",30)

        
JapaneseRestaurant.describe_restaurant()


JapaneseRestaurant.open_restaurent('open')
JapaneseRestaurant.set_number_served()
JapaneseRestaurant.increment_number_served()

JapaneseRestaurant.set_number_served()


#dasgal 5
class User:
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=login_attempts
    
    def describe_user(self):
        print(f"My first name is {self.first_name} and my last name is {self.last_name}.")

    def great_user(self):
        print(f"Hi! {self.first_name}.")

    def increment_login_attempts(self):
        self.login_attempts+=1
        print(f"login attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts=0
        print(f"login attempts: {self.login_attempts}")

Boldoo=User("Boldoo", "Bataa", 0)
Boldoo.describe_user()
Boldoo.great_user()

Boldoo.increment_login_attempts()
Boldoo.increment_login_attempts()
Boldoo.increment_login_attempts()
Boldoo.increment_login_attempts()

Boldoo.reset_login_attempts()
Boldoo.increment_login_attempts()