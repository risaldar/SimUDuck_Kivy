
import abc

import CollectionsManager
from Ducks.CoopTypes.Coop import CoopClass

# ========================================= Coop Class ===================================#
class SmallCoopClass(CoopClass):
    
    def __init__(self):
        super(SmallCoopClass, self).__init__()
        print 'Initialized a new SmallCoop'

    def display(self):
        print ('I am a SmallCoop')

    def getColumns(self):
        return 2

    def getRows(self):
        return 1
# ----------------------------------------------
