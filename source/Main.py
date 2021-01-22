import kivy

from time import time
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color
from kivy.graphics.texture import Texture
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

import abc

import CollectionsManager
from Ducks.DuckTypes.Duck import DuckClass
from Ducks.CoopTypes.Coop import CoopClass
from DuckComponentDecorator import DuckComponentDecoratorClass
from Ducks.DuckFlyBehaviors.FlyBehavior import FlyBehavior
from Ducks.DuckQuackBehaviors.QuackBehavior import QuackBehavior


# ====================================== Main ==============================#
class MyApp(App):

    AllControlWidgets = []
    AllDuckCreateButtons = {}
    AllDuckTypeLayout = None
    AllDuckTypeLayout_ChildDuckComponents = []
    AllDuckButtonInstanceDictionary = {}
    OneSelectedButton = None
    OneSelectedDuckComponent = None
    label_totalDucks = None

    root = None

    def _print_widgets(self, parent):
        print parent
        for child in parent.children:
            self._print_widgets(child)

    def btnCbk_new(self, instance):
        CollectionsManager.createNewDatabase()
        for component in self.AllDuckTypeLayout_ChildDuckComponents:
            del component
        self.AllDuckTypeLayout_ChildDuckComponents = []
        self.OneSelectedDuckComponent = None
        self.redrawAllDuckComponents(None)

    def btnCbk_save(self, instance):
        CollectionsManager.saveDatabase(self.AllDuckTypeLayout_ChildDuckComponents)
        self.OneSelectedDuckComponent = None

    def btnCbk_escape(self, instance):
        self.OneSelectedDuckComponent = None

    def btnCbk_addNewCoop(self, instance):
        OneNewCoop = CollectionsManager.createNewCoop(instance.text)
        # Actual benefit of Composite Pattern can be seen here, Irrespective of duck or coop we can call addDuckComponent
        if self.OneSelectedDuckComponent is None or self.OneSelectedDuckComponent.addDuckComponent(OneNewCoop) == False:
            self.AllDuckTypeLayout_ChildDuckComponents.append(OneNewCoop)
        self.redrawAllDuckComponents(None)

    def btnCbk_addNewDuck(self, instance):
        OneNewDuck = CollectionsManager.createNewDuck(instance.text)
        # Actual benefit of Composite Pattern can be seen here, Irrespective of duck or coop we can call addDuckComponent
        if self.OneSelectedDuckComponent is None or self.OneSelectedDuckComponent.addDuckComponent(OneNewDuck) == False:
            self.AllDuckTypeLayout_ChildDuckComponents.append(OneNewDuck)
        self.redrawAllDuckComponents(None)

    def btnCbk_selectOneDuckComponent(self, instance):
        self.OneSelectedDuckComponent = self.AllDuckButtonInstanceDictionary[instance]

    def btnCbk_setFlyBehavior(self, instance):
        if self.OneSelectedDuckComponent is not None:
            OneFlyBehavior = CollectionsManager.createNewDuckFlyBehavior(instance.text)
            # Actual benefit of Composite Pattern can be seen here, Irrespective of duck or coop we can call setFlyBehavior
            self.OneSelectedDuckComponent.setFlyBehavior(OneFlyBehavior)
            self.redrawAllDuckComponents(None)

    def btnCbk_setQuackBehavior(self, instance):
        if self.OneSelectedDuckComponent is not None:
            OneQuackBehavior = CollectionsManager.createNewDuckQuackBehavior(instance.text)
            # Actual benefit of Composite Pattern can be seen here, Irrespective of duck or coop we can call setQuackBehavior
            self.OneSelectedDuckComponent.setQuackBehavior(OneQuackBehavior)
            self.redrawAllDuckComponents(None)

    def performDuck(self, component):
        component_widget = [key for key, value in self.AllDuckButtonInstanceDictionary.iteritems() if value == component][0]
        pre_details = component_widget.text
        splitted_details = pre_details.split('\n')
        # Actual benefit of Composite Pattern can be seen here, Irrespective of duck or coop we can call performFly and performQuack
        splitted_details[1] = component.performFly()
        splitted_details[2] = component.performQuack()
        details = '\n'.join(splitted_details)
        component_widget.text = details

    def btnCbk_performDuck(self, instance):
        if self.OneSelectedDuckComponent is not None:
            if isinstance(self.OneSelectedDuckComponent, CoopClass):
                iterator = self.OneSelectedDuckComponent.createIterator()
                while True:
                    child_component = iterator.next()
                    if child_component is not None:
                        self.performDuck(child_component)
                    else:
                        break
            else:
                self.performDuck(self.OneSelectedDuckComponent)
            Clock.schedule_once(self.redrawAllDuckComponents, 2) # 2sec action

    # redraw is needed since everything inside canvas needs to be readjusted if size or position of containing layout changes
    def _redraw(self, obj, value):
        for child in obj.canvas.children:
            if type(child) is Rectangle:
                child.pos = obj.pos
                child.size = obj.size

    def addCompositeDecoration(self, component, color):
        for child_component in component.ChildDuckComponents:
            if isinstance(child_component, CoopClass):
                self.addCompositeDecoration(child_component, color)
            else:
                OneNewDuckComponentDecorator = CollectionsManager.createNewDuckComponentDecorator(color, child_component)
                component.updateDuckComponent(child_component, OneNewDuckComponentDecorator)

    def addDecoration(self, component, color):
        for child_component in component.ChildDuckComponents:
            if child_component == self.OneSelectedDuckComponent:
                if isinstance(child_component, CoopClass):
                    self.addCompositeDecoration(child_component, color)
                else:
                    OneNewDuckComponentDecorator = CollectionsManager.createNewDuckComponentDecorator(color, child_component)
                    component.updateDuckComponent(child_component, OneNewDuckComponentDecorator)
                    self.OneSelectedDuckComponent = OneNewDuckComponentDecorator
                return True
            elif isinstance(child_component, CoopClass):
                if self.addDecoration(child_component, color) is True:
                    return True
            else:
                pass
        return False

    def btnCbk_addDecoration(self, instance):
        if self.OneSelectedDuckComponent is not None:
            for component in self.AllDuckTypeLayout_ChildDuckComponents:
                if component == self.OneSelectedDuckComponent:
                    if isinstance(component, CoopClass):
                        self.addCompositeDecoration(component, instance.text)
                    else:
                        component_index = self.AllDuckTypeLayout_ChildDuckComponents.index(component)
                        self.AllDuckTypeLayout_ChildDuckComponents.remove(component)
                        OneNewDuckComponentDecorator = CollectionsManager.createNewDuckComponentDecorator(instance.text, component)
                        self.AllDuckTypeLayout_ChildDuckComponents.insert(component_index, OneNewDuckComponentDecorator)
                        self.OneSelectedDuckComponent = OneNewDuckComponentDecorator
                elif isinstance(component, CoopClass):
                    if self.addDecoration(component, instance.text) is True:
                        break
                else:
                    pass
            self.redrawAllDuckComponents(None)

    def removeDuckComponent(self, component):
        for child_component in component.ChildDuckComponents:
            if child_component == self.OneSelectedDuckComponent:
                component.removeDuckComponent(child_component)
                return True
            elif isinstance(child_component, CoopClass):
                if self.removeDuckComponent(child_component) is True:
                    return True
            else:
                pass
        return False

    def btnCbk_removeDuckComponent(self, instance):
        if self.OneSelectedDuckComponent is not None:
            for component in self.AllDuckTypeLayout_ChildDuckComponents:
                if component == self.OneSelectedDuckComponent:
                    self.AllDuckTypeLayout_ChildDuckComponents.remove(component)
                elif isinstance(component, CoopClass):
                    if self.removeDuckComponent(component) is True:
                        break
                else:
                    pass
            self.OneSelectedDuckComponent = None
            self.redrawAllDuckComponents(None)

    def UpdateLabel(self, label):
        DuckCount = 0
        for component in self.AllDuckTypeLayout_ChildDuckComponents:
            if isinstance(component, CoopClass):
                iterator = component.createIterator()
                while True:
                    child_component = iterator.next()
                    if child_component is not None:
                        DuckCount += 1
                    else:
                        break
            else:
                DuckCount += 1
        self.label_totalDucks.text="Total Ducks = " + str(DuckCount)

    def redrawDuckWidget(self, component, parent_widget):
        btn_OneNewDuck = Button(id='Duck', on_press=self.btnCbk_selectOneDuckComponent, size_hint=(1, 1))
        self.AllDuckButtonInstanceDictionary[btn_OneNewDuck] = component
        component_widget = btn_OneNewDuck
        while isinstance(component, DuckComponentDecoratorClass) is True:
            # Add a container layout to selected button as per decorated color
            wrapped_widget = component_widget
            boxlayout_OneDuckComponentDecorator = BoxLayout(id='Decorator', padding=[10, 10, 10, 10], orientation='vertical', size_hint=(1, 1), pos_hint={'top': 1})
            decoration_color = component.getDuckComponentDecoration()[0]
            boxlayout_OneDuckComponentDecorator.canvas.add(Color(rgba=decoration_color))
            boxlayout_OneDuckComponentDecorator.canvas.add(Rectangle(pos=wrapped_widget.pos, size=wrapped_widget.size))
            boxlayout_OneDuckComponentDecorator.add_widget(wrapped_widget)
            boxlayout_OneDuckComponentDecorator.bind(pos=self._redraw, size=self._redraw)
            component_widget = boxlayout_OneDuckComponentDecorator
            component = component.WrappedDuckComponent
        details = component.__class__.__name__.replace('Class', '') + "\n" + component.flyBehavior.getDetails() + "\n" + component.quackBehavior.getDetails()
        btn_OneNewDuck.text = details
        parent_widget.add_widget(component_widget)

    def redrawCoopWidget(self, component, parent_widget):
        details = component.__class__.__name__.replace('Class', '') + "\n" + str(component.getColumns()) + 'x' + str(component.getRows())
        btn_OneNewCoop = Button(text=details, on_press=self.btnCbk_selectOneDuckComponent, background_color=(1.0, 0.0, 0.0, 1.0), size_hint=(1, 0.2))
        gridlayout_OneNewCoop = GridLayout(cols = component.getColumns(), rows = component.getRows())
        boxlayout_OneNewCoop = BoxLayout(id='Coop', orientation='vertical', size_hint=(1, 1), pos_hint={'top': 1})
        boxlayout_OneNewCoop.add_widget(btn_OneNewCoop)
        boxlayout_OneNewCoop.add_widget(gridlayout_OneNewCoop)
        self.AllDuckButtonInstanceDictionary[btn_OneNewCoop] = component
        parent_widget.add_widget(boxlayout_OneNewCoop)
        return gridlayout_OneNewCoop

    def redrawDuckComponents(self, component, parent_widget):
        if isinstance(component, CoopClass):
            component_widget = self.redrawCoopWidget(component, parent_widget)
            for child_component in component.ChildDuckComponents:
                self.redrawDuckComponents(child_component, component_widget)
        else:
            self.redrawDuckWidget(component, parent_widget)

    def redrawAllDuckComponents(self, instance):
        self.AllDuckTypeLayout.clear_widgets()
        self.AllDuckButtonInstanceDictionary = {}
        for component in self.AllDuckTypeLayout_ChildDuckComponents:
            self.redrawDuckComponents(component, self.AllDuckTypeLayout)
        Clock.schedule_once(self.UpdateLabel, 0.1)


    def build(self):
        '''
        This is main function called by Kivy Framework at start of application to register root widget to be drawn by kivy.
        '''
        self.title = 'SimUDuck'

        CollectionsManager.loadCollections()
        
        btn_new = Button(text='New', on_press=self.btnCbk_new, size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})
        self.AllControlWidgets.append(btn_new)
        
        btn_save = Button(text='Save', on_press=self.btnCbk_save, size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})
        self.AllControlWidgets.append(btn_save)
        
        btn_escape = Button(text='Escape', on_press=self.btnCbk_escape, size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})
        self.AllControlWidgets.append(btn_escape)

        dropdown_addNewDuck = DropDown()
        self.AllControlWidgets.append(dropdown_addNewDuck)
        for OneDuckTypeName in CollectionsManager.getAllDuckTypes():
            btn = Button(text=OneDuckTypeName, on_press=self.btnCbk_addNewDuck, size_hint_y=None)
            dropdown_addNewDuck.add_widget(btn)
            self.AllControlWidgets.append(btn)
        btn_addNewDuck = Button(text='Add a new Duck', on_release=dropdown_addNewDuck.open, size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})
        self.AllControlWidgets.append(btn_addNewDuck)

        dropdown_addNewCoop = DropDown()
        self.AllControlWidgets.append(dropdown_addNewCoop)
        for OneCoopTypeName in CollectionsManager.getAllCoopTypes():
            btn = Button(text=OneCoopTypeName, on_press=self.btnCbk_addNewCoop, size_hint_y=None)
            dropdown_addNewCoop.add_widget(btn)
            self.AllControlWidgets.append(btn)
        btn_addNewCoop = Button(text='Add a new Coop', on_release=dropdown_addNewCoop.open, size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})
        self.AllControlWidgets.append(btn_addNewCoop)
    
        dropdown_setFlyBehavior = DropDown()
        self.AllControlWidgets.append(dropdown_setFlyBehavior)
        for OneDuckFlyBehaviorName in CollectionsManager.getAllDuckFlyBehaviors():
            btn = Button(text=OneDuckFlyBehaviorName, on_press=self.btnCbk_setFlyBehavior, size_hint_y=None)
            dropdown_setFlyBehavior.add_widget(btn)
            self.AllControlWidgets.append(btn)
        btn_setFlyBehavior = Button(text='Set Fly Behavior', on_release=dropdown_setFlyBehavior.open, size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})
        self.AllControlWidgets.append(btn_setFlyBehavior)

        dropdown_setQuackBehavior = DropDown()
        self.AllControlWidgets.append(dropdown_setQuackBehavior)
        for OneDuckQuackBehaviorName in CollectionsManager.getAllDuckQuackBehaviors():
            btn = Button(text=OneDuckQuackBehaviorName, on_press=self.btnCbk_setQuackBehavior, size_hint_y=None)
            dropdown_setQuackBehavior.add_widget(btn)
            self.AllControlWidgets.append(btn)
        btn_setQuackBehavior = Button(text='Set Quack Behavior', on_release=dropdown_setQuackBehavior.open,size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})
        self.AllControlWidgets.append(btn_setQuackBehavior)
        
        dropdown_addDecoration = DropDown()
        self.AllControlWidgets.append(dropdown_addDecoration)
        for OneDuckComponentDecorationName in CollectionsManager.getAllDuckComponentDecorators():
            btn = Button(text=OneDuckComponentDecorationName, color=[0, 0, 0, 1], on_press=self.btnCbk_addDecoration, size_hint_y=None)
            btn.background_color = CollectionsManager.createNewDuckComponentDecorator(OneDuckComponentDecorationName, None).getDuckComponentDecoration()[0]
            dropdown_addDecoration.add_widget(btn)
            self.AllControlWidgets.append(btn)
        btn_addDecoration = Button(text='Add Decoration', on_release=dropdown_addDecoration.open, size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})
        self.AllControlWidgets.append(btn_addDecoration)

        btn_performDuck = Button(text='Perform Duck', on_press=self.btnCbk_performDuck,size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})
        self.AllControlWidgets.append(btn_performDuck)

        btn_removeDuckComponent = Button(text='Remove', on_press=self.btnCbk_removeDuckComponent,size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})
        self.AllControlWidgets.append(btn_removeDuckComponent)

        self.label_totalDucks = Label(text="Total Ducks = 0", color=[0, 0, 0, 1], size_hint=(1, 0.2), halign="left", pos_hint={'top': 1})

        control_layout = BoxLayout(size_hint=(1, None), pos_hint={'top': 1})
        self.AllControlWidgets.append(control_layout)

        control_layout.add_widget(btn_escape)
        control_layout.add_widget(btn_new)
        control_layout.add_widget(btn_save)
        control_layout.add_widget(btn_addNewDuck)
        control_layout.add_widget(btn_addNewCoop)
        control_layout.add_widget(btn_setFlyBehavior)
        control_layout.add_widget(btn_setQuackBehavior)
        control_layout.add_widget(btn_addDecoration)
        control_layout.add_widget(btn_performDuck)
        control_layout.add_widget(btn_removeDuckComponent)
        control_layout.add_widget(self.label_totalDucks)

        self.AllDuckTypeLayout = BoxLayout(id='AllDuckTypeLayout', size_hint=(1, 1), pos_hint={'bottom': 1})

        root = BoxLayout(orientation='vertical', size_hint=(1, 1), pos_hint={'top': 1})
        root.add_widget(control_layout)
        root.add_widget(self.AllDuckTypeLayout)

        self.root = root

        Window.clearcolor = (1, 1, 1, 1)

        self.AllDuckTypeLayout_ChildDuckComponents = CollectionsManager.getDatabase()
        self.redrawAllDuckComponents(None)

        return root

if __name__ == '__main__':
    MyApp().run()