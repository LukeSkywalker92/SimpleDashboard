from SimpleDashboard import Dashboard
from SimpleDashboard.elements import *

dashboard = Dashboard()

def callback():
    print('Button pressed')

def callback2():
    print('Button2 pressed')

for i in range(9):
    def callback():
        print('Button' + str(i) + 'pressed')
    card = Card(width='1-3')
    dashboard.add_element(card)
    card_title = CardTitle('Title '+ str(i))
    paragraph = Paragraph('Text '+ str(i))
    button = Button('Button ' + str(i), callback)
    card.append_child(card_title)
    card.append_child(paragraph)
    card.append_child(button)

dashboard.run()
