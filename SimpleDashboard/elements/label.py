from .element import Element

class Label(Element):

    def __init__(self, value, *args, tag='span', classes=['uk-label'], **kwargs):
        super().__init__(tag, classes, *args, **kwargs)
        self.html.text = self._generate_inner_html(value)
