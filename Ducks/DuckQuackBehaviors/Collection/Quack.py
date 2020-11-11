
import abc

from Ducks.DuckQuackBehaviors.QuackBehavior import QuackBehavior

# ----------------------------------------------
class QuackClass(QuackBehavior):
    details = 'I can quack'
    def __init__(self):
        pass
    def quack(self):
        print 'I quack'
    def getDetails(self):
        return self.details
# ----------------------------------------------
