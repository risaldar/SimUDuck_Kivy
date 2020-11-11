
import abc

import CollectionsManager
from Ducks.DuckTypes.Duck import DuckClass

# ========================================= Duck Class ===================================#
class DecoyDuckClass(DuckClass):
    def __init__(self):
        # this is default behavior
        self.setFlyBehavior(CollectionsManager.createNewDuckFlyBehavior('FlyNoWay'))
        self.setQuackBehavior(CollectionsManager.createNewDuckQuackBehavior('MuteQuack'))
        print 'Initialized a new Decoy Duck'
    def display(self):
        print ('I am a Decoy Duck')
# ----------------------------------------------
