from flask import Flask, render_template
from flask_socketio import SocketIO
import xml.etree.ElementTree as ET
from .elements import Grid

class Dashboard():
    
    def __init__(self, title='SimpleDashboard', host='127.0.0.1', port=5000):
        self.app = Flask(__name__)
        #app.config['SECRET_KEY'] = 'secret!'
        self.socketio = SocketIO(self.app, async_mode='eventlet')
        self.grid = Grid()
        self.grid.register(self.socketio)
        self.elements = []
        self.title=title
        self.host = host
        self.port = port
        @self.app.route('/')
        def home():
            return render_template('main.html',
                                   title=self.title,
                                   content=self.generate_html(),
                                   js=self.generate_js())

    def run(self):
        self.grid.register(self.socketio)
        self.socketio.run(self.app, self.host, self.port)

    def add_element(self, element):
        self.grid.append_child(element)

    def add_script(self, script):
        self.scripts.append(script)

    def generate_html(self):
        return self.grid.get_html()

    def generate_js(self):
        return self.grid.get_js()
