
import abc

import CollectionsManager
from Ducks.CoopTypes.Coop import CoopClass

# ========================================= Coop Class ===================================#
class VerticalCoopClass(CoopClass):

    def __init__(self):
        super(VerticalCoopClass, self).__init__()
        print 'Initialized a new VerticalCoop'
        
    def display(self):
        print ('I am a VerticalCoop')

    def getColumns(self):
        return 1

    def getRows(self):
        return 4
# ----------------------------------------------
