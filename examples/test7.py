from SimpleDashboard import Dashboard
from SimpleDashboard.elements import Card

dashboard = Dashboard()

card = Card(title='bla')

dashboard.add_element(card)

dashboard.run()