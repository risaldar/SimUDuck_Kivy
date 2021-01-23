import CollectionsManager
from UserController.UserCommand import UserCommandClass
from Ducks.CoopTypes.Coop import CoopClass

# ==================================== UserCommandSetQuackBehavior Class =================================#
class UserCommandSetQuackBehavior(UserCommandClass):
    
    new_behavior = None
    previous_behavior = None
    component = None

    def __init__(self):
        print 'Initialized a new user command: UserCommandSetQuackBehavior'

    def execute(self, *args):
        self.component = args[0][1]
        if not isinstance(self.component, CoopClass):
            self.previous_behavior = self.component.quackBehavior
        else:
            self.previous_behavior = None
        self.new_behavior = CollectionsManager.createNewDuckQuackBehavior(args[0][0])
        self.component.setQuackBehavior(self.new_behavior)

    def undo(self, *args):
        if self.previous_behavior is not None:
            self.component.setQuackBehavior(self.previous_behavior)

    def redo(self, *args):
        self.component.setQuackBehavior(self.new_behavior)

# ----------------------------------------------
