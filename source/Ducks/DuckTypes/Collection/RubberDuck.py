
import abc

import CollectionsManager
from Ducks.DuckTypes.Duck import DuckClass

# ========================================= Duck Class ===================================#
class RubberDuckClass(DuckClass):
    def __init__(self):
        # this is default behavior
        self.setFlyBehavior(CollectionsManager.createNewDuckFlyBehavior('FlyNoWay'))
        self.setQuackBehavior(CollectionsManager.createNewDuckQuackBehavior('Squeak'))
        print 'Initialized a new Rubber Duck'
    def display(self):
        print ('I am a Rubber Duck')
# ----------------------------------------------
