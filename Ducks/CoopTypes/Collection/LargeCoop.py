
import abc

import CollectionsManager
from Ducks.CoopTypes.Coop import CoopClass

# ========================================= Coop Class ===================================#
class LargeCoopClass(CoopClass):

    def __init__(self):
        super(LargeCoopClass, self).__init__()
        print 'Initialized a new LargeCoop'

    def display(self):
        print ('I am a LargeCoop')

    def getColumns(self):
        return 3

    def getRows(self):
        return 3
# ----------------------------------------------
