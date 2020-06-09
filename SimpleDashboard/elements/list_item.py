from .element import Element

class ListItem(Element):

    def __init__(self, *args, tag='li', classes=[], **kwargs):
        super().__init__(tag, classes, *args, **kwargs)
