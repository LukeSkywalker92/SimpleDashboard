import xml.etree.ElementTree as ET
import copy

class Element():

    def __init__(self, tag, classes, *args, width='1-1', **kwargs):
        self.id = id(self)
        self.tag = copy.copy(tag)
        self.classes = copy.copy(classes)
        self.classes.append('uk-width-'+width)
        self.children = []
        self.et = ET
        self.html = self.et.Element(self.tag, attrib={'id': str(self.id), 'class': ' '.join(self.classes)})
        self.js = 'socket.on("'+str(self.id)+'_update", function(data){document.getElementById("'+str(self.id)+'").innerHTML=data});'

    def register(self, socketio):
        self.socketio = socketio
        self._on_register()

    def _on_register(self):
        pass

    def _add_event_listener(self, event, callback):
        self.js += 'document.getElementById("'+str(self.id)+'").addEventListener("'+ str(event) +'", function() {socket.emit("'+str(self.id)+'_'+event+'")});'
        self.socketio.on_event(str(self.id)+'_'+str(event), callback)

    def update_inner_html(self, text):
        self.html.text = str(text)
        self.socketio.emit(str(self.id)+'_update', str(text))
        print(text)

    def append_child(self, child):
        self.children.append(child)
        child.register(self.socketio)

    def get_html(self):
        et = self.html
        for child in self.children:
            et.append(child.html)
        return self.et.tostring(et, encoding='utf8', method='html').decode('UTF-8')

    def get_element(self):
        et = copy.copy(self.html)
        for child in self.children:
            et.append(child.html)
        return et

    def get_js(self):
        js = copy.copy(self.js)
        for child in self.children:
            js += child.get_js() + '\n'
        return js
