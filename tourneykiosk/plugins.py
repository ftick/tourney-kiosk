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
        self.bus.subscribe("braacket-stats", self.stats)

    def stop(self):
        self.bus.log('Stopping Braacket Plugin')
        self.bus.unsubscribe("braacket-search", self.search)
        self.bus.unsubscribe("braacket-stats", self.stats)

    def search(self, name):
        return self.braacket.player_search(name)

    def stats(self, uuid):
        ret_obj = self.braacket.player_stats(uuid)
        ret_obj['provider'] = "Braacket.com"
        return ret_obj