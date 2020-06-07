from .element import Element

class CardTitle(Element):

    def __init__(self, text, *args, tag='h3', classes=['uk-card-title'], **kwargs):
        super().__init__(tag, classes, *args, **kwargs)
        self.html.text = str(text)
