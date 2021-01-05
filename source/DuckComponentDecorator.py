
import abc

from DuckComponent import DuckComponentClass

# ========================= Duck Component Decorator Class =============================#

# abstract class for Duck Component Decorator. 
# Implements Composite Pattern For Duck and Coop Classes.

class DuckComponentDecoratorClass(DuckComponentClass):
    '''
    A class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract methods and properties are overridden.
    '''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def setFlyBehavior(self, behavior):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass

    @abc.abstractmethod
    def setQuackBehavior(self, behavior):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass

    @abc.abstractmethod
    def performFly(self):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass

    @abc.abstractmethod
    def performQuack(self):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass

    @abc.abstractmethod
    def getColumns(self):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass

    @abc.abstractmethod
    def getRows(self):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass

    @abc.abstractmethod
    def addDuckComponent(self, component):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass

    @abc.abstractmethod
    def removeDuckComponent(self, component):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass

    @abc.abstractmethod
    def getDuckComponentDecoration(self, component):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass

    @abc.abstractmethod
    def createIterator(self):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass
# ----------------------------------------------
