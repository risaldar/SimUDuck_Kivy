
import abc

import CollectionsManager
from Ducks.CoopTypes.Coop import CoopClass

# ========================================= Coop Class ===================================#
class MegaCoopClass(CoopClass):

    def __init__(self):
        super(MegaCoopClass, self).__init__()
        print 'Initialized a new MegaCoop'

    def display(self):
        print ('I am a MegaCoop')

    def getColumns(self):
        return 10

    def getRows(self):
        return 2
# ----------------------------------------------
