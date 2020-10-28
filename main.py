import kivy

import abc
from time import time
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


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
    @abc.abstractmethod
    def getDetails(self):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass
# ----------------------------------------------
class FlyWithWings(FlyBehavior):
    details = 'I can fly with Wings'
    def __init__(self):
        pass
    def fly(self):
        print 'I am flying with wings'
    def getDetails(self):
        return self.details
# ----------------------------------------------
class FlyNoWay(FlyBehavior):
    details = 'I have no wings'
    def __init__(self):
        pass
    def fly(self):
        print 'I can not fly'
    def getDetails(self):
        return self.details

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
    @abc.abstractmethod
    def getDetails(self):
        # Will get a TypeError if this method is not implemented by
        # concrete class.
        pass
# ----------------------------------------------
class Quack(QuackBehavior):
    details = 'I can quack'
    def __init__(self):
        pass
    def quack(self):
        print 'I quack'
    def getDetails(self):
        return self.details
# ----------------------------------------------
class Squeak(QuackBehavior):
    details = 'I can squeak'
    def __init__(self):
        pass
    def quack(self):
        print 'I squeak'
    def getDetails(self):
        return self.details
# ----------------------------------------------
class MuteQuack(QuackBehavior):
    details = 'I am mute'
    def __init__(self):
        pass
    def quack(self):
        print 'I am mute'
    def getDetails(self):
        return self.details

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
        self.setFlyBehavior(FlyWithWings())
        self.setQuackBehavior(Quack())
    def display(self):
        print ('I am a Mallard Duck')
# ----------------------------------------------
class ReadheadDuckClass(DuckClass):
    def __init__(self):
        print 'Initialized a new Readhead Duck'
        self.setFlyBehavior(FlyWithWings())
        self.setQuackBehavior(Quack())
    def display(self):
        print ('I am a Readhead Duck')
# ----------------------------------------------
class RubberDuckClass(DuckClass):
    def __init__(self):
        print 'Initialized a new Rubber Duck'
        self.setFlyBehavior(FlyNoWay())
        self.setQuackBehavior(Squeak())
    def display(self):
        print ('I am a Rubber Duck')
# ----------------------------------------------
class DecoyDuckClass(DuckClass):
    def __init__(self):
        print 'Initialized a new Decoy Duck'
        self.setFlyBehavior(FlyNoWay())
        self.setQuackBehavior(MuteQuack())
    def display(self):
        print ('I am a Decoy Duck')

# ====================================== Main ==============================#
class MyApp(App):

    AllDucks = []
    Duck_Buttons = []

    TD_label = Label(text="Total Ducks = " + str(len(AllDucks)), size_hint=(0.5, 0.2), halign="left", valign="middle")
    layout_Mallard = BoxLayout()
    layout_RedHead = BoxLayout()
    layout_RubberDuck = BoxLayout()
    layout_DecoyDuck = BoxLayout()

    def btnCbk_addMallardDuck(self, instance):
        New_Mallard = MallardDuckClass()
        self.AllDucks.append(New_Mallard)
        details = "Mallard Duck\n" + New_Mallard.flyBehavior.getDetails() + "\n" + New_Mallard.quackBehavior.getDetails()
        dummy_duck = Button(text=details, size_hint=(.2, 1))
        self.Duck_Buttons.append(dummy_duck)
        self.layout_Mallard.add_widget(dummy_duck)

    def btnCbk_addReadheadDuck(self, instance):
        New_RedHead = ReadheadDuckClass()
        self.AllDucks.append(New_RedHead)
        details = "Red Head  Duck\n" + New_RedHead.flyBehavior.getDetails() + "\n" + New_RedHead.quackBehavior.getDetails()
        dummy_duck = Button(text=details, size_hint=(.2, 1))
        self.Duck_Buttons.append(dummy_duck)
        self.layout_RedHead.add_widget(dummy_duck)


    def btnCbk_addRubberDuck(self, instance):
        New_Rubber = RubberDuckClass()
        self.AllDucks.append(New_Rubber)
        details = "Rubber Duck\n" + New_Rubber.flyBehavior.getDetails() + "\n" + New_Rubber.quackBehavior.getDetails()
        dummy_duck = Button(text=details, size_hint=(.2, 1))
        self.Duck_Buttons.append(dummy_duck)
        self.layout_RubberDuck.add_widget(dummy_duck)

    def btnCbk_addDecoyDuck(self, instance):
        New_Decoy = DecoyDuckClass()
        self.AllDucks.append(New_Decoy)
        details = "Decoy Duck\n" + New_Decoy.flyBehavior.getDetails() + "\n" + New_Decoy.quackBehavior.getDetails()
        dummy_duck = Button(text=details, size_hint=(.2, 1))
        self.Duck_Buttons.append(dummy_duck)
        self.layout_DecoyDuck.add_widget(dummy_duck)

    def btnCbk_totalducks(self, instance):
        print 'Total Ducks are ' + str(len(self.AllDucks))
        for idx,x in enumerate(self.AllDucks):
            print str(idx) + '.',
            x.display()

    def btnCbk_setFlyBehavior(self, instance):
        self.btnCbk_totalducks(instance)
        if(len(self.AllDucks) > 0):
            duck_index=input("Select Duck Index\n")
            if(duck_index < len(self.AllDucks)):
                Duck_fly_behvaior = input("Select Fly Behavior\n1. Fly with Wings\n2. Cant Fly\n")
                if(Duck_fly_behvaior == 1):
                    Fly = FlyWithWings()
                    self.AllDucks[int(duck_index)].setFlyBehavior(Fly)
                elif(Duck_fly_behvaior == 2):
                    NoFly = FlyNoWay()
                    self.AllDucks[int(duck_index)].setFlyBehavior(NoFly)
                else:
                    print("Wrong Behavior Selected\n")
            else:
                print("Wrong Index\n")

    def btnCbk_setQuackBehavior(self, instance):
        self.btnCbk_totalducks(instance)
        if(len(self.AllDucks) > 0):
            duck_index=input("Select Duck Index  ")
            if(duck_index < len(self.AllDucks)):
                Duck_quack_behvaior = input("Select Quack Behavior\n1. Quack\n2. Squeak\n3. MuteQuack\n")
                if (Duck_quack_behvaior == 1):
                    In_Quack = Quack()
                    self.AllDucks[int(duck_index)].setQuackBehavior(In_Quack)
                elif(Duck_quack_behvaior == 2):
                    In_Squeak = Squeak()
                    self.AllDucks[int(duck_index)].setQuackBehavior(In_Squeak)
                elif(Duck_quack_behvaior ==  3):
                    In_Mute = MuteQuack()
                    self.AllDucks[int(duck_index)].setQuackBehavior(In_Mute)
                else:
                    print("Wrong Behavior Selected\n")
            else:
                print "Worng Index\n"

    def btnCbk_performDuck(self, instance):
        self.btnCbk_totalducks(instance)
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
        for idx,x in enumerate(self.Duck_Buttons):
            pre_details=x.text
            splitted_details = pre_details.split('\n')
            splitted_details[1]=self.AllDucks[idx].flyBehavior.getDetails()
            splitted_details[2]=self.AllDucks[idx].quackBehavior.getDetails()
            details = '\n'.join(splitted_details)
            x.text = details

    def build(self):
        self.title = 'SimUDuck'

        Clock.schedule_interval(self.UpdateLabel, 0.2)

        btn_addMallardDuck = Button(text='Add a new Mallard Duck', on_press=self.btnCbk_addMallardDuck,size_hint=(0.5, 0.2), halign="left", valign="middle")
        btn_addReadheadDuck = Button(text='Add a new Readhead Duck', on_press=self.btnCbk_addReadheadDuck,size_hint=(0.5, 0.2), halign="left", valign="middle")
        btn_addRubberDuck = Button(text='Add a new Rubber Duck', on_press=self.btnCbk_addRubberDuck,size_hint=(0.5, 0.2), halign="left", valign="middle")
        btn_addDecoyDuck = Button(text='Add a new Decoy Duck', on_press=self.btnCbk_addDecoyDuck,size_hint=(0.5, 0.2), halign="left", valign="middle")
        btn_totalducks = Button(text='Total Ducks', on_press=self.btnCbk_totalducks,size_hint=(0.5, 0.2), halign="left", valign="middle")
        btn_setFlyBehavior = Button(text='Set Fly Behavior', on_press=self.btnCbk_setFlyBehavior,size_hint=(0.5, 0.2), halign="left", valign="middle")
        btn_setQuackBehavior = Button(text='Set Quack Behavior', on_press=self.btnCbk_setQuackBehavior,size_hint=(0.5, 0.2), halign="left", valign="middle")
        btn_PerformDuck = Button(text='Perform Duck', on_press=self.btnCbk_performDuck,size_hint=(0.5, 0.2), halign="left", valign="middle")


        layout = BoxLayout()
        layout.add_widget(btn_addMallardDuck)
        layout.add_widget(btn_addReadheadDuck)
        layout.add_widget(btn_addRubberDuck)
        layout.add_widget(btn_addDecoyDuck)
        layout.add_widget(btn_totalducks)
        layout.add_widget(btn_setFlyBehavior)
        layout.add_widget(btn_setQuackBehavior)
        layout.add_widget(btn_PerformDuck)
        layout.add_widget(self.TD_label)

        MD_label = Label(text="Mallard Ducks ", size_hint=(0.5, 0.2), halign="left", valign="top")
        self.layout_Mallard.add_widget(MD_label)

        RD_label = Label(text="Red Head Ducks ", size_hint=(0.5, 0.2), halign="left", valign="top")
        self.layout_RedHead.add_widget(RD_label)

        RbD_label = Label(text="Rubber Ducks ", size_hint=(0.5, 0.2), halign="left", valign="top")
        self.layout_RubberDuck.add_widget(RbD_label)

        Decoy_label = Label(text="Decoy Ducks ", size_hint=(0.5, 0.2), halign="left", valign="top")
        self.layout_DecoyDuck.add_widget(Decoy_label)

        root = BoxLayout(orientation='vertical')
        root.add_widget(layout)
        root.add_widget(self.layout_Mallard)
        root.add_widget(self.layout_RedHead)
        root.add_widget(self.layout_RubberDuck)
        root.add_widget(self.layout_DecoyDuck)

        return root

if __name__ == '__main__':
    MyApp().run()