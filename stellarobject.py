class Stellar:
    name = ""
    mass = 0
    diameter = 0
    speed = 0
    distances = []
    coordinates = [(0, 0)]
    rgb = (0, 0, 0)

    def __init__(self, name, mass=0, diameter=0, speed=0, distances=0, coordinates=[(0, 0)], rgb=(0, 0, 0)):
        self.name = name
        self.mass = mass
        self.diameter = diameter
        self.speed = speed
        self.distances = distances
        self.coordinates = coordinates
        self.rgb = rgb   
