import CollectionsManager
from UserController.UserCommand import UserCommandClass
from Ducks.CoopTypes.Coop import CoopClass

# ==================================== UserCommandAddDecoration Class =================================#
class UserCommandAddDecoration(UserCommandClass):
    
    decoration = None
    decorated_component = None
    component_selected = None
    component_selected_new = None
    component_parent = None
    component_grandparent = None
    
    def __init__(self):
        print 'Initialized a new user command: UserCommandAddDecoration'

    def addCompositeDecoration(self, component, color):
        for child_component in component.ChildDuckComponents:
            if isinstance(child_component, CoopClass):
                self.addCompositeDecoration(child_component, color)
            else:
                decorated_component = CollectionsManager.createNewDuckComponentDecorator(color, child_component)
                component.replaceDuckComponent(child_component, decorated_component)

    def addDecoration(self, component, color):
        for child_component in component.ChildDuckComponents:
            if child_component == self.component_selected:
                self.component_parent = component
                if isinstance(child_component, CoopClass):
                    self.addCompositeDecoration(child_component, color)
                    self.component_selected_new = self.component_selected
                else:
                    self.decorated_component = CollectionsManager.createNewDuckComponentDecorator(color, child_component)
                    component.replaceDuckComponent(child_component, self.decorated_component)
                    self.component_selected_new = self.decorated_component
                return True
            elif isinstance(child_component, CoopClass):
                if self.addDecoration(child_component, color) is True:
                    return True
            else:
                pass
        return False

    def execute(self, *args):
        self.decoration = args[0][0]
        self.component_selected = args[0][1]
        self.component_grandparent = args[0][2]
        for component in self.component_grandparent:
            if component == self.component_selected:
                if isinstance(component, CoopClass):
                    self.addCompositeDecoration(component, self.decoration)
                    self.component_grandparent = None
                    self.component_parent = component
                    self.component_selected_new = self.component_selected
                else:
                    component_index = self.component_grandparent.index(component)
                    self.component_grandparent.remove(component)
                    self.decorated_component = CollectionsManager.createNewDuckComponentDecorator(self.decoration, component)
                    self.component_grandparent.insert(component_index, self.decorated_component)
                    self.component_parent = None
                    self.component_selected_new = self.decorated_component
            elif isinstance(component, CoopClass):
                if self.addDecoration(component, self.decoration) is True:
                    self.component_grandparent = None
                    break
            else:
                pass
        return self.component_selected_new
    
    def removeCompositeDecoration(self, component):
        for child_component in component.ChildDuckComponents:
            if isinstance(child_component, CoopClass):
                self.removeCompositeDecoration(child_component)
            else:
                component.replaceDuckComponent(child_component, child_component.WrappedDuckComponent)

    def removeDecoration(self, component):
        for child_component in component.ChildDuckComponents:
            if child_component == self.component_selected_new:
                if isinstance(child_component, CoopClass):
                    self.removeCompositeDecoration(child_component)
                else:
                    component.replaceDuckComponent(child_component, child_component.WrappedDuckComponent)
                return True
            elif isinstance(child_component, CoopClass):
                if self.removeDecoration(child_component) is True:
                    return True
            else:
                pass
        return False

    def undo(self, *args):
        if self.component_grandparent is not None:
            if isinstance(self.component_selected, CoopClass):
                self.removeCompositeDecoration(self.component_selected)
            else:
                component_index = self.component_grandparent.index(self.decorated_component)
                self.component_grandparent.remove(self.decorated_component)
                self.component_grandparent.insert(component_index, self.component_selected)
        elif self.component_parent is not None:
            self.removeCompositeDecoration(self.component_parent)
        else:
            pass
        return self.component_selected
    
    def redo(self, *args):
        if self.component_grandparent is not None:
            if isinstance(self.component_selected, CoopClass):
                self.addCompositeDecoration(self.component_selected, self.decoration)
            else:
                component_index = self.component_grandparent.index(self.component_selected)
                self.component_grandparent.remove(self.component_selected)
                self.component_grandparent.insert(component_index, self.decorated_component)
        elif self.component_parent is not None:
            if isinstance(self.component_selected, CoopClass):
                self.addCompositeDecoration(self.component_parent, self.decoration)
            else:
                self.addDecoration(self.component_selected, self.decoration)
        else:
            pass
        return self.component_selected_new

# ----------------------------------------------
