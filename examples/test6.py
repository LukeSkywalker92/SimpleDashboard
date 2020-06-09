from SimpleDashboard import Dashboard
from SimpleDashboard.elements import *
from SimpleDashboard.tools import Poller
from random import random

dashboard = Dashboard()

append_card = Card( width='1-2')
append_card_title = CardTitle('Append Chart')
append_chart = Chart(xlabel='X Label', ylabel='Y Label')
append_paragraph = Paragraph('')

def update_chart():
    y = random()
    append_chart.update(y=y)
    append_paragraph.update(y)

append_button = Button('Append Chart', update_chart)
clear_button = Button('Clear Chart', append_chart.clear)

append_card.append_child(append_card_title)
append_card.append_child(append_paragraph)
append_card.append_child(append_chart)
append_card.append_child(append_button)
append_card.append_child(clear_button)
dashboard.add_element(append_card)

poll_card = Card( width='1-2')

poll_card_title = CardTitle('Poll Chart')
poll_chart = Chart(x=[], y=[], mode='markers', xlabel='X Label', ylabel='Y Label')
poll_paragraph = Paragraph('')

def stream_chart():
    x = random()
    y = random()
    return x, y

poller = Poller(stream_chart, poll_chart, poll_paragraph)

poll_button = Button('Start Poller', poller.start)
poll_stop_button = Button('Stop Poller', poller.stop)
poll_clear_button = Button('Clear Chart', poll_chart.clear)

poll_card.append_child(poll_card_title)
poll_card.append_child(poll_paragraph)
poll_card.append_child(poll_chart)
poll_card.append_child(poll_button)
poll_card.append_child(poll_stop_button)
poll_card.append_child(poll_clear_button)
dashboard.add_element(poll_card)


dashboard.run()
