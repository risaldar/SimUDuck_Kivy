
import abc

# ============================= Fly Behavior =====================================#
class FlyBehavior:
    '''
    A class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract methods and properties are overridden.
    '''
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def fly(self):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass
    @abc.abstractmethod
    def getDetails(self):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass
# ----------------------------------------------

        