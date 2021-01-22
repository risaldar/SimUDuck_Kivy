import abc
import os
import importlib
from xml.dom import minidom
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
import xml.etree.ElementTree as ET

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
AllDatabaseComponents = []

def getDuckCollectionsRootPath(CollectionName):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Ducks\\' + CollectionName + '\Collection')

def getDecorationCollectionsRootPath(CollectionName):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), CollectionName + '\Collection')

def getDatabaseRootPath(CollectionName):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), CollectionName + '\Collection')

def loadCollections():
    global AllCoopTypes
    global AllDuckTypes
    global AllDuckComponentDecorators
    global AllDuckFlyBehaviors
    global AllDuckQauckBehaviors
    global AllDatabaseComponents
    AllCoopTypes = []
    AllDuckTypes = []
    AllDuckComponentDecorators = []
    AllDuckFlyBehaviors = []
    AllDuckQauckBehaviors = []
    AllDatabaseComponents = []
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
    if os.path.exists(os.path.join(getDatabaseRootPath('Database'), 'Components.xml')):
        try:
            tree = ET.parse(os.path.join(getDatabaseRootPath('Database'), 'Components.xml'))
            root = tree.getroot()
            for child in root:
                AllDatabaseComponents.append(getComponentFromDatabase(child))
        except:
            print 'ERROR: Failed to load database'
            createNewDatabase()
    else:
        os.makedirs(getDatabaseRootPath('Database'))
        createNewDatabase()

def getComponentFromDatabase(component_root):
    if 'Decorator' in component_root.tag:
        component = createNewDuckComponentDecorator(component_root.tag, None)
        # we know decorator has exactly one wrapped component
        for child_component in component_root:
            component.WrappedDuckComponent = getComponentFromDatabase(child_component)
    elif 'Coop' in component_root.tag:
        component = createNewCoop(component_root.tag)
        for child_component in component_root:
            print child_component.tag
            component.addDuckComponent(getComponentFromDatabase(child_component))
    else:
        component = createNewDuck(component_root.tag)
        component.setFlyBehavior(createNewDuckFlyBehavior(component_root.attrib["flyBehavior"]))
        component.setQuackBehavior(createNewDuckQuackBehavior(component_root.attrib["quackBehavior"]))
    return component

def createNewDatabase():
    with open(os.path.join(getDatabaseRootPath('Database'), 'Components.xml'), "w") as f:
        pass

def addComponentToDatabase(root, component):
    component_subelement = SubElement(root, component.__class__.__name__[:-len("Class")])
    if 'Decorator' in component.__class__.__name__:
        addComponentToDatabase(component_subelement, component.WrappedDuckComponent)
    elif 'Coop' in component.__class__.__name__:
        for child_component in component.ChildDuckComponents:
            addComponentToDatabase(component_subelement, child_component)
    else:
        component_subelement.set("flyBehavior", component.flyBehavior.__class__.__name__[:-len("Class")])
        component_subelement.set("quackBehavior", component.quackBehavior.__class__.__name__[:-len("Class")])

def saveDatabase(AllBaseComponents):
    root = Element('AllDuckTypeLayout_ChildDuckComponents')
    for OneBaseComponent in AllBaseComponents:
        addComponentToDatabase(root, OneBaseComponent)
    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    with open(os.path.join(getDatabaseRootPath('Database'), 'Components.xml'), "w") as f:
        f.write(xmlstr.encode('utf-8'))

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
    name = DuckComponentDecoratorName
    if name.startswith("DuckComponentDecorator"):
        name = name[len("DuckComponentDecorator"):]
    Module = importlib.import_module('DuckComponentDecorators.Collection.DuckComponentDecorator' + name)
    DuckComponentDecoratorClass = getattr(Module, 'DuckComponentDecorator' + name + 'Class')
    OneDuckComponentDecorator = DuckComponentDecoratorClass(component)
    return OneDuckComponentDecorator

def getDatabase():
    global AllDatabaseComponents
    return AllDatabaseComponents

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