# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclasses with polymorphic behavior
class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"

class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"

class Boat(Vehicle):
    def move(self):
        return "🛥️ Sailing on the water"

class Bicycle(Vehicle):
    def move(self):
        return "🚴 Pedaling on a bike path"

# Function that demonstrates polymorphism
def show_vehicle_movement(vehicle):
    print(vehicle.move())

# Create objects of different vehicle types
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Loop through and demonstrate polymorphism
for v in vehicles:
    show_vehicle_movement(v)
