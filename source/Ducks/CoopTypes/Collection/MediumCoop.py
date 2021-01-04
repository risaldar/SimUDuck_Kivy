
import abc

import CollectionsManager
from Ducks.CoopTypes.Coop import CoopClass

# ========================================= Coop Class ===================================#
class MediumCoopClass(CoopClass):

    def __init__(self):
        super(MediumCoopClass, self).__init__()
        print 'Initialized a new MediumCoop'

    def display(self):
        print ('I am a MediumCoop')

    def getColumns(self):
        return 1

    def getRows(self):
        return 4
# ----------------------------------------------
