
import abc

import CollectionsManager
from Ducks.DuckTypes.Duck import DuckClass

# ========================================= Duck Class ===================================#
class MallardDuckClass(DuckClass):
    def __init__(self):
        # this is default behavior
        self.setFlyBehavior(CollectionsManager.createNewDuckFlyBehavior('FlyWithWings'))
        self.setQuackBehavior(CollectionsManager.createNewDuckQuackBehavior('Quack'))
        print 'Initialized a new Mallard Duck'
    def display(self):
        print ('I am a Mallard Duck')
# ----------------------------------------------
