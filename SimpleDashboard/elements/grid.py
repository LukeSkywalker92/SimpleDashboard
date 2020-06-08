from .element import Element

class Grid(Element):

    def __init__(self, *args, tag='uk-grid', classes=['uk-grid uk-child-width-expand@s', 'uk-text-center', 'uk-grid-medium'], **kwargs):
        super().__init__(tag, classes, *args, **kwargs)
