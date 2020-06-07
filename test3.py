from SimpleDashboard import Dashboard
from SimpleDashboard.elements import *

dashboard = Dashboard()

def callback():
    print('Button pressed')

for i in range(12):
    card = Card(width='1-3')
    dashboard.add_element(card)
    card_title = CardTitle('Title '+ str(i))
    paragraph = Paragraph('Text '+ str(i))
    button = Button('Button ' + str(i), callback)
    card.append_child(card_title)
    card.append_child(paragraph)
    card.append_child(button)

dashboard.run()
