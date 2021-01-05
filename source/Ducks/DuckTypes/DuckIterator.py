
from DuckComponent import DuckComponentClass
from DuckComponentIterator import DuckComponentIteratorClass

# =================================== Duck Iterator Class ================================#
class DuckIteratorClass(DuckComponentIteratorClass):

    def __init__(self):
        print 'initialized a new duck iterator'

    def next(self):
        return None
# ----------------------------------------------
