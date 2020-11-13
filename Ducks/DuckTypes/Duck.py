
from DuckComponent import DuckComponentClass

# ========================================= Duck Class ===================================#
class DuckClass(DuckComponentClass):
    flyBehavior = None
    quackBehavior = None

    def __init__(self):
        print 'initialized a new Duck'

    def setFlyBehavior(self, behavior):
        self.flyBehavior = behavior

    def setQuackBehavior(self, behavior):
        self.quackBehavior = behavior

    def performFly(self):
        return self.flyBehavior.fly()

    def performQuack(self):
        return self.quackBehavior.quack()
# ----------------------------------------------
