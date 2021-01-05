import os
import importlib

from DuckComponent import DuckComponentClass
from DuckComponentIterator import DuckComponentIteratorClass

# =================================== Coop Iterator Class ================================#
class CoopIteratorClass(DuckComponentIteratorClass):

    IteratorStack = []

    def __init__(self, iterator):
        self.IteratorStack.append(iterator)
        print 'initialized a new coop iterator'

    def next(self):
        Module = importlib.import_module('Ducks.CoopTypes.Coop')
        CoopClass = getattr(Module, 'CoopClass')
        if len(self.IteratorStack) == 0:
            return None
        try:
            iterator = self.IteratorStack[-1]
            component = iterator.next()
            if type(component) is CoopClass:
                self.IteratorStack.append(component.createIterator())
            return component
        except:
            self.IteratorStack.pop()
            return self.next()
# ----------------------------------------------
