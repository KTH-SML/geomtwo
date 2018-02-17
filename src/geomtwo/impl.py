import geomtwo.msg as gms
import matplotlib.pyplot as plt
import cmath as cm





class Vector:

    def __init__(self, *args, **kwargs):
        if len(args) is 2:
            self._data = complex(*args)
            return
        if len(args) is 1:
            if isinstance(args[0], (self.__class__, gms.Vector)):
                self._data = complex(args[0].x, args[0].y)
                return
            if isinstance(args[0], complex):
                self._data = complex(args[0])
                return
            if isinstance(args[0], list):
                self.__class__.__init__(self, *args[0])
                return
        if len(args) is 0:
            if set(kwargs.keys()) == set(("x", "y")):
                self.__class__.__init__(self, kwargs["x"], kwargs["y"])
                return
            if set(kwargs.keys()) == set(("magnitude", "angle")):
                self.__class__.__init__(self, kwargs["magnitude"]*cm.cos(kwargs["angle"]), kwargs["magnitude"]*cm.sin(kwargs["angle"]))
                return
            if len(kwargs) is 0:
                self.__class__.__init__(self, 0.0, 0.0)
                return
        raise ValueError

    def serialize(self):
        return gms.Vector(self.x, self.y)

    def __repr__(self):
        string = "{} instance".format(self.__class__.__name__)
        string += "\nx: " + str(self._data.real)
        string += "\ny: " + str(self._data.imag)
        return string

    def draw(self, x0=0., y0=0., **kwargs):
        head_size = 0.15*abs(self._data)
        artist = plt.gca().arrow(x0, y0, self.x, self.y, head_length=head_size, head_width=head_size, **kwargs)
        return artist,

    @property
    def x(self): return self._data.real

    @property
    def y(self): return self._data.imag

    @property
    def complex_number(self):
        return self._data

    @property
    def norm_squared(self):
        return self.x**2 + self.y**2

    @property
    def norm(self):
        return abs(self._data)

    def __add__(self, other):
        return self.__class__(self._data+other._data)

    def __neg__(self):
        return self.__class__(-self._data)

    def __sub__(self, other):
        return self + (-other)

    def __rmul__(self, other):
        return self.__class__(other*self._data)

    def __mul__(self, other):
        return self.__rmul__(other)

    def __div__(self, other):
        return self*(1.0/other)

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def cross(self, other):
        return self.x*other.y-self.y*other.x

    def angle_to(self, other, force_positive=False):
        result = cm.phase(complex(self.dot(other),self.cross(other)))
        if result < 0 and force_positive: result += 2*cm.pi
        return result

    def rotate(self, angle):
        return self.__class__(self._data*cm.rect(1.0, angle))

    def saturate(self, threshold):
        if self.norm > threshold: return self*threshold/self.norm
        return self



if __name__ == "__main__":
    vec = Vector(gms.Vector(x=2,y=3))
    print vec
    vec2 = Vector(x=1,y=2)
    print vec + vec2
    print vec - vec2
    print vec.dot(vec2)
    print 2*vec
    print vec2.angle_to(vec, force_positive=True)
    plt.figure()
    plt.xlim([-5,5])
    plt.ylim([-5,5])
    vec.draw()
    #plt.show()





class Point(Vector):

    def __init__(self, *args, **kwargs):
        if len(args) is 1 and isinstance(args[0], (gms.Point, self.__class__)):
            self.__class__.__init__(self, args[0].x, args[0].y)
            return
        Vector.__init__(self, *args, **kwargs)

    def draw(self, **kwargs):
        return plt.scatter(self.x, self.y, **kwargs),

    def serialize(self):
        return gms.Point(self.x, self.y)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            raise TypeError("You are trying to add {} and {}. One cannot add two {}".format(self, other, self.__class__))
        return Vector.__add__(self, other)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self._data - other._data)
        return self + (-other)

    def __mul__(self, other): raise TypeError
    def __rmul__(self, other): raise TypeError
    def __div__(self, other): raise TypeError
    def dot(self, other): raise TypeError
    def cross(self, other): raise TypeError
    def angle_to(self, other): raise TypeError
    def saturate(self, other): raise TypeError





if __name__ == "__main__":
    pt = Point(gms.Point())
    pt.draw(s=200)
    pt2 = Point(2,3)
    (pt-pt2).draw(color="red")
    #plt.show()
    print pt2+vec





class Versor(Vector):

    def __init__(self, *args, **kwargs):
        if len(args) is 2:
            norm = cm.sqrt(args[0]**2+args[1]**2)
            Vector.__init__(self, args[0]/norm, args[1]/norm)
        if len(args) is 1:
            if isinstance(args[0], (gms.Vector, gms.Versor, Vector, Versor)):
                self.__class__.__init__(self, args[0].x, args[0].y)
                return
            if isinstance(args[0], complex):
                self.__class__.__init__(self, args[0].real, args[0].imag)
                return
            if isinstance(args[0], float):
                self.__class__.__init__(self, cm.cos(args[0]), cm.sin(args[0]))
                return
        if len(args) is 0:
            if set(kwargs.keys()) == set(("x", "y")):
                self.__class__.__init__(self, kwargs["x"], kwargs["y"])
                return
            if set(kwargs.keys()) == set(("angle")):
                self.__class__.__init__(self, kwargs["angle"])
                return

    def serialize(self):
        return gms.Versor(self.x, self.y)

    def __add__(self, other): raise TypeError
    def __sub__(self, other): raise TypeError

    def __rmul__(self, other):
        return Vector(other*self._data)

    @property
    def vector(self):
        return Vector(self._data)

    def saturate(self): raise TypeError






if __name__ == "__main__":
    vs2 = Versor(2,4)
    print vs2.norm, vs2.norm_squared
    vs2.draw()
    plt.show()
