import kivy

import abc
from time import time
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# ==================================================================
class FlyBehavior:
    '''
    A class that has a metaclass derived from ABCMeta cannot be 
    instantiated unless all of its abstract methods and properties are overridden.
    '''
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def fly(self):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass
# ----------------------------------------------
class FlyWithWings(FlyBehavior):
    def __init__(self):
        pass
    def fly(self):
        print 'I am flying with wings'
# ----------------------------------------------
class FlyNoWay(FlyBehavior):
    def __init__(self):
        pass
    def fly(self):
        print 'I can not fly'
# ==================================================================
class QuackBehavior:
    '''
    A class that has a metaclass derived from ABCMeta cannot be 
    instantiated unless all of its abstract methods and properties are overridden.
    '''
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def quack(self):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass
# ----------------------------------------------
class Quack(QuackBehavior):
    def __init__(self):
        pass
    def quack(self):
        print 'I quack'
# ----------------------------------------------
class Squeak(QuackBehavior):
    def __init__(self):
        pass
    def quack(self):
        print 'I squeak'
# ----------------------------------------------
class MuteQuack(QuackBehavior):
    def __init__(self):
        pass
    def quack(self):
        print 'I am mute'
# ==================================================================
class DuckClass:
    flyBehavior = None
    quackBehavior = None
    def __init__(self):
        print 'initialized a new Duck'

    def setFlyBehavior(self, behavior):
        self.flyBehavior = behavior

    def setQuackBehavior(self, behavior):
        self.quackBehavior = behavior

    def performFly(self):
        self.flyBehavior.fly()

    def quackFly(self):
        self.quackBehavior.quack()
# ----------------------------------------------
class MallardDuckClass(DuckClass):
    def __init__(self):
        print 'initialized a new Mallard Duck'
    def display(self):
        print 'I am a Mallard Duck'
# ----------------------------------------------
class ReadheadDuckClass(DuckClass):
    def __init__(self):
        print 'initialized a new Readhead Duck'
    def display(self):
        print 'I am a Readhead Duck'
# ----------------------------------------------
class RubberDuckClass(DuckClass):
    def __init__(self):
        print 'initialized a new Rubber Duck'
    def display(self):
        print 'I am a Rubber Duck'
# ----------------------------------------------
class DecoyDuckClass(DuckClass):
    def __init__(self):
        print 'initialized a new Decoy Duck'
    def display(self):
        print 'I am a Decoy Duck'
# ==================================================================
class MyApp(App):

    AllDucks = []

    def ButtonPressed(self, instance):
        print 'ButtonPressed'

    def build(self):
        self.title = 'SimUDuck'
        
        wid = Widget()

        label = Label(text='0')

        btn_addMallardDuck = Button(text='Add a new Mallard Duck', on_press=self.ButtonPressed)
        btn_addReadheadDuck = Button(text='Add a new Readhead Duck', on_press=self.ButtonPressed)
        btn_addRubberDuck = Button(text='Add a new Rubber Duck', on_press=self.ButtonPressed)
        btn_addDecoyDuck = Button(text='Add a new Decoy Duck', on_press=self.ButtonPressed)

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(btn_addMallardDuck)
        layout.add_widget(btn_addReadheadDuck)
        layout.add_widget(btn_addRubberDuck)
        layout.add_widget(btn_addDecoyDuck)
        layout.add_widget(label)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

        return root

    def _update_clock(self, dt):
        self.time = time()

if __name__ == '__main__':
    MyApp().run()