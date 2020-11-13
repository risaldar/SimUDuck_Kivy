import kivy

from time import time
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color
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
    #AllDuckTypeLayouts = {}
    AllDuckTypeLayout = None
    AllDuckInstanceButtons = []
    OneSelectedDuckInstanceButton = None
    OneSelectedCoopInstanceButton = None
    TD_label = None

    def btnCbk_addNewCoop(self, instance):
        CoopTypeName = instance.text
        OneNewCoop = CollectionsManager.createNewCoop(CoopTypeName)
        self.AllDuckInstanceObjects.append(OneNewCoop)
        details = CoopTypeName + "\n"
        btn_OneNewCoop = Button(text=details, on_press=self.btnCbk_selectOneCoop, background_color=(1.0, 0.0, 0.0, 1.0), size_hint=(1, 1))
        self.AllDuckInstanceButtons.append(btn_OneNewCoop)
        self.AllDuckTypeLayout.add_widget(btn_OneNewCoop)
        #Clock.schedule_once(self.UpdateLabel, 0.1)

    def btnCbk_addNewDuck(self, instance):
        DuckTypeName = instance.text
        OneNewDuck = CollectionsManager.createNewDuck(DuckTypeName)
        self.AllDuckInstanceObjects.append(OneNewDuck)
        details = DuckTypeName + "\n" + OneNewDuck.flyBehavior.getDetails() + "\n" + OneNewDuck.quackBehavior.getDetails()
        btn_OneNewDuck = Button(text=details, on_press=self.btnCbk_selectOneDuck, size_hint=(1, 1))
        if self.OneSelectedCoopInstanceButton is None:
            self.AllDuckInstanceButtons.append(btn_OneNewDuck)
            #self.AllDuckTypeLayouts[DuckTypeName].add_widget(btn_OneNewDuck)
            self.AllDuckTypeLayout.add_widget(btn_OneNewDuck)
        else:
            print 'TODO'
            #self.OneSelectedCoopInstanceButton.add_widget(btn_OneNewDuck)
        Clock.schedule_once(self.UpdateLabel, 0.1)

    def btnCbk_selectOneCoop(self, instance):
        self.OneSelectedDuckInstanceButton = None
        self.OneSelectedCoopInstanceButton = instance

    def btnCbk_selectOneDuck(self, instance):
        self.OneSelectedCoopInstanceButton = None
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
            Clock.schedule_once(self.UpdateLabel, 0.1)

    def btnCbk_setQuackBehavior(self, instance):
        if self.OneSelectedDuckInstanceButton is not None:
            OneSelectedDuckInstanceIndex = self.AllDuckInstanceButtons.index(self.OneSelectedDuckInstanceButton)
            OneQuackBehavior = CollectionsManager.createNewDuckQuackBehavior(instance.text)
            self.AllDuckInstanceObjects[OneSelectedDuckInstanceIndex].setQuackBehavior(OneQuackBehavior)
            Clock.schedule_once(self.UpdateLabel, 0.1)

    def btnCbk_performDuck(self, instance):
        if self.OneSelectedDuckInstanceButton is not None:
            OneSelectedDuckInstanceIndex = self.AllDuckInstanceButtons.index(self.OneSelectedDuckInstanceButton)
            pre_details=self.OneSelectedDuckInstanceButton.text
            splitted_details = pre_details.split('\n')
            splitted_details[1]=self.AllDuckInstanceObjects[OneSelectedDuckInstanceIndex].performFly()
            splitted_details[2]=self.AllDuckInstanceObjects[OneSelectedDuckInstanceIndex].performQuack()
            details = '\n'.join(splitted_details)
            self.OneSelectedDuckInstanceButton.text = details
            Clock.schedule_once(self.UpdateLabel, 2) # 2sec action

    def btnCbk_removeDuck(self, instance):
        if self.OneSelectedDuckInstanceButton is not None:
            OneSelectedDuckInstanceIndex = self.AllDuckInstanceButtons.index(self.OneSelectedDuckInstanceButton)
            #layout = self.AllDuckTypeLayouts[self.AllDuckInstanceObjects[OneSelectedDuckInstanceIndex].__class__.__name__[:-len('Class')]]
            layout = self.AllDuckTypeLayout
            layout.remove_widget(self.OneSelectedDuckInstanceButton)
            del self.AllDuckInstanceButtons[OneSelectedDuckInstanceIndex]
            del self.AllDuckInstanceObjects[OneSelectedDuckInstanceIndex]
            
    def UpdateLabel(self, label):
        DuckCount = 0
        for idx, instance in enumerate(self.AllDuckInstanceButtons):
            pre_details=instance.text
            splitted_details = pre_details.split('\n')
            if 'Duck' in splitted_details[0]:
                DuckCount += 1
                splitted_details[1]=self.AllDuckInstanceObjects[idx].flyBehavior.getDetails()
                splitted_details[2]=self.AllDuckInstanceObjects[idx].quackBehavior.getDetails()
            details = '\n'.join(splitted_details)
            instance.text = details
        self.TD_label.text="Total Ducks = " + str(DuckCount)

    def build(self):
        self.title = 'SimUDuck'

        CollectionsManager.loadCollections()

        dropdown_addNewDuck = DropDown()
        for OneDuckTypeName in CollectionsManager.getAllDuckTypes():
            btn = Button(text=OneDuckTypeName, on_press=self.btnCbk_addNewDuck, size_hint_y=None)
            dropdown_addNewDuck.add_widget(btn)
        btn_addNewDuck = Button(text='Add a new Duck', on_release=dropdown_addNewDuck.open, size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})

        dropdown_addNewCoop = DropDown()
        for OneCoopTypeName in CollectionsManager.getAllCoopTypes():
            btn = Button(text=OneCoopTypeName, on_press=self.btnCbk_addNewCoop, size_hint_y=None)
            dropdown_addNewCoop.add_widget(btn)
        btn_addNewCoop = Button(text='Add a new Coop', on_release=dropdown_addNewCoop.open, size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})
    
        dropdown_setFlyBehavior = DropDown()
        for OneDuckFlyBehaviorName in CollectionsManager.getAllDuckFlyBehaviors():
            btn = Button(text=OneDuckFlyBehaviorName, on_press=self.btnCbk_setFlyBehavior, size_hint_y=None)
            dropdown_setFlyBehavior.add_widget(btn)
        btn_setFlyBehavior = Button(text='Set Fly Behavior', on_release=dropdown_setFlyBehavior.open, size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})
    
        dropdown_setQuackBehavior = DropDown()
        for OneDuckQuackBehaviorName in CollectionsManager.getAllDuckQuackBehaviors():
            btn = Button(text=OneDuckQuackBehaviorName, on_press=self.btnCbk_setQuackBehavior, size_hint_y=None)
            dropdown_setQuackBehavior.add_widget(btn)
        btn_setQuackBehavior = Button(text='Set Quack Behavior', on_release=dropdown_setQuackBehavior.open,size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})
        
        btn_PerformDuck = Button(text='Perform Duck', on_press=self.btnCbk_performDuck,size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})
        
        btn_removeDuck = Button(text='Remove a Duck', on_press=self.btnCbk_removeDuck,size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})

        self.TD_label = Label(text="Total Ducks = " + str(len(self.AllDuckInstanceObjects)), size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})

        control_layout = BoxLayout(size_hint=(1, None), pos_hint={'top': 1})

        control_layout.add_widget(btn_addNewDuck)
        control_layout.add_widget(btn_addNewCoop)
        control_layout.add_widget(btn_setFlyBehavior)
        control_layout.add_widget(btn_setQuackBehavior)
        control_layout.add_widget(btn_PerformDuck)
        control_layout.add_widget(btn_removeDuck)
        control_layout.add_widget(self.TD_label)

        self.AllDuckTypeLayout = BoxLayout(size_hint=(1, 1), pos_hint={'bottom': 1})

        root = BoxLayout(orientation='vertical', size_hint=(1, 1), pos_hint={'top': 1})
        root.add_widget(control_layout)
        root.add_widget(self.AllDuckTypeLayout)

        return root

if __name__ == '__main__':
    MyApp().run()