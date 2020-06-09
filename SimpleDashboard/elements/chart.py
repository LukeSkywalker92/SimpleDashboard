from .element import Element

class Chart(Element):

    def __init__(self, x=None, y=[], *args, tag='div', classes=[],
                 mode='lines+markers', title='', persistent=True,
                 xlabel='', ylabel='', **kwargs):
        super().__init__(tag, classes, *args, **kwargs)
        self.persistent = persistent
        self.mode = mode
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.x_start = x
        self.x = x
        self.y = y
        self.__generate_js()

    def __generate_js(self):
        x_js = ''
        x_data_js = ''
        if self.x != None:
            x_js = 'x: ' + str(self.x) + ','
            x_data_js = 'x: [data["x"]],'

        self.js = ('Plotly.newPlot( "' + str(self.id) + '", [{'
	               '' + x_js + ''
	               'y: ' + str(self.y) + ','
                   'mode: "' + self.mode + '",'
                   'title: "' + self.title + '"'
                   ' }], {'
	               'xaxis: { title: "' + self.xlabel + '" },'
                   'yaxis: { title: "' + self.ylabel + '" },'
                   '}, {responsive: true} );'
                   'socket.on("'+str(self.id)+'_update",'
                   'function(data){'
                   'Plotly.extendTraces("'+str(self.id)+'", {'
                   '' + x_data_js + ''
                   'y: [data["y"]]'
                   '}, [0])});'
                   'socket.on("'+str(self.id)+'_clear",'
                   'function(){'
                   'Plotly.newPlot( "' + str(self.id) + '", [{'
           	       '' + x_js + ''
           	       'y: ' + str(self.y) + ','
                   'mode: "' + self.mode + '",'
                   'title: "' + self.title + '"'
                   ' }], {'
           	       'xaxis: { title: "' + self.xlabel + '" },'
                   'yaxis: { title: "' + self.ylabel + '" },'
                   '}, {responsive: true} );'
                   '});')

    def update(self, x=[], y=[]):
        if isinstance(x, list) is False:
            x = [x]
        if y == []:
            y=x
        if isinstance(y, list) is False:
            y = [y]
        if self.persistent:
            if self.x is not None:
                self.x.append(x[0])
            self.y.append(y[0])
        self.socketio.emit(str(self.id)+'_update', {'x': x, 'y': y})
        self.__generate_js()

    def clear(self):
        self.x = self.x_start
        self.y = []
        self.__generate_js()
        self.socketio.emit(str(self.id)+'_clear')
