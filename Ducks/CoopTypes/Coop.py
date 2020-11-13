
from DuckComponent import DuckComponentClass

# ========================================= Coop Class ===================================#
class CoopClass(DuckComponentClass):
    ChildDuckComponents = None

    def __init__(self):
        self.ChildDuckComponents = []
        print 'initialized a new Coop'

    def setFlyBehavior(self, behavior):
        for child in self.ChildDuckComponents:
            child.setFlyBehavior(behavior)

    def setQuackBehavior(self, behavior):
        for child in self.ChildDuckComponents:
            child.setQuackBehavior(behavior)

    def performFly(self):
        # Unneeded method for Duck class but implemented due to Composite Pattern
        pass

    def performQuack(self):
        # Unneeded method for Duck class but implemented due to Composite Pattern
        pass

    def addDuckComponent(self, component):
        self.ChildDuckComponents.append(component)
        return True
# ----------------------------------------------
