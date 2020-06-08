import eventlet

class Poller():

    def __init__(self, function, element, interval=1):
        self.function = function
        self.element = element
        self.interval = interval
        self.active = False
        self.thread = None

    def poll(self):
        while True:
            self.element.update(*(self.function()))
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
