from SimpleDashboard import Dashboard
from SimpleDashboard.elements import Label, Button

dashboard = Dashboard()

def callback():
    print('Button pressed')

label = Label('Label')
button = Button('Button', callback)

dashboard.add_element(label)
dashboard.add_element(button)

dashboard.run()
