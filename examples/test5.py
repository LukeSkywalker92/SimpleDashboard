from SimpleDashboard import Dashboard
from SimpleDashboard.elements import *
from SimpleDashboard.tools import Poller
import time
import eventlet
from random import random

dashboard = Dashboard()


def rand():
    return random()

card = Card(width='1-3')
dashboard.add_element(card)
card_title = CardTitle('Title ')
paragraph = Paragraph(0, digits=3, unit='kg')

poller = Poller(rand, paragraph)

button = Button('Button ', poller.start)
card.append_child(card_title)
card.append_child(paragraph)
card.append_child(button)



dashboard.run()
