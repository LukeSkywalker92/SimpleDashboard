from .element import Element

class CardTitle(Element):

    def __init__(self, value, *args, tag='h3', classes=['uk-card-title'], **kwargs):
        super().__init__(tag, classes, *args, **kwargs)
        self.html.text = self._generate_inner_html(value)
