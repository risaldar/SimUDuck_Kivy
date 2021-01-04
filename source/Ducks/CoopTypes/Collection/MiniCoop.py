
import abc

import CollectionsManager
from Ducks.CoopTypes.Coop import CoopClass

# ========================================= Coop Class ===================================#
class MiniCoopClass(CoopClass):

    def __init__(self):
        super(MiniCoopClass, self).__init__()
        print 'Initialized a new MiniCoop'

    def display(self):
        print ('I am a MiniCoop')

    def getColumns(self):
        return 1

    def getRows(self):
        return 1
# ----------------------------------------------
