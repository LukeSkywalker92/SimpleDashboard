from .element import Element

class Button(Element):

    def __init__(self, text, callback):
        super().__init__()
        self.tag = 'button'
        self.classes = ['uk-button', 'uk-button-default']
        self.html = self.et.Element(self.tag, attrib={'id': str(self.id), 'class': ' '.join(self.classes)})
        self.html.text = text
        self.callback = callback

    def _on_register(self):
        self._add_event_listener('click', self.callback)
