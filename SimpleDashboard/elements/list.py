from .element import Element

class List(Element):

    def __init__(self, *args, tag='ul', classes=['uk-list'], **kwargs):
        super().__init__(tag, classes, *args, **kwargs)
