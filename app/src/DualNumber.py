
class DualNumber:
    def __init__(self, primal, tangent=1):
        self.primal = primal # real part
        self.tangent = tangent # dual part
    
    def __add__(self, v):
        # right addition : current_object + input object
        if type(v) is DualNumber:
            return DualNumber(self.primal+v.primal, self.tangent+v.tangent)
        else: # scalar addition
            # In fact we should have checked the type of the input object for int/float
            # but other operation with specific object could be defined and allow them to avoid having to rewrite that class exception
            return DualNumber(self.primal+v, self.tangent)
    
    def __mul__(self, v):
        # right multiplication : current_object x input object
        if type(v) is DualNumber:
            return DualNumber(self.primal*v.primal, self.primal*v.tangent + self.tangent*v.primal)
        else: # scalar multiplication
            return DualNumber(self.primal*v, self.tangent*v)
    
    def __sub__(self, v):
        # right subtraction : current_object - input object
        if type(v) is DualNumber:
            return DualNumber(self.primal - v.primal, self.tangent - v.tangent)
        else: # scalar substraction
            return DualNumber(self.primal - v, self.tangent)
    
    def __truediv__(self, v):
        # numerator division : current_object / input object
        if type(v) is DualNumber:
            dem = v.primal**2
            val = self*DualNumber(v.primal, -v.tangent)

            return DualNumber(val.primal/dem, val.tangent/dem)
        else:
            return DualNumber(self.primal/v, self.tangent/v)

    def __rmul__(self, v):
        # left scalar mutiplication : scalar x current_object
        return DualNumber(self.primal*v, self.tangent*v)
    
    def __radd__(self, v):
        # left scalar addition : scalar + current_object
        return DualNumber(self.primal+v, self.tangent)
    
    def __rsub__(self, v):
        # left scalar substraction : scalar - current_object
        return DualNumber(self.primal-v, self.tangent)
    
    def __rtruediv__(self, v):
        # denominator diviison : scalar / current_object

        # Since the division gives tricky expansion we just forward that case to
        # the previous division definition for numerator dual number
        return DualNumber(v, 0)/self

    def __neg__(self):
        # - current_object
        return DualNumber(-self.primal, -self.tangent)
    
    def __pos__(self):
        return self

    def __str__(self):
        return "{0} + {1}ɛ".format(self.primal, self.tangent)
    
