
import abc

from Ducks.DuckFlyBehaviors.FlyBehavior import FlyBehavior

# ============================= Fly Behavior =====================================#
class FlyNoWayClass(FlyBehavior):
    details = 'I have no wings'
    def __init__(self):
        pass
    def fly(self):
        print 'I can not fly'
    def getDetails(self):
        return self.details
# ----------------------------------------------

        