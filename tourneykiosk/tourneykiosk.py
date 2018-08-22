import cherrypy
import random
import string
from enum import Enum

# ----- enums 

class BracketType(Enum):
    CHALLONGE = 1
    BRAACKET = 2
    SMASHGG = 3

class PlayerBankType(Enum):
    BRAACKET = 1

class TourneyKiosk():
    def __init__(self, tourney_vars, playerbank_vars,
            tourney_type=BracketType.CHALLONGE, 
            playerbank_type=PlayerBankType.BRAACKET):
        self._tourney_type = tourney_type
        self._tourney_vars = tourney_vars
        self._playerbank_type = playerbank_type
        self._playerbank_vars = playerbank_vars

    # ----- server stuff

    class HelloWorld(object):
        @cherrypy.expose
        def index(self):
            return """<html>
              <head></head>
              <body>
                <form method="get" action="generate">
                  <input type="text" value="" name="saved_val" />
                  <button type="submit">Give it now!</button>
                </form>
              </body>
            </html>"""

        @cherrypy.expose
        def generate(self, saved_val=None):
            if saved_val is not None:
                cherrypy.session['saved_val'] = saved_val
            if 'saved_val' not in cherrypy.session:
                return 'no saved_val yet!'
            return 'current saved val: ' + cherrypy.session['saved_val']

    conf = {
        '/': {
            'tools.sessions.on': True
        }
    }
    cherrypy.quickstart(HelloWorld(), '/', conf)