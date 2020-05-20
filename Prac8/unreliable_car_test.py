from random import randint
from prac_08.unreliable_car import UnreliableCar


def main():
    new_car = UnreliableCar('Truck', 100, 80)
    print(new_car)
    random_distance = randint(0, 100)
    new_car.drive(random_distance)
    print(new_car)

main()