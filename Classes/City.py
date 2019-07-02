
class City:

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def get_xcoord(self):
        return self.x_coordinate

    def get_ycoord(self):
        return self.y_coordinate

    def __str__(self):
        return "City with coordinates: X:{} - Y:{}".format(self.x_coordinate, self.y_coordinate)

