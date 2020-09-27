class Stellar:
    name = ""
    mass = 0
    diameter = 0
    speed = 0
    distances = []


    def __init__(self, name, mass=0, diameter=0, speed=0, distances=0):
        self.name = name
        self.mass = mass
        self.diameter = diameter
        self.speed = speed
        self.distances = distances
    
    def setMass(self, mass):
        self.mass = mass

    def getMass(self):
        if self.mass != 0:
            return self.mass
        else:
            raise Exception("Object does not have mass")
    
