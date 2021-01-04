
import abc

import CollectionsManager
from Ducks.DuckTypes.Duck import DuckClass

# ========================================= Duck Class ===================================#
class ReadheadDuckClass(DuckClass):
    def __init__(self):
        # this is default behavior
        self.setFlyBehavior(CollectionsManager.createNewDuckFlyBehavior('FlyWithWings'))
        self.setQuackBehavior(CollectionsManager.createNewDuckQuackBehavior('Quack'))
        print 'Initialized a new Readhead Duck'
    def display(self):
        print ('I am a Readhead Duck')
# ----------------------------------------------
