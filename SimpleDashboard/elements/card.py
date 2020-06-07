from .element import Element

class Card(Element):

    def __init__(self, *args, tag='div', classes=['uk-card', 'uk-card-default', 'uk-card-body'], **kwargs):
        super().__init__(tag, classes, *args, **kwargs)
