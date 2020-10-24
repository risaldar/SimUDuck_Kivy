import kivy

import abc
from time import time
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp


# ============================= Fly Behavior =====================================#
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

# ======================================= Quack Behavior ==================================#
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

# ========================================= Duck Class ===================================#
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

    def performQuack(self):
        self.quackBehavior.quack()
# ----------------------------------------------
class MallardDuckClass(DuckClass):
    def __init__(self):
        print 'Initialized a new Mallard Duck'
    def display(self):
        print ('I am a Mallard Duck')
# ----------------------------------------------
class ReadheadDuckClass(DuckClass):
    def __init__(self):
        print 'Initialized a new Readhead Duck'
    def display(self):
        print ('I am a Readhead Duck')
# ----------------------------------------------
class RubberDuckClass(DuckClass):
    def __init__(self):
        print 'Initialized a new Rubber Duck'
    def display(self):
        print ('I am a Rubber Duck')
# ----------------------------------------------
class DecoyDuckClass(DuckClass):
    def __init__(self):
        print 'Initialized a new Decoy Duck'
    def display(self):
        print ('I am a Decoy Duck')

# ====================================== Main ==============================#
class MyApp(App):

    AllDucks = []

    TD_label = Label(text="Total Ducks = " + str(len(AllDucks)), size_hint=(0.5, 0.2), halign="left", valign="middle")

    def Add_MallardDuck(self, instance):
        print 'Add_MallardDuck'
        New_Mallard = MallardDuckClass()
        self.AllDucks.append(New_Mallard)

    def Add_RedHeadDuck(self, instance):
        print 'Add_RedHeadDuck'
        New_RedHead = ReadheadDuckClass()
        self.AllDucks.append(New_RedHead)

    def Ass_RubberDuck(self, instance):
        print 'Ass_RubberDuck'
        New_Rubber = RubberDuckClass()
        self.AllDucks.append(New_Rubber)

    def Add_DecoyDuck(self, instance):
        print 'Add_DecoyDuck'
        New_Decoy = DecoyDuckClass()
        self.AllDucks.append(New_Decoy)

    def Total_Ducks(self, instance):
        print 'Total Ducks are ' + str(len(self.AllDucks))
        for idx,x in enumerate(self.AllDucks):
            print str(idx) + '. '
            x.display()

    def SetFlyBehavior(self, instance):
        self.Total_Ducks(self)
        if(len(self.AllDucks) > 0):
            duck_index=input("Select Duck Index\n")
            if(duck_index < len(self.AllDucks)):
                Duck_fly_behvaior = input("Select Fly Behavior\n1. Fly with Wings\n2. Cant Fly\n")
                if(Duck_fly_behvaior ==1):
                    Fly = FlyWithWings()
                    self.AllDucks[int(duck_index)].setFlyBehavior(Fly)
                elif(Duck_fly_behvaior ==  2):
                    NoFly = FlyNoWay()
                    self.AllDucks[int(duck_index)].setFlyBehavior(NoFly)
                else:
                    print("Wrong Behavior Selected\n")
            else:
                print("Wrong Index\n")

    def SetQuackBehavior(self, instance):
        self.Total_Ducks(self)
        if(len(self.AllDucks) > 0):
            duck_index=input("Select Duck Index  ")
            if(duck_index < len(self.AllDucks)):
                Duck_quack_behvaior = input("Select Quack Behavior\n1. Quack\n2. Squeak\n3. MuteQuack\n")
                if (Duck_quack_behvaior == 1):
                    In_Quack = Quack()
                    self.AllDucks[int(duck_index)].setFlyBehavior(In_Quack)
                elif(Duck_quack_behvaior == 2):
                    In_Squeak = Squeak()
                    self.AllDucks[int(duck_index)].setFlyBehavior(In_Squeak)
                elif(Duck_quack_behvaior ==  3):
                    In_Mute = MuteQuack()
                    self.AllDucks[int(duck_index)].setFlyBehavior(In_Mute)
                else:
                    print("Wrong Behavior Selected\n")
            else:
                print "Worng Index\n"

    def SpawnDuck(self, instance):
        self.Total_Ducks(self)
        if(len(self.AllDucks) >0):
            duck_index=input("Select Duck Index  ")
            if(duck_index < len(self.AllDucks)):
                if(self.AllDucks[int(duck_index)].flyBehavior != None):
                    self.AllDucks[int(duck_index)].performFly()
                else:
                    print("No Fly Behavior")

                if(self.AllDucks[int(duck_index)].quackBehavior != None):
                    self.AllDucks[int(duck_index)].performQuack()
                else:
                    print("No Quack behavior")
            else:
                print("Wrong Index\n")

    def UpdateLabel(self, label):
        self.TD_label.text="Total Ducks = " + str(len(self.AllDucks))

    def build(self):
        self.title = 'SimUDuck'

        Clock.schedule_interval(self.UpdateLabel, 0.2)

        btn_addMallardDuck = Button(text='Add a new Mallard Duck', on_press=self.Add_MallardDuck,size_hint=(0.5, 0.2), halign="left", valign="middle")
        btn_addReadheadDuck = Button(text='Add a new Readhead Duck', on_press=self.Add_RedHeadDuck,size_hint=(0.5, 0.2), halign="left", valign="middle")
        btn_addRubberDuck = Button(text='Add a new Rubber Duck', on_press=self.Ass_RubberDuck,size_hint=(0.5, 0.2), halign="left", valign="middle")
        btn_addDecoyDuck = Button(text='Add a new Decoy Duck', on_press=self.Add_DecoyDuck,size_hint=(0.5, 0.2), halign="left", valign="middle")
        btn_totalducks = Button(text='Total Ducks', on_press=self.Total_Ducks,size_hint=(0.5, 0.2), halign="left", valign="middle")
        btn_setFlyBehavior = Button(text='Set Fly Behavior', on_press=self.SetFlyBehavior,size_hint=(0.5, 0.2), halign="left", valign="middle")
        btn_setQuackBehavior = Button(text='Set Quack Behavior', on_press=self.SetQuackBehavior,size_hint=(0.5, 0.2), halign="left", valign="middle")
        btn_SpawnDuck = Button(text='Spawn Duck', on_press=self.SpawnDuck,size_hint=(0.5, 0.2), halign="left", valign="middle")

        layout = BoxLayout()
        layout.add_widget(btn_addMallardDuck)
        layout.add_widget(btn_addReadheadDuck)
        layout.add_widget(btn_addRubberDuck)
        layout.add_widget(btn_addDecoyDuck)
        layout.add_widget(btn_totalducks)
        layout.add_widget(btn_setFlyBehavior)
        layout.add_widget(btn_setQuackBehavior)
        layout.add_widget(btn_SpawnDuck)
        layout.add_widget(self.TD_label)

        root = BoxLayout(orientation='vertical')
        root.add_widget(layout)

        return root

if __name__ == '__main__':
    MyApp().run()