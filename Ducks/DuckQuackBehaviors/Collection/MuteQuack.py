
import abc

from Ducks.DuckQuackBehaviors.QuackBehavior import QuackBehavior

# ----------------------------------------------
class MuteQuackClass(QuackBehavior):
    details = 'I am mute'
    def __init__(self):
        pass
    def quack(self):
        return 'I am mute'
    def getDetails(self):
        return self.details
# ----------------------------------------------
