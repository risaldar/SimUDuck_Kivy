
import abc

# ===================== Duck Component Iterator Class ===========================#

# abstract class for Duck Component Iterator. 

class DuckComponentIteratorClass:
    '''
    A class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract methods and properties are overridden.
    '''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def next(self):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass
# ----------------------------------------------