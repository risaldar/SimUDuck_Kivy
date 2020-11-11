import abc
import os
import importlib

from Ducks.DuckTypes.Duck import DuckClass
from Ducks.DuckFlyBehaviors.FlyBehavior import FlyBehavior
from Ducks.DuckQuackBehaviors.QuackBehavior import QuackBehavior


# ====================================== Main ==============================#

AllDuckTypes = []
AllDuckColors = []
AllDuckFlyBehaviors = []
AllDuckQauckBehaviors = []

def getCollectionsRootPath(CollectionName):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Ducks\\' + CollectionName + '\Collection')


def loadCollections():
    global AllDuckTypes
    global AllDuckColors
    global AllDuckFlyBehaviors
    global AllDuckQauckBehaviors
    AllDuckTypes = []
    AllDuckColors = []
    AllDuckFlyBehaviors = []
    AllDuckQauckBehaviors = []
    # walk and collect classes
    for dirpath, dirnames, filenames in os.walk(getCollectionsRootPath('DuckTypes')):
        for filename in filenames:
            if filename != '__init__.py' and filename.endswith('.py'):
                AllDuckTypes.append(filename[:-3])
    for dirpath, dirnames, filenames in os.walk(getCollectionsRootPath('DuckColors')):
        for filename in filenames:
            if filename != '__init__.py' and filename.endswith('.py'):
                AllDuckColors.append(filename[:-3])
    for dirpath, dirnames, filenames in os.walk(getCollectionsRootPath('DuckFlyBehaviors')):
        for filename in filenames:
            if filename != '__init__.py' and filename.endswith('.py'):
                AllDuckFlyBehaviors.append(filename[:-3])
    for dirpath, dirnames, filenames in os.walk(getCollectionsRootPath('DuckQuackBehaviors')):
        for filename in filenames:
            if filename != '__init__.py' and filename.endswith('.py'):
                AllDuckQauckBehaviors.append(filename[:-3])
    print 'initialized CollectionsManager'

def createNewDuck(DuckTypeName):
    Module = importlib.import_module('Ducks.DuckTypes.Collection.' + DuckTypeName)
    DuckTypeClass = getattr(Module, DuckTypeName + 'Class')
    OneDuck = DuckTypeClass()
    return OneDuck

def createNewDuckColor(DuckColorName):
    Module = importlib.import_module('Ducks.DuckColors.Collection.' + DuckColorName)
    DuckColorClass = getattr(Module, DuckColorName + 'Class')
    OneDuckColor = DuckColorClass()
    return OneDuckColor

def createNewDuckFlyBehavior(DuckFlyBehaviorName):
    Module = importlib.import_module('Ducks.DuckFlyBehaviors.Collection.' + DuckFlyBehaviorName)
    DuckFlyBehaviorClass = getattr(Module, DuckFlyBehaviorName + 'Class')
    OneDuckFlyBehavior = DuckFlyBehaviorClass()
    return OneDuckFlyBehavior

def createNewDuckQuackBehavior(DuckQuackBehaviorName):
    Module = importlib.import_module('Ducks.DuckQuackBehaviors.Collection.' + DuckQuackBehaviorName)
    DuckQuackBehaviorClass = getattr(Module, DuckQuackBehaviorName + 'Class')
    OneDuckQuackBehavior = DuckQuackBehaviorClass()
    return OneDuckQuackBehavior

def getAllDuckTypes():
    global AllDuckTypes
    return AllDuckTypes

def getAllDuckColors():
    global AllDuckColors
    return AllDuckColors

def getAllDuckFlyBehaviors():
    global AllDuckFlyBehaviors
    return AllDuckFlyBehaviors

def getAllDuckQuackBehaviors():
    global AllDuckQauckBehaviors
    return AllDuckQauckBehaviors
# ----------------------------------------------