
import abc

from Ducks.DuckQuackBehaviors.QuackBehavior import QuackBehavior

# ----------------------------------------------
class SqueakClass(QuackBehavior):
    details = 'I can squeak'
    def __init__(self):
        pass
    def quack(self):
        print 'I squeak'
    def getDetails(self):
        return self.details
# ----------------------------------------------
