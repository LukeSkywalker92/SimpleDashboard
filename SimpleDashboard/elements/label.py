from .element import Element

class Label(Element):

    def __init__(self, text, *args, tag='span', classes=['uk-label'], **kwargs):
        super().__init__(tag, classes, *args, **kwargs)
        self.html.text = str(text)
