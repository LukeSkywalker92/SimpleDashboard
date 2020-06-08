from SimpleDashboard import Dashboard
from SimpleDashboard.elements import *
import time
import eventlet
from random import random

dashboard = Dashboard()

def thread_func(paragraph):
    while True:
        paragraph[0].update_inner_html(str(round(random(),4)))

        eventlet.sleep(1)


card = Card(width='1-3')
dashboard.add_element(card)
card_title = CardTitle('Title ')
paragraph = Paragraph('Text ')

def callback():
    eventlet.greenthread.spawn(thread_func, (paragraph, ))

button = Button('Button ', callback)
card.append_child(card_title)
card.append_child(paragraph)
card.append_child(button)

dashboard.run()
