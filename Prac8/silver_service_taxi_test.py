from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    new_taxi = SilverServiceTaxi('Prius 1', 100, 2)
    print(new_taxi)
    new_taxi.fanciness = 2
    new_taxi.drive(18)
    print(new_taxi.get_fare())


if __name__ == '__main__':
    main()