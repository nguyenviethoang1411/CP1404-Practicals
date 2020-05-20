from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Drive car program"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    current_taxi = None
    # Menu looper
    while True:
        print('Let\'s drive!')
        print('(C)hoose Taxi')
        print('(D)rive')
        print('(Q)uit')
        choice = input('>>>').upper()
        if choice == 'C':
            for index, taxi in enumerate(taxis):
                print('{} - {}'.format(index, taxi))

            current_taxi = int(input('Choose taxi: '))
            bill_to_date += taxis[current_taxi].get_fare()
            print('Bill to date: ', round(bill_to_date, 1))
        elif choice == 'D':
            if current_taxi is not None:
                distance = int(input('Drive how far? '))
                taxis[current_taxi].drive(distance)
                fare = taxis[current_taxi].get_fare()
                print('Your {} trip cost you {}'.format(taxis[current_taxi].name, fare))
                bill_to_date += fare
                print('Bill to date: ', round(bill_to_date, 1))
            else:
                print('Please choose a taxi first!')
            pass
        elif choice == 'Q':
            print('Total trip cost: ', round(bill_to_date, 1))
            break
        else:
            print('Invalid menu choice')


main()