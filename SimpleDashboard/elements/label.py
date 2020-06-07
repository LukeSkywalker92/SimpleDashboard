from .element import Element

class Label(Element):

    def __init__(self, text):
        super().__init__()
        self.tag = 'span'
        self.classes = ['uk-label']
        self.html = self.et.Element(self.tag, attrib={'id': str(self.id), 'class': ' '.join(self.classes)})
        self.html.text = str(text)
