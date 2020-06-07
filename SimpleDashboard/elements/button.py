from .element import Element

class Button(Element):

    def __init__(self, text, callback, *args, tag='button', classes=['uk-button', 'uk-button-default'], **kwargs):
        super().__init__(tag, classes, *args, **kwargs)
        self.html.text = text
        self.callback = callback

    def _on_register(self):
        self._add_event_listener('click', self.callback)
