
from DuckComponent import DuckComponentClass
from DuckIterator import DuckIteratorClass

# ========================================= Duck Class ===================================#
class DuckClass(DuckComponentClass):
    flyBehavior = None
    quackBehavior = None

    def __init__(self):
        print 'initialized a new Duck'

    def createIterator(self):
        return DuckIteratorClass()
        
    def setFlyBehavior(self, behavior):
        self.flyBehavior = behavior

    def setQuackBehavior(self, behavior):
        self.quackBehavior = behavior

    def performFly(self):
        return self.flyBehavior.fly()

    def performQuack(self):
        return self.quackBehavior.quack()

    def getColumns(self):
        # Unneeded method for Duck class but implemented due to Composite Pattern
        pass

    def getRows(self):
        # Unneeded method for Duck class but implemented due to Composite Pattern
        pass

    def addDuckComponent(self, component):
        # a duck can't add anything else in it.
        return False

    def replaceDuckComponent(self, component_old, component_new):
        # a duck can't update anything else in it.
        return False

    def removeDuckComponent(self, component):
        # a duck can't add anything else in it.
        return -1

# ----------------------------------------------
