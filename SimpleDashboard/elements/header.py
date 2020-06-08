from .element import Element

class Header(Element):

    def __init__(self, value, *args, tag='h1', classes=[], **kwargs):
        super().__init__(tag, classes, *args, **kwargs)
        self.html.text = self._generate_inner_html(value)
