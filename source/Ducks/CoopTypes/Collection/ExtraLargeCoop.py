
import abc

import CollectionsManager
from Ducks.CoopTypes.Coop import CoopClass

# ========================================= Coop Class ===================================#
class ExtraLargeCoopClass(CoopClass):

    def __init__(self):
        super(ExtraLargeCoopClass, self).__init__()
        print 'Initialized a new ExtraLargeCoop'
        
    def display(self):
        print ('I am a ExtraLargeCoop')

    def getColumns(self):
        return 4

    def getRows(self):
        return 4
# ----------------------------------------------
