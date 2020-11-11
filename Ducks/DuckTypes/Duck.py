
import abc

# ========================================= Duck Class ===================================#
class DuckClass:
    flyBehavior = None
    quackBehavior = None

    def __init__(self):
        print 'initialized a new Duck'

    def setFlyBehavior(self, behavior):
        self.flyBehavior = behavior

    def setQuackBehavior(self, behavior):
        self.quackBehavior = behavior

    def performFly(self):
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior.quack()
# ----------------------------------------------
