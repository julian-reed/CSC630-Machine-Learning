#OOP version, should be easier
# Instead of self and other, there is left and right

"""
TO DO:
Nothing! All done :)
Onto LogReg!
"""
import math
import numpy as np

class Variable():
    import math
    import numpy as np
    
    number_of_variables = 0
    
    def __init__(self, name=None) :
        if name != None:
            self.name = name
            Variable.number_of_variables += 1
            self.current_number = Variable.number_of_variables
            
    @staticmethod
    def reset():
        Variable.number_of_variables = 0
    
    #Independent variable version, methods to be overwritten later
    def evaluate(self, values):
        return values[self.name]
    
    def grad(self, values):
        output = [0] * Variable.number_of_variables
        output[self.current_number - 1] = 1
        return np.array(output)
        
    def __call__(self, **kwargs):
        return self.evaluate(kwargs)
    
    def gradient(self, **kwargs):
        return self.grad(kwargs)
    
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
    
    def exp(self):
        import math
        return ExpVariable(self)
        
    def log(self):
        import math
        return LogVariable(self)

#Object Oriented Refactoring: self, other = self.right, self.left
class AdditionVariable(Variable):
    def __init__(self, left, right):
        if type(left) == np.int32:
            left = left.item()
        self.left = left
        if type(right) == np.int32:
            right = right.item()
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.left, (float, int, np.ndarray, np.int32)):
            return self.right.evaluate(values) + self.left
        
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return self.left.evaluate(values) + self.right
        
        return self.left.evaluate(values) + self.right.evaluate(values)
    
    def grad(self, values):
        if isinstance(self.left, (float, int, np.ndarray, np.int32)):
            return self.right.grad(values)
        
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return self.left.grad(values)
        
        return self.left.grad(values) + self.right.grad(values)
        
    
class SubtractionVariable(Variable):
    def __init__(self, left, right):
        if type(left) == np.int32:
            left = left.item()
        self.left = left
        if type(right) == np.int32:
            right = right.item()
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.left, (float, int, np.ndarray, np.int32)):
            return self.left - self.right.evaluate(values)
        
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return self.left.evaluate(values) - self.right
        
        return self.left.evaluate(values) - self.right.evaluate(values)
    
    def grad(self, values):
        if isinstance(self.left, (float, int, np.ndarray, np.int32)):
            return self.right.grad(values) * -1
        
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return self.left.grad(values)
        
        return self.left.grad(values) + self.right.grad(values) * -1
    
class rSubtractionVariable(Variable):
    def __init__(self, left, right):
        if type(left) == np.int32:
            left = left.item()
        self.left = left
        if type(right) == np.int32:
            right = right.item()
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.left, (float, int, np.ndarray, np.int32)):
            return self.left - self.right.evaluate(values)
        
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return self.left.evaluate(values) - self.right
        
        return self.left.evaluate(values) - self.right.evaluate(values)
    
    def grad(self, values):
        if isinstance(self.left, (float, int, np.ndarray, np.int32)):
            return self.right.grad(values) * -1
        
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return self.left.grad(values)
        
        return self.left.grad(values) + self.right.grad(values) * -1

class MultiplicationVariable(Variable):
    def __init__(self, left, right):
        if type(left) == np.int32:
            left = left.item()
        self.left = left
        if type(right) == np.int32:
            right = right.item()
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.left, (float, int, np.ndarray, np.int32)):
            return self.right.evaluate(values) * self.left
        
        if isinstance(self.right, (float, int, np.ndarray)):
            return self.left.evaluate(values) * self.right
        
        return self.left.evaluate(values) * self.right.evaluate(values)
    
    def grad(self, values):
        if isinstance(self.left, (float, int, np.ndarray, np.int32)):
            return self.right.grad(values) * self.left
        
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return self.left.grad(values) * self.right
        
        return self.left.evaluate(values) * self.right.grad(values) + self.right.evaluate(values) * self.left.grad(values)

class DivisionVariable(Variable):
    def __init__(self, left, right):
        if type(left) == np.int32:
            left = left.item()
        self.left = left
        if type(right) == np.int32:
            right = right.item()
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.left, (float, int, np.ndarray, np.int32)):
            return self.left / self.right.evaluate(values) 
        
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return self.left.evaluate(values) / self.right
        
        return self.left.evaluate(values) / self.right.evaluate(values)
    
    def grad(self, values):
        if isinstance(self.left, (float, int, np.ndarray, np.int32)):
            return self.right.grad(values)
        
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return self.left.grad(values)
        
        return self.left.grad(values) * self.right.grad(values) ** -1
    
class rDivisionVariable(Variable):
    def __init__(self, left, right):
        if type(left) == np.int32:
            left = left.item()
        self.left = left
        if type(right) == np.int32:
            right = right.item()
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.left, (float, int, np.ndarray, np.int32)):
            return self.left / self.right.evaluate(values) 
        
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return self.left.evaluate(values) / self.right
        
        return self.left.evaluate(values) / self.right.evaluate(values)
    
    def grad(self, values):
        if isinstance(self.left, (float, int, np.ndarray, np.int32)):
            return self.right.grad(values)
        
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return self.left.grad(values)
        
        return self.left.grad(values) * self.right.grad(values) ** -1
    
class PowerVariable(Variable):
    def __init__(self, left, right):
        if type(left) == np.int32:
            left = left.item()
        self.left = left
        if type(right) == np.int32:
            right = right.item()
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.left, (float, int, np.ndarray, np.int32)):
            return self.left ** self.right.evaluate(values) 
        
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return self.left.evaluate(values) ** self.right
        
        return self.left.evaluate(values) ** self.right.evaluate(values)
    
    def grad(self, values):
        if isinstance(self.left, (float, int, np.ndarray, np.int32)):
            return self.right.grad(values) * self.left * self.right.evaluate(values) ** (self.left - 1)
        
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return self.left.grad(values) * self.right * self.left.evaluate(values) ** (self.right - 1)
        
        return (self.right.evaluate(values) * (self.left.evaluate(values) ** (self.right.evaluate(values) - 1))) * self.left.grad(values)

class rPowerVariable(Variable):
    def __init__(self, left, right):
        if type(left) == np.int32:
            left = left.item()
        self.left = left
        if type(right) == np.int32:
            right = right.item()
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.left, (float, int, np.ndarray, np.int32)):
            return self.left ** self.right.evaluate(values) 
        
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return self.left.evaluate(values) ** self.right
        
        return self.left.evaluate(values) ** self.right.evaluate(values)
    
    def grad(self, values):
        if isinstance(self.left, (float, int, np.ndarray, np.int32)):
            return self.right.grad(values) * self.left * self.right.evaluate(values) ** (self.left - 1)
        
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return self.left.grad(values) * self.right * self.left.evaluate(values) ** (self.right - 1)
        
        return (self.right.evaluate(values) * (self.left.evaluate(values) ** (self.right.evaluate(values) - 1))) * self.left.grad(values)

class ExpVariable(Variable):
    import math
    def __init__(self, right):
        if type(right) == np.int32:
            right = right.item()
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return math.e ** self.right
        
        return math.e ** self.right.evaluate(values)
    
    def grad(self, values):
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return (math.e ** self.right) * self.right.grad(values)
        
        return (math.e ** self.right.evaluate(values)) * self.right.grad(values)
    
class LogVariable(Variable):
    def __init__(self, right):
        if type(right) == np.int32:
            right = right.item()
        self.right = right
    
    def evaluate(self, values):
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return np.log(self.right) / np.log(math.e)
        
        return np.log(self.right.evaluate(values)) / np.log(math.e)
    
    def grad(self, values):
        if isinstance(self.right, (float, int, np.ndarray, np.int32)):
            return np.log(0) / np.log(math.e)
        
        return 1/self.right.evaluate(values) * self.right.grad(values)
    
def exp(self):
    import math
    return ExpVariable(self)
        
def log(self):
    import math
    return LogVariable(self)
