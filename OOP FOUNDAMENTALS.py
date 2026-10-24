
#!/usr/bin/env python3
#practical example of OOP concepts in Python
#leah mae jayme
from abc import ABC, abstractmethod


# 1. ABSTRACTION: Define an abstract base class that cannot be instantiated directly

class Vehicle(ABC): #THIS IS THE ABSTRACT CLASS

  def __init__(self, make, model): #THIS IS THE CONSTRUCTOR
    self.make = make #THIS IS THE INSTANCE VARIABLE
    self.model = model #THIS IS THE INSTANCE VARIABLE

  @abstractmethod #THIS IS THE ABSTRACT METHOD
  def start_engine(self):  #THIS IS THE ABSTRACT METHOD 
    """Subclasses must implement this behavior.""" #THIS IS THE ABSTRACT METHOD

    pass #THIS IS THE ABSTRACT METHOD

  def vehicle_info(self): #THIS IS THE CONCRETE METHOD
    return f"Vehicle: {self.make} {self.model}" #THIS IS THE CONCRETE METHOD


# 2. INHERITANCE & 4. POLYMORPHISM: Car inherits from Vehicle and overrides start_engine

class Car(Vehicle): #this is the subclass

  def __init__(self, make, model, fuel_level): #this is the constructor of the subclass
    super().__init__(make, model) #this calls the constructor of the superclass (Vehicle)
    self.__fuel_level = fuel_level  #this is a private attribute (encapsulation)
                                                        #encapsulated data is hidden from outside access, promoting data integrity and security
    
    # 3. ENCAPSULATION: Private attribute
  # Getter method to safely access encapsulated data

  def get_fuel_level(self): #this is the getter method for the private attribute __fuel_level
    return f"{self.__fuel_level}% fuel remaining" #this is the getter method for the private attribute __fuel_level 
                                                    #it provides controlled access to the private attribute, allowing external code to retrieve its value without directly accessing it.

  # Polymorphic implementation for a standard gas car
  def start_engine(self): #this is the overridden method from the abstract class Vehicle it provides a specific implementation for starting the engine of a Car.
    return f"{self.make} {self.model}'s engine roars to life! MOEW MOEW." #THIS IS THE POLYMORPHIC IMPLEMENTATION OF THE START_ENGINE METHOD FOR THE CAR CLASS.


# 2. INHERITANCE & 4. POLYMORPHISM: ElectricCar inherits from Vehicle and implements its own version

class ElectricCar(Vehicle): #this is the subclass OF Vehicle

  def __init__(self, make, model, battery_percentage): #this is the constructor of the subclass ElectricCar IT TAKES THE PARAMETERS MAKE, MODEL, AND BATTERY_PERCENTAGE
    super().__init__(make, model) #this calls the constructor of the superclass (Vehicle) to initialize the make and model attributes IT'S A WAY TO REUSE THE CODE FROM THE PARENT CLASS AND ENSURE THAT THE COMMON ATTRIBUTES ARE PROPERLY INITIALIZED.
    self.__battery_percentage = battery_percentage  # Encapsulated data
                                                    #THis is a private attribute that stores the battery percentage of the electric car. It is encapsulated to prevent direct access from outside the class, promoting data integrity and security.

  def get_battery_percentage(self): #this is the getter method for the private attribute __battery_percentage
    return f"{self.__battery_percentage}% battery remaining" #this is the getter method for the private attribute __battery_percentage. It provides controlled access to the private attribute, allowing external code to retrieve its value without directly accessing it.

  # Polymorphic implementation for an electric car

  def start_engine(self): #this is the overridden method from the abstract class Vehicle it provides a specific implementation for starting the engine of an ElectricCar.
    return f"{self.make} {self.model} powers on silently. Ready to travel." #THIS IS THE POLYMORPHIC IMPLEMENTATION OF THE START_ENGINE METHOD FOR THE ELECTRICCAR CLASS.


# --- Demonstration ---

# Creating objects (instances of the classes)
my_sedan = Car("Toyota", "Camry", 50) #this creates an instance of the Car class with the make "Toyota", model "Camry", and fuel level 50. It initializes the attributes of the Car object using the constructor defined in the Car class.
my_ev = ElectricCar("Tesla", "Model Y", 90) #this creates an instance of the ElectricCar class with the make "Tesla", model "Model Y", and battery percentage 90. It initializes the attributes of the ElectricCar object using the constructor defined in the ElectricCar class.

vehicles = [my_sedan, my_ev] #this creates a list called vehicles that contains the instances of the Car and ElectricCar classes. It allows for easy iteration and management of multiple vehicle objects.

for v in vehicles: #this iterates over each vehicle object in the vehicles list. It allows us to perform actions on each vehicle, such as retrieving information and starting the engine.
  #this is for LOOP that iterates over each vehicle object in the vehicles list. It allows us to perform actions on each vehicle, such as retrieving information and starting the engine.
  print(v.vehicle_info()) #this calls the vehicle_info method on the current vehicle object v. It retrieves and prints the make and model of the vehicle.
  print(v.start_engine())  # Polymorphism in action!
  print("-" * 30) #This prints a separator line of 30 dashes for better readability in the output.


# Encapsulation protection in action:
# print(my_sedan.__fuel_level) # This would raise an AttributeError!

print("Checking fuel securely:", my_sedan.get_fuel_level()) #this calls the get_fuel_level method on the my_sedan object. It retrieves and prints the fuel level of the car in a controlled manner, demonstrating encapsulation protection.