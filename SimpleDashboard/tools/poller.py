import eventlet

class Poller():

    def __init__(self, function, *elements, interval=1):
        self.function = function
        self.elements = elements
        self.interval = interval
        self.active = False
        self.thread = None

    def poll(self):
        while True:
            value = self.function()
            if isinstance(value, tuple):
                for element in self.elements:
                    element.update(value)
            else:
                for element in self.elements:
                    element.update(value)
            eventlet.sleep(self.interval)

    def start(self):
        if self.active is False:
            self.thread = eventlet.greenthread.spawn(self.poll)
            self.active = True
        else:
            print('Thread already running!')

    def stop(self):
        if self.active:
            self.thread.kill()
            self.active = False
        else:
            print('Thread not running!')
