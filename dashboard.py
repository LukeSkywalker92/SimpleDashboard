from flask import Flask, render_template
from flask_socketio import SocketIO

class Dashboard():
    def __init__(self):
        self.app = Flask(__name__)
        #app.config['SECRET_KEY'] = 'secret!'
        self.socketio = SocketIO(self.app)
        self.elements = []
        self.scripts = []
        self.scripts.append('https://cdn.jsdelivr.net/npm/socket.io-client@2/dist/socket.io.js')
        @self.app.route('/')
        def hello_world():
            return render_template('main.html', content=self.generate_html())

    def run(self):
        self.socketio.run(self.app)

    def add_element(self, element):
        element.register(self.socketio)
        self.elements.append(element)

    def add_script(self, script):
        self.scripts.append(script)

    def generate_html(self):
        html = ''
        scripts = ['<script src="'+script+'"></script>' for script in self.scripts]
        for element in self.elements:
            html += element.get_html()
        for script in scripts:
            html += script
        html += '<script>'
        html += '(function() {'
        html += 'var socket = io();'
        for element in self.elements:
            html += element.get_js() + '\n'
        html += '})();'
        html += '</script>'
        return html
