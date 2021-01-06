import os
import importlib

from DuckComponent import DuckComponentClass
from DuckComponentIterator import DuckComponentIteratorClass

# =================================== Coop Iterator Class ================================#
class CoopIteratorClass(DuckComponentIteratorClass):

    IteratorStack = None

    def __init__(self, iterator):
        self.IteratorStack = []
        self.IteratorStack.append(iterator)
        print 'initialized a new coop iterator'

    def next(self):
        if len(self.IteratorStack) == 0:
            return None
        try:
            iterator = self.IteratorStack[-1]
            component = iterator.next()
            if component is None:
                self.IteratorStack.pop()
                return self.next()
            if 'CoopClass' in component.__class__.__name__:
                component_iterator = component.createIterator()
                self.IteratorStack.append(component_iterator)
                return self.next()
            return component
        except:
            self.IteratorStack.pop()
            return self.next()
# ----------------------------------------------
