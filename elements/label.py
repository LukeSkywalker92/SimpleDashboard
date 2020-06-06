from .element import Element

class Label(Element):

    def __init__(self, text):
        super().__init__()
        self.html = '<p id='+str(self.id)+'>' + str(text) + '</p>'
