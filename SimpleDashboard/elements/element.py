import xml.etree.ElementTree as ET
import copy
import base64

class Element():

    def __init__(self, tag, classes, *args, width='1-1', unit=None, digits=None, **kwargs):
        self.id = id(self)
        self.string_id = base64.b32encode(str(self.id).encode()).decode()
        self.tag = copy.copy(tag)
        self.classes = copy.copy(classes)
        self.classes.append('uk-width-'+width)
        self.unit = unit
        self.digits = digits
        self.children = []
        self.et = ET
        self.socketio = None
        self.registered = False
        self.html = self.et.Element(self.tag, attrib={'id': str(self.id), 'class': ' '.join(self.classes)})
        self.js = 'socket.on("'+str(self.id)+'_update", function(data){document.getElementById("'+str(self.id)+'").innerHTML=data});'

    def register(self, socketio):
        if socketio is not None:
            if self.registered is False:
                self.socketio = socketio
                self._on_register()
                self.registered = True
            for child in self.children:
                child.register(self.socketio)

    def _on_register(self):
        pass

    def _add_event_listener(self, event, callback):
        self.js += 'document.getElementById("'+str(self.id)+'").addEventListener("'+ str(event) +'", function() {socket.emit("'+str(self.id)+'_'+event+'")});'
        self.socketio.on_event(str(self.id)+'_'+str(event), callback)

    def _generate_inner_html(self, value):
        if isinstance(value, str):
            return value
        elif isinstance(value, int) or isinstance(value, float):
            return_value = value
            if self.digits is not None:
                return_value = round(return_value, self.digits)
            return_value = str(return_value)
            if self.unit is not None:
                return_value += ' ' + self.unit
            return return_value
        else:
            return str(value)


    def update(self, value):
        inner_html = self._generate_inner_html(value)
        self.html.text = inner_html
        self.socketio.emit(str(self.id)+'_update', inner_html)

    def append_child(self, child):
        self.children.append(child)
        child.register(self.socketio)
        self.html.append(child.html)

    def get_html(self):
        return self.et.tostring(self.html, encoding='utf8', method='html').decode('UTF-8')

    def get_element(self):
        return self.html

    def get_js(self):
        js = copy.copy(self.js)
        for child in self.children:
            js += child.get_js() + '\n'
        return js
