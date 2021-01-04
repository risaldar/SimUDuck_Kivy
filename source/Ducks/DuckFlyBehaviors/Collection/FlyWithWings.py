
import abc

from Ducks.DuckFlyBehaviors.FlyBehavior import FlyBehavior

# ============================= Fly Behavior =====================================#
class FlyWithWingsClass(FlyBehavior):
    details = 'I can fly with Wings'
    def __init__(self):
        pass
    def fly(self):
        return 'I am flying with wings'
    def getDetails(self):
        return self.details
# ----------------------------------------------
        