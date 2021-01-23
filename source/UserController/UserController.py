
# ========================= User Controller Class =============================#

# Implements Command Pattern For Duck and Coop Classes.

class UserControllerClass():

    CommandUndoStack = []
    CommandRedoStack = []
    CommandDictionary = {}

    def __init__(self):
        print 'initialized a new UserController'

    def setCommand(self, name, command_object):
        print ' > setting command : ' + name
        self.CommandDictionary[name] = command_object

    def doCommand(self, name, *args):
        print ' > running command : ' + name
        ret = self.CommandDictionary[name].execute(args)
        self.CommandRedoStack = []
        self.CommandUndoStack.append(self.CommandDictionary[name])
        return ret

    def undoCommand(self):
        if len(self.CommandUndoStack) > 0:
            command_object = self.CommandUndoStack.pop()
            print ' > undoing command : ' + command_object.__class__.__name__
            command_object.undo()
            self.CommandRedoStack.append(command_object)

    def redoCommand(self):
        if len(self.CommandRedoStack) > 0:
            command_object = self.CommandRedoStack.pop()
            print ' > redoing command : ' + command_object.__class__.__name__
            command_object.redo()
            self.CommandUndoStack.append(command_object)

# ----------------------------------------------
