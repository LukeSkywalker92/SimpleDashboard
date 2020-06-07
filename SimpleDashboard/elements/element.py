import xml.etree.ElementTree as ET

class Element():

    def __init__(self):
        self.id = id(self)
        self.et = ET
        self.html = ''
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
        self.html.text = text
        self.socketio.emit(str(self.id)+'_update', str(html))

    def get_html(self):
        return self.et.tostring(self.html, encoding='utf8', method='html').decode('UTF-8')

    def get_element(self):
        return self.html

    def get_js(self):
        return self.js