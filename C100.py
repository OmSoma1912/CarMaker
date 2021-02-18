class Car(object):
    """
        bluprint for car
    """

    def __init__ (self, model, color, company, speed_limit):
        self.color = color
        self.model = model
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarating...")
        "accelarator functionality here"

    def change_gear(self, gear_type):
        print("gear changed")
        "gear related functionality here"

audi = Car("Q7", "Black", "Audi", 220)

print(audi.start())
            
