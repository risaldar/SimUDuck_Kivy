import CollectionsManager
from UserController.UserCommand import UserCommandClass
from Ducks.CoopTypes.Coop import CoopClass

# ==================================== UserCommandRemoveDuckComponent Class =================================#
class UserCommandRemoveDuckComponent(UserCommandClass):
    
    component = None
    component_parent = None
    component_grandparent = None
    component_index = 0
    
    def __init__(self):
        print 'Initialized a new user command: UserCommandRemoveDuckComponent'
    
    def removeDuckComponent(self, component):
        for child_component in component.ChildDuckComponents:
            if child_component == self.component:
                self.component_index = component.removeDuckComponent(child_component)
                self.component_parent = component
                self.component_grandparent = None
                return True
            elif isinstance(child_component, CoopClass):
                if self.removeDuckComponent(child_component) is True:
                    return True
            else:
                pass
        return False

    def execute(self, *args):
        self.component = args[0][0]
        self.component_grandparent = args[0][1]
        for component in self.component_grandparent:
            if component == self.component:
                self.component_parent = None
                self.component_index = self.component_grandparent.index(self.component)
                self.component_grandparent.remove(component)
            elif isinstance(component, CoopClass):
                if self.removeDuckComponent(component) is True:
                    break
            else:
                pass
    
    def undo(self, *args):
        if self.component_grandparent is not None:
            self.component_grandparent.insert(self.component_index, self.component)
        elif self.component_parent is not None:
            self.component_parent.addDuckComponent(self.component, self.component_index)
        else:
            pass
    
    def redo(self, *args):
        if self.component_grandparent is not None:
            self.component_index = self.component_grandparent.index(self.component)
            self.component_grandparent.remove(self.component)
        elif self.component_parent is not None:
            self.component_index = self.component_parent.removeDuckComponent(self.component)
        else:
            pass

# ----------------------------------------------
