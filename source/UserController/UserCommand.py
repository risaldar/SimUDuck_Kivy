
import abc

# ========================= User Command Class =============================#

# Implements Command Pattern For Duck and Coop Classes.

class UserCommandClass():
    '''
    A class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract methods and properties are overridden.
    '''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self, *args):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass

    @abc.abstractmethod
    def undo(self, *args):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass


    @abc.abstractmethod
    def redo(self, *args):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass

# ----------------------------------------------
