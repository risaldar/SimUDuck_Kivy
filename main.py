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
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

import abc

import CollectionsManager
from Ducks.DuckTypes.Duck import DuckClass
from Ducks.DuckFlyBehaviors.FlyBehavior import FlyBehavior
from Ducks.DuckQuackBehaviors.QuackBehavior import QuackBehavior


# ====================================== Main ==============================#
class MyApp(App):

    AllDuckCreateButtons = {}
    AllDuckTypeLayout = None
    AllDuckButtonInstanceDictionary = {}
    OneSelectedButton = None
    label_totalDucks = None

    def btnCbk_addNewCoop(self, instance):
        CoopTypeName = instance.text
        OneNewCoop = CollectionsManager.createNewCoop(CoopTypeName)
        details = CoopTypeName + "\n" + str(OneNewCoop.getColumns()) + 'x' + str(OneNewCoop.getRows())
        btn_OneNewCoop = Button(text=details, on_press=self.btnCbk_selectOneDuckComponent, background_color=(1.0, 0.0, 0.0, 1.0), size_hint=(1, 0.2))
        gridlayout_OneNewCoop = GridLayout(cols = OneNewCoop.getColumns(), rows = OneNewCoop.getRows())
        boxlayout_OneNewCoop = BoxLayout(orientation='vertical', size_hint=(1, 1), pos_hint={'top': 1})
        boxlayout_OneNewCoop.add_widget(btn_OneNewCoop)
        boxlayout_OneNewCoop.add_widget(gridlayout_OneNewCoop)
        self.AllDuckButtonInstanceDictionary[btn_OneNewCoop] = OneNewCoop

        # Actual benefit of Composite Pattern can be seen here, Irrespective of duck or coop we can call addDuckComponent
        if self.OneSelectedButton is None or self.AllDuckButtonInstanceDictionary[self.OneSelectedButton].addDuckComponent(OneNewCoop) == False:
            self.AllDuckTypeLayout.add_widget(boxlayout_OneNewCoop)
        else:
            for child in self.OneSelectedButton.parent.children:
                # Each Coop layout has exactly 2 children. One is Coop button which is now pressed and other is grid where we need to add new coop
                if child != self.OneSelectedButton:
                    child.add_widget(boxlayout_OneNewCoop)
                    break
        Clock.schedule_once(self.UpdateLabel, 0.1)

    def btnCbk_addNewDuck(self, instance):
        DuckTypeName = instance.text
        OneNewDuck = CollectionsManager.createNewDuck(DuckTypeName)
        details = DuckTypeName + "\n" + OneNewDuck.flyBehavior.getDetails() + "\n" + OneNewDuck.quackBehavior.getDetails()
        btn_OneNewDuck = Button(text=details, on_press=self.btnCbk_selectOneDuckComponent, size_hint=(1, 1))
        self.AllDuckButtonInstanceDictionary[btn_OneNewDuck] = OneNewDuck
        # Actual benefit of Composite Pattern can be seen here, Irrespective of duck or coop we can call addDuckComponent
        if self.OneSelectedButton is None or self.AllDuckButtonInstanceDictionary[self.OneSelectedButton].addDuckComponent(OneNewDuck) == False:
            self.AllDuckTypeLayout.add_widget(btn_OneNewDuck)
        else:
            for child in self.OneSelectedButton.parent.children:
                # Each Coop layout has exactly 2 children. One is Coop button which is now pressed and other is grid where we need to add new duck
                if child != self.OneSelectedButton:
                    child.add_widget(btn_OneNewDuck)
                    break
        Clock.schedule_once(self.UpdateLabel, 0.1)

    def btnCbk_selectOneDuckComponent(self, instance):
        self.OneSelectedButton = instance

    def btnCbk_setFlyBehavior(self, instance):
        if self.OneSelectedButton is not None:
            OneFlyBehavior = CollectionsManager.createNewDuckFlyBehavior(instance.text)
            # Actual benefit of Composite Pattern can be seen here, Irrespective of duck or coop we can call setFlyBehavior
            self.AllDuckButtonInstanceDictionary[self.OneSelectedButton].setFlyBehavior(OneFlyBehavior)
            Clock.schedule_once(self.UpdateLabel, 0.1)

    def btnCbk_setQuackBehavior(self, instance):
        if self.OneSelectedButton is not None:
            OneQuackBehavior = CollectionsManager.createNewDuckQuackBehavior(instance.text)
            # Actual benefit of Composite Pattern can be seen here, Irrespective of duck or coop we can call setQuackBehavior
            self.AllDuckButtonInstanceDictionary[self.OneSelectedButton].setQuackBehavior(OneQuackBehavior)
            Clock.schedule_once(self.UpdateLabel, 0.1)

    def btnCbk_performDuck(self, instance):
        if self.OneSelectedButton is not None:
            pre_details=self.OneSelectedButton.text
            splitted_details = pre_details.split('\n')
            # Actual benefit of Composite Pattern can be seen here, Irrespective of duck or coop we can call performFly and performQuack
            splitted_details[1]=self.AllDuckButtonInstanceDictionary[self.OneSelectedButton].performFly()
            splitted_details[2]=self.AllDuckButtonInstanceDictionary[self.OneSelectedButton].performQuack()
            details = '\n'.join(splitted_details)
            self.OneSelectedButton.text = details
            Clock.schedule_once(self.UpdateLabel, 2) # 2sec action

    def btnCbk_removeDuck(self, instance):
        if self.OneSelectedButton is not None:
            layout = self.AllDuckTypeLayout
            layout.remove_widget(self.OneSelectedButton)
            del self.AllDuckButtonInstanceDictionary[self.OneSelectedButton]
            del self.AllDuckButtonInstanceDictionary[self.OneSelectedButton]
            
    def UpdateLabel(self, label):
        DuckCount = 0
        for button, component in self.AllDuckButtonInstanceDictionary.items():
            if 'Duck' in component.__class__.__name__:
                pre_details=button.text
                splitted_details = pre_details.split('\n')
                DuckCount += 1
                splitted_details[1]=component.flyBehavior.getDetails()
                splitted_details[2]=component.quackBehavior.getDetails()
                details = '\n'.join(splitted_details)
                button.text = details
        self.label_totalDucks.text="Total Ducks = " + str(DuckCount)

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
        
        btn_performDuck = Button(text='Perform Duck', on_press=self.btnCbk_performDuck,size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})
        
        btn_removeDuck = Button(text='Remove a Duck', on_press=self.btnCbk_removeDuck,size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})

        self.label_totalDucks = Label(text="Total Ducks = 0", size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})

        control_layout = BoxLayout(size_hint=(1, None), pos_hint={'top': 1})

        control_layout.add_widget(btn_addNewDuck)
        control_layout.add_widget(btn_addNewCoop)
        control_layout.add_widget(btn_setFlyBehavior)
        control_layout.add_widget(btn_setQuackBehavior)
        control_layout.add_widget(btn_performDuck)
        control_layout.add_widget(btn_removeDuck)
        control_layout.add_widget(self.label_totalDucks)

        self.AllDuckTypeLayout = BoxLayout(size_hint=(1, 1), pos_hint={'bottom': 1})

        root = BoxLayout(orientation='vertical', size_hint=(1, 1), pos_hint={'top': 1})
        root.add_widget(control_layout)
        root.add_widget(self.AllDuckTypeLayout)

        return root

if __name__ == '__main__':
    MyApp().run()