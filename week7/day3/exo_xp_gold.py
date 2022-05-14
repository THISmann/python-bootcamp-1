class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        pi = 3.14
        p = 1
        p = self.radius*2*pi
        return p

    def area(self):
        pi = 3.14
        A = 1
        A = pi*self.radius*self.radius
        return A

    def geometrical(self):
        circle = Circle()
        p = circle.perimeter()
        a = circle.area()
        return(p, a)


class MyList:
    def __init__(self, letters):
        self.letters = letters

    def resersed_list(self):
        return self.letters.reverse()

    def sorted_list(self):
        return self.letters.sort()

    def generate_second_list(self):
        pass
