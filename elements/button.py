from .element import Element

class Button(Element):

    def __init__(self, text, callback):
        super().__init__()
        self.html = '<button id='+str(self.id)+'>' + str(text) + '</button>'
        self.callback = callback
        
    def _on_register(self):
        self._add_event_listener('click', self.callback)
