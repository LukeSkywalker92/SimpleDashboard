from SimpleDashboard import Dashboard
from SimpleDashboard.elements import *

dashboard = Dashboard()

def callback():
    print('Button pressed')

def callback2():
    print('Button2 pressed')

label = Label('Label')
button = Button('Button', callback)


card = Card(width='1-3')
dashboard.add_element(card)
card_title = CardTitle('Title')
paragraph = Paragraph('Text')
card.append_child(card_title)
card.append_child(paragraph)
#card.append_child(label)
card.append_child(button)


label2 = Label('Label')
button2 = Button('Button', callback2)
card2 = Card(width='1-3')
dashboard.add_element(card2)
card_title2 = CardTitle('Title')
paragraph2 = Paragraph('Text')
card2.append_child(card_title2)
card2.append_child(paragraph2)
#card.append_child(label)
card2.append_child(button2)



dashboard.run()
