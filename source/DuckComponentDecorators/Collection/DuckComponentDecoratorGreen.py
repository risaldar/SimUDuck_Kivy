
import abc

import CollectionsManager
from DuckComponent import DuckComponentClass
from DuckComponentDecorator import DuckComponentDecoratorClass

# ================================ Concrete Decorator Class ==============================#
class DuckComponentDecoratorGreenClass(DuckComponentDecoratorClass):

    WrappedDuckComponent = None

    def __init__(self, component):
        self.WrappedDuckComponent = component
        print 'Initialized a new DuckComponentDecoratorGreen'

    def getDuckComponentDecoration(self):
        colors = [[0, 255, 0, 1]]
        if self.WrappedDuckComponent is not None and self.WrappedDuckComponent.getDuckComponentDecoration() is not None:
            colors.append(self.WrappedDuckComponent.getDuckComponentDecoration())
        return colors

    def setFlyBehavior(self, behavior):
        # Forward this request to wrapped object
        self.WrappedDuckComponent.setFlyBehavior(behavior)

    def setQuackBehavior(self, behavior):
        # Forward this request to wrapped object
        self.WrappedDuckComponent.setQuackBehavior(behavior)

    def performFly(self):
        # Forward this request to wrapped object
        return self.WrappedDuckComponent.performFly()

    def performQuack(self):
        # Forward this request to wrapped object
        return self.WrappedDuckComponent.performQuack()

    def getColumns(self):
        # Forward this request to wrapped object
        return self.WrappedDuckComponent.getColumns()

    def getRows(self):
        # Forward this request to wrapped object
        return self.WrappedDuckComponent.getRows()

    def addDuckComponent(self, component):
        # Forward this request to wrapped object
        return self.WrappedDuckComponent.addDuckComponent(component)

    def replaceDuckComponent(self, component_old, component_new):
        # Forward this request to wrapped object
        return self.WrappedDuckComponent.replaceDuckComponent(component_old, component_new)

    def removeDuckComponent(self, component):
        # Forward this request to wrapped object
        return self.WrappedDuckComponent.removeDuckComponent(component)

    def createIterator(self):
        return self.WrappedDuckComponent.createIterator()

# ----------------------------------------------
