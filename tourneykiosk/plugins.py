import cherrypy
from cherrypy.process import wspbus, plugins
from braacket import Braacket

class BraacketPlugin(plugins.SimplePlugin):
    def __init__(self, bus, league):
        plugins.SimplePlugin.__init__(self, bus)
        self.braacket = Braacket(league)

    def start(self):
        self.bus.log('Starting up Braacket Plugin')
        self.bus.subscribe("braacket-search", self.search)

    def stop(self):
        self.bus.log('Stopping Braacket Plugin')
        self.bus.unsubscribe("braacket-search", self.search)

    def search(self, name):
        return self.braacket.player_search(name)