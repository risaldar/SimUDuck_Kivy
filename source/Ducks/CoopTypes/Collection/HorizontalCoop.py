
import abc

import CollectionsManager
from Ducks.CoopTypes.Coop import CoopClass

# ========================================= Coop Class ===================================#
class HorizontalCoopClass(CoopClass):

    def __init__(self):
        super(HorizontalCoopClass, self).__init__()
        print 'Initialized a new HorizontalCoop'
        
    def display(self):
        print ('I am a HorizontalCoop')

    def getColumns(self):
        return 4

    def getRows(self):
        return 1
# ----------------------------------------------
