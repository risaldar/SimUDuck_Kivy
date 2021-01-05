import abc
import os
import importlib

from Ducks.CoopTypes.Coop import CoopClass
from Ducks.DuckTypes.Duck import DuckClass
from Ducks.DuckFlyBehaviors.FlyBehavior import FlyBehavior
from Ducks.DuckQuackBehaviors.QuackBehavior import QuackBehavior


# ====================================== Main ==============================#

AllCoopTypes = []
AllDuckTypes = []
AllDuckComponentDecorators = []
AllDuckFlyBehaviors = []
AllDuckQauckBehaviors = []

def getDuckCollectionsRootPath(CollectionName):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Ducks\\' + CollectionName + '\Collection')

def getDecorationCollectionsRootPath(CollectionName):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), CollectionName + '\Collection')


def loadCollections():
    global AllCoopTypes
    global AllDuckTypes
    global AllDuckComponentDecorators
    global AllDuckFlyBehaviors
    global AllDuckQauckBehaviors
    AllCoopTypes = []
    AllDuckTypes = []
    AllDuckComponentDecorators = []
    AllDuckFlyBehaviors = []
    AllDuckQauckBehaviors = []
    # walk and collect classes
    for dirpath, dirnames, filenames in os.walk(getDuckCollectionsRootPath('CoopTypes')):
        for filename in filenames:
            if filename != '__init__.py' and filename.endswith('.py'):
                AllCoopTypes.append(filename[:-3])
    for dirpath, dirnames, filenames in os.walk(getDuckCollectionsRootPath('DuckTypes')):
        for filename in filenames:
            if filename != '__init__.py' and filename.endswith('.py'):
                AllDuckTypes.append(filename[:-3])
    for dirpath, dirnames, filenames in os.walk(getDuckCollectionsRootPath('DuckFlyBehaviors')):
        for filename in filenames:
            if filename != '__init__.py' and filename.endswith('.py'):
                AllDuckFlyBehaviors.append(filename[:-3])
    for dirpath, dirnames, filenames in os.walk(getDuckCollectionsRootPath('DuckQuackBehaviors')):
        for filename in filenames:
            if filename != '__init__.py' and filename.endswith('.py'):
                AllDuckQauckBehaviors.append(filename[:-3])
    for dirpath, dirnames, filenames in os.walk(getDecorationCollectionsRootPath('DuckComponentDecorators')):
        for filename in filenames:
            if filename != '__init__.py' and filename.endswith('.py'):
                AllDuckComponentDecorators.append(filename[len('DuckComponentDecorator'):-3])

def createNewCoop(CoopTypeName):
    Module = importlib.import_module('Ducks.CoopTypes.Collection.' + CoopTypeName)
    CoopTypeClass = getattr(Module, CoopTypeName + 'Class')
    OneCoop = CoopTypeClass()
    return OneCoop

def createNewDuck(DuckTypeName):
    Module = importlib.import_module('Ducks.DuckTypes.Collection.' + DuckTypeName)
    DuckTypeClass = getattr(Module, DuckTypeName + 'Class')
    OneDuck = DuckTypeClass()
    return OneDuck

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

def createNewDuckComponentDecorator(DuckComponentDecoratorName, component):
    Module = importlib.import_module('DuckComponentDecorators.Collection.DuckComponentDecorator' + DuckComponentDecoratorName)
    DuckComponentDecoratorClass = getattr(Module, 'DuckComponentDecorator' + DuckComponentDecoratorName + 'Class')
    OneDuckComponentDecorator = DuckComponentDecoratorClass(component)
    return OneDuckComponentDecorator

def getAllCoopTypes():
    global AllCoopTypes
    return AllCoopTypes

def getAllDuckTypes():
    global AllDuckTypes
    return AllDuckTypes

def getAllDuckFlyBehaviors():
    global AllDuckFlyBehaviors
    return AllDuckFlyBehaviors

def getAllDuckQuackBehaviors():
    global AllDuckQauckBehaviors
    return AllDuckQauckBehaviors

def getAllDuckComponentDecorators():
    global AllDuckComponentDecorators
    return AllDuckComponentDecorators

def getAllDuckDecorations():
    return ['Red', 'Blue', 'Yellow']

# ----------------------------------------------