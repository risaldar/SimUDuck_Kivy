
import abc

from Ducks.DuckQuackBehaviors.QuackBehavior import QuackBehavior

# ----------------------------------------------
class QuackClass(QuackBehavior):
    details = 'I can quack'
    def __init__(self):
        pass
    def quack(self):
        return 'I quack'
    def getDetails(self):
        return self.details
# ----------------------------------------------
