import kivy

from time import time
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

import abc

import CollectionsManager
from Ducks.DuckTypes.Duck import DuckClass
from Ducks.DuckFlyBehaviors.FlyBehavior import FlyBehavior
from Ducks.DuckQuackBehaviors.QuackBehavior import QuackBehavior


# ====================================== Main ==============================#
class MyApp(App):

    AllDuckInstanceObjects = []
    AllDuckCreateButtons = {}
    AllDuckInstanceButtons = []
    OneSelectedDuckInstanceButton = None

    TD_label = Label(text="Total Ducks = " + str(len(AllDuckInstanceObjects)), size_hint=(0.5, 0.2), halign="left", valign="middle")
    layout_AllDucks = BoxLayout()
    #layout_Mallard = BoxLayout()
    #layout_RedHead = BoxLayout()
    #layout_RubberDuck = BoxLayout()
    #layout_DecoyDuck = BoxLayout()

    def btnCbk_addNewDuck(self, instance):
        DuckTypeName = instance.text[len('Add a new '):]
        OneNewDuck = CollectionsManager.createNewDuck(DuckTypeName)
        self.AllDuckInstanceObjects.append(OneNewDuck)
        details = DuckTypeName + "\n" + OneNewDuck.flyBehavior.getDetails() + "\n" + OneNewDuck.quackBehavior.getDetails()
        btn_OneNewDuck = Button(text=details, on_press=self.btnCbk_selectOneDuck, size_hint=(.2, 1))
        self.AllDuckInstanceButtons.append(btn_OneNewDuck)
        self.layout_AllDucks.add_widget(btn_OneNewDuck)

    def btnCbk_selectOneDuck(self, instance):
        self.OneSelectedDuckInstanceButton = instance

    def btnCbk_totalducks(self, instance):
        print 'Total Ducks are ' + str(len(self.AllDuckInstanceObjects))
        for idx,x in enumerate(self.AllDuckInstanceObjects):
            print str(idx) + '.',
            x.display()

    def btnCbk_setFlyBehavior(self, instance):
        if self.OneSelectedDuckInstanceButton is not None:
            OneSelectedDuckInstanceIndex = self.AllDuckInstanceButtons.index(self.OneSelectedDuckInstanceButton)
            OneFlyBehavior = CollectionsManager.createNewDuckFlyBehavior(instance.text)
            self.AllDuckInstanceObjects[OneSelectedDuckInstanceIndex].setFlyBehavior(OneFlyBehavior)

    def btnCbk_setQuackBehavior(self, instance):
        if self.OneSelectedDuckInstanceButton is not None:
            OneSelectedDuckInstanceIndex = self.AllDuckInstanceButtons.index(self.OneSelectedDuckInstanceButton)
            OneQuackBehavior = CollectionsManager.createNewDuckQuackBehavior(instance.text)
            self.AllDuckInstanceObjects[OneSelectedDuckInstanceIndex].setQuackBehavior(OneQuackBehavior)

    def btnCbk_performDuck(self, instance):
        if self.OneSelectedDuckInstanceButton is not None:
            OneSelectedDuckInstanceIndex = self.AllDuckInstanceButtons.index(self.OneSelectedDuckInstanceButton)
            self.AllDuckInstanceObjects[OneSelectedDuckInstanceIndex].performFly()
            self.AllDuckInstanceObjects[OneSelectedDuckInstanceIndex].performQuack()

    def UpdateLabel(self, label):
        self.TD_label.text="Total Ducks = " + str(len(self.AllDuckInstanceObjects))
        for idx, instance in enumerate(self.AllDuckInstanceButtons):
            pre_details=instance.text
            splitted_details = pre_details.split('\n')
            splitted_details[1]=self.AllDuckInstanceObjects[idx].flyBehavior.getDetails()
            splitted_details[2]=self.AllDuckInstanceObjects[idx].quackBehavior.getDetails()
            details = '\n'.join(splitted_details)
            instance.text = details

    def build(self):
        self.title = 'SimUDuck'

        Clock.schedule_interval(self.UpdateLabel, 0.2)

        CollectionsManager.loadCollections()

        for OneDuckTypeName in CollectionsManager.getAllDuckTypes():
            self.AllDuckCreateButtons[OneDuckTypeName] = Button(text='Add a new ' + OneDuckTypeName, on_press=self.btnCbk_addNewDuck, size_hint=(0.5, 0.2), halign="left", valign="middle")

        btn_totalducks = Button(text='Total Ducks', on_press=self.btnCbk_totalducks, size_hint=(0.5, 0.2), halign="left", valign="middle")

        dropdown_setFlyBehavior = DropDown()
        for OneDuckFlyBehaviorName in CollectionsManager.getAllDuckFlyBehaviors():
            btn = Button(text=OneDuckFlyBehaviorName, on_press=self.btnCbk_setFlyBehavior, size_hint_y=None)
            dropdown_setFlyBehavior.add_widget(btn)
        btn_setFlyBehavior = Button(text='Set Fly Behavior', on_release=dropdown_setFlyBehavior.open, size_hint=(0.5, 0.2), halign="left", valign="middle")
    
        dropdown_setQuackBehavior = DropDown()
        for OneDuckQuackBehaviorName in CollectionsManager.getAllDuckQuackBehaviors():
            btn = Button(text=OneDuckQuackBehaviorName, on_press=self.btnCbk_setQuackBehavior, size_hint_y=None)
            dropdown_setQuackBehavior.add_widget(btn)
        btn_setQuackBehavior = Button(text='Set Quack Behavior', on_release=dropdown_setQuackBehavior.open,size_hint=(0.5, 0.2), halign="left", valign="middle")
        
        btn_PerformDuck = Button(text='Perform Duck', on_press=self.btnCbk_performDuck,size_hint=(0.5, 0.2), halign="left", valign="middle")

        layout = BoxLayout()
        for OneButtionKey, OneButtonInstance in self.AllDuckCreateButtons.items():
            layout.add_widget(OneButtonInstance)

        layout.add_widget(btn_totalducks)
        layout.add_widget(btn_setFlyBehavior)
        layout.add_widget(btn_setQuackBehavior)
        layout.add_widget(btn_PerformDuck)
        layout.add_widget(self.TD_label)

        AllDuckInstances_label = Label(text="All Ducks Instances", size_hint=(0.5, 0.2), halign="left", valign="top")
        self.layout_AllDucks.add_widget(AllDuckInstances_label)

        #MD_label = Label(text="Mallard Ducks ", size_hint=(0.5, 0.2), halign="left", valign="top")
        #self.layout_Mallard.add_widget(MD_label)
#
        #RD_label = Label(text="Red Head Ducks ", size_hint=(0.5, 0.2), halign="left", valign="top")
        #self.layout_RedHead.add_widget(RD_label)
#
        #RbD_label = Label(text="Rubber Ducks ", size_hint=(0.5, 0.2), halign="left", valign="top")
        #self.layout_RubberDuck.add_widget(RbD_label)
#
        #Decoy_label = Label(text="Decoy Ducks ", size_hint=(0.5, 0.2), halign="left", valign="top")
        #self.layout_DecoyDuck.add_widget(Decoy_label)

        root = BoxLayout(orientation='vertical')
        root.add_widget(layout)
        root.add_widget(self.layout_AllDucks)
        #root.add_widget(self.layout_Mallard)
        #root.add_widget(self.layout_RedHead)
        #root.add_widget(self.layout_RubberDuck)
        #root.add_widget(self.layout_DecoyDuck)

        return root

if __name__ == '__main__':
    MyApp().run()