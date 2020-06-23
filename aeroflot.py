class Aeroflot(object):
    def __init__(self, destination="", departure="", flight_number=0, capacity=0, price=0):
        self.destination = destination
        self.departure = departure
        self.flight_number = flight_number
        self.capacity = capacity
        self.price = price

    # !!!!!

    def __repr__(self):
        s=str(vars(self))
        return s
