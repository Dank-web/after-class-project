class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"

    def car_type(self):
        return "Luxury Car"


class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "340 km/h"

    def car_type(self):
        return "Sports Car"


# Polymorphism in action
for car in (BMW(), Ferrari()):
    print("Fuel Type:", car.fuel_type())
    print("Max Speed:", car.max_speed())
    print("Car Type:", car.car_type())
    print("----------------------")