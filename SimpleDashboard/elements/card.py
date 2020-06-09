from .element import Element
from .card_title import CardTitle

class Card(Element):

    def __init__(self, *args, title=None, tag='div', classes=['uk-card', 'uk-card-default', 'uk-card-body'], **kwargs):
        super().__init__(tag, classes, *args, **kwargs)
        if title is not None:
            self.card_title = CardTitle(title)
            self.append_child(self.card_title)
