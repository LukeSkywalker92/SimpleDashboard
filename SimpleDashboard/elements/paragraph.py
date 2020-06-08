from .element import Element

class Paragraph(Element):

    def __init__(self, value, *args, tag='p', classes=[], **kwargs):
        super().__init__(tag, classes, *args, **kwargs)
        self.html.text = self._generate_inner_html(value)
