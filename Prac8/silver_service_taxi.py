from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Extended from Taxi class"""
    # Class variable
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def __str__(self):
        return "{} plus flagfall of ${}".format(super().__str__(), self.flag_fall)

    def get_fare(self):
        # If distance > 0 then count the flag fall
        return super().get_fare() + self.flag_fall if self.current_fare_distance != 0 else 0
