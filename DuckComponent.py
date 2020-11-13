
import abc

# =============================== Duck Component Class =================================#

# abstract class for Duck and Coop Classes. 
# Implements Composite Pattern For Duck and Coop Classes.

class DuckComponentClass:
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
# ----------------------------------------------
