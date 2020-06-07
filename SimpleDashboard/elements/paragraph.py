from .element import Element

class Paragraph(Element):

    def __init__(self, text, *args, tag='p', classes=[], **kwargs):
        super().__init__(tag, classes, *args, **kwargs)
        self.html.text = str(text)
