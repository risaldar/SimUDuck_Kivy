
import abc

import CollectionsManager
from DuckComponent import DuckComponentClass
from DuckComponentDecorator import DuckComponentDecoratorClass

# ================================ Concrete Decorator Class ==============================#
class DuckComponentDecoratorRedClass(DuckComponentDecoratorClass):

    WrappedDuckComponent = None

    def __init__(self, component):
        self.WrappedDuckComponent = component
        print 'Initialized a new DuckComponentDecoratorRed'

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

    def removeDuckComponent(self, component):
        # Forward this request to wrapped object
        return self.WrappedDuckComponent.removeDuckComponent(component)

    def getDuckComponentDecoration(self):
        colors = [[255, 0, 0, 1]]
        if self.WrappedDuckComponent is not None and self.WrappedDuckComponent.getDuckComponentDecoration() is not None:
            colors.append(self.WrappedDuckComponent.getDuckComponentDecoration())
        return colors
# ----------------------------------------------
