from flask import Flask, render_template
from flask_socketio import SocketIO
import xml.etree.ElementTree as ET

class Dashboard():
    def __init__(self, title='SimpleDashboard'):
        self.app = Flask(__name__)
        #app.config['SECRET_KEY'] = 'secret!'
        self.socketio = SocketIO(self.app)
        self.elements = []
        self.title=title
        @self.app.route('/')
        def home():
            return render_template('main.html',
                                   title=self.title,
                                   content=self.generate_html(),
                                   js=self.generate_js())

    def run(self):
        self.socketio.run(self.app)

    def add_element(self, element):
        element.register(self.socketio)
        self.elements.append(element)

    def add_script(self, script):
        self.scripts.append(script)

    def generate_html(self):
        et = ET.Element('uk-grid',attrib={'class': 'uk-grid uk-child-width-expand@s uk-text-center uk-grid-medium'})
        for element in self.elements:
            et.append(element.get_element())
        return ET.tostring(et, encoding='utf8', method='html').decode('UTF-8')

    def generate_js(self):
        js = ''
        for element in self.elements:
            js += element.get_js() + '\n'
        return js
