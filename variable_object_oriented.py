#OOP version, should be easier
# Instead of self and other, there is left and right

"""
TO DO:
Work on r functions
Fix domain error
"""
import math
class Variable():
    import math
    def __init__(self, name=None) :
        if name != None:
            self.name = name          # its key in the evaluation dictionary
            
    def evaluate(self, values):
        #Independent variable version
        return values[self.name]
    
    def __call__(self, **kwargs):
        return self.evaluate(kwargs)
    
    def __add__(self, other):
        return AdditionVariable(self, other)
    
    def __radd__(self, other):
        return AdditionVariable(self, other)
    
    def __sub__(self, other):
        return SubtractionVariable(self, other)
    
    def __rsub__(self, other):
        return rSubtractionVariable(self, other)
    
    def __mul__(self, other):
        return MultiplicationVariable(self, other)
    
    def __rmul__(self, other):
        return MultiplicationVariable(self, other)
    
    def __truediv__(self, other):
        return DivisionVariable(self, other)
    
    def __rtruediv__(self, other):
        return rDivisionVariable(self, other)
    
    def __pow__(self, other):
        return PowerVariable(self, other)
    
    def __rpow__(self, other):
        return rPowerVariable(self, other)

class AdditionVariable(Variable):
    #left and right corespond to where each variable is in the equation
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    #overrides original evaluate method
    def evaluate(self, values):
        if isinstance(self.left, (float, int)):
            return self.right.evaluate(values) + self.left
        
        if isinstance(self.right, (float, int)):
            return self.left.evaluate(values) + self.right
        
        return self.left.evaluate(values) + self.right.evaluate(values)
    
    #add gradient method later
    
class SubtractionVariable(Variable):
    #left and right corespond to where each variable is in the equation
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.left, (float, int)):
            return self.left - self.right.evaluate(values)
        
        if isinstance(self.right, (float, int)):
            return self.left.evaluate(values) - self.right
        
        return self.left.evaluate(values) - self.right.evaluate(values)
    
    #add gradient method later
    
class rSubtractionVariable(Variable):
    #left and right corespond to where each variable is in the equation
    def __init__(self, left, right):
        self.left = right
        self.right = left
    
    def evaluate(self, values):
        if isinstance(self.left, (float, int)):
            return self.left - self.right.evaluate(values)
        
        if isinstance(self.right, (float, int)):
            return self.left.evaluate(values) - self.right
        
        return self.left.evaluate(values) - self.right.evaluate(values)
    
    #add gradient method later

class MultiplicationVariable(Variable):
    #left and right corespond to where each variable is in the equation
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.left, (float, int)):
            return self.right.evaluate(values) * self.left
        
        if isinstance(self.right, (float, int)):
            return self.left.evaluate(values) * self.right
        
        return self.left.evaluate(values) * self.right.evaluate(values)
    
    #add gradient method later

class DivisionVariable(Variable):
    #left and right corespond to where each variable is in the equation
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.left, (float, int)):
            return self.left / self.right.evaluate(values) 
        
        if isinstance(self.right, (float, int)):
            return self.left.evaluate(values) / self.right
        
        return self.left.evaluate(values) / self.right.evaluate(values)
    
    #add gradient method later
    
class rDivisionVariable(Variable):
    #left and right corespond to where each variable is in the equation
    def __init__(self, left, right):
        self.left = right
        self.right = left
    
    def evaluate(self, values):
        if isinstance(self.left, (float, int)):
            return self.left / self.right.evaluate(values) 
        
        if isinstance(self.right, (float, int)):
            return self.left.evaluate(values) / self.right
        
        return self.left.evaluate(values) / self.right.evaluate(values)
    
    #add gradient method later
    
class PowerVariable(Variable):
    #left and right corespond to where each variable is in the equation
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.left, (float, int)):
            return self.left ** self.right.evaluate(values) 
        
        if isinstance(self.right, (float, int)):
            return self.left.evaluate(values) ** self.right
        
        return self.left.evaluate(values) ** self.right.evaluate(values)
    
    #add gradient method later

class rPowerVariable(Variable):
    #left and right corespond to where each variable is in the equation
    def __init__(self, left, right):
        self.left = right
        self.right = left
    
    def evaluate(self, values):
        if isinstance(self.left, (float, int)):
            return self.left ** self.right.evaluate(values) 
        
        if isinstance(self.right, (float, int)):
            return self.left.evaluate(values) ** self.right
        
        return self.left.evaluate(values) ** self.right.evaluate(values)
    
    #add gradient method later

class ExpVariable(Variable):
    import math
    #left and right corespond to where each variable is in the equation
    def __init__(self, right):
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.right, (int, float)):
            return math.e ** self.right
        
        return math.e ** self.right.evaluate(values)
    
    #add gradient method later
    
class LogVariable(Variable):
    import math
    #left and right corespond to where each variable is in the equation
    def __init__(self, right):
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.right, (int, float)):
            return math.log(self.right) / math.log(math.e)
        
        return math.log(self.right.evaluate(values)) / math.log(math.e)
    
    #add gradient method later
    
def exp(self):
    import math
    return ExpVariable(self)
        
def log(self):
    import math
    return LogVariable(self)