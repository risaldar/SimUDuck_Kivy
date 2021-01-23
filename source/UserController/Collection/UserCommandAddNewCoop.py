import CollectionsManager
from UserController.UserCommand import UserCommandClass

# ==================================== UserCommandAddNewCoop Class =================================#
class UserCommandAddNewCoop(UserCommandClass):
    
    component = None
    component_index = 0
    component_selected = None
    component_parent = None
    
    def __init__(self):
        print 'Initialized a new user command: UserCommandAddNewCoop'
    
    def execute(self, *args):
        self.component_selected = args[0][1]
        self.component = CollectionsManager.createNewCoop(args[0][0])
        if self.component_selected is None or self.component_selected.addDuckComponent(self.component) == False:
            self.component_parent = args[0][2]
            self.component_parent.append(self.component)
    
    def undo(self, *args):
        self.component_index = -1
        if self.component_selected is not None:
            self.component_index = self.component_selected.removeDuckComponent(self.component)
        if self.component_index < 0:
            self.component_parent.remove(self.component)
    
    def redo(self, *args):
        if self.component_selected is None or self.component_selected.addDuckComponent(self.component, self.component_index) == False:
            self.component_parent.append(self.component)

# ----------------------------------------------
