
from DuckComponent import DuckComponentClass
from CoopIterator import CoopIteratorClass

# ========================================= Coop Class ===================================#
class CoopClass(DuckComponentClass):
    CoopIterator = None
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

    def updateDuckComponent(self, component_old, component_new):
        component_index = self.ChildDuckComponents.index(component_old)
        self.ChildDuckComponents.remove(component_old)
        self.ChildDuckComponents.insert(component_index, component_new)
        return True

    def removeDuckComponent(self, component):
        if component in self.ChildDuckComponents:
            self.ChildDuckComponents.remove(component)
            return True
        else:
            return False

    def createIterator(self):
        self.CoopIterator = CoopIteratorClass(iter(self.ChildDuckComponents))
        return self.CoopIterator
# ----------------------------------------------
