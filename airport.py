from random import Random

class Airport():

    def __init__(self):
        self.planes = []

    def land(self, plane):
        if self.stormy() == True:
            raise Exception('Plane cannot land')
        else:
            self.planes.append(plane)

    def take_off(self, plane):
        self.planes.remove(plane)

    def stormy(self):
        random = Random()
        weather = random.randint(1, 5)
        if weather > 4:
            return True
