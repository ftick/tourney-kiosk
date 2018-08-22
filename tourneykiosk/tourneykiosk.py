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

    class Root(object):
        @cherrypy.expose
        def index(self):
            return """<html>
              <head></head>
              <body>
                <p>Nothing Yet...</p>
              </body>
            </html>"""

    # ----- start server

    conf = {
        '/': {
            'tools.sessions.on': True
        }
    }
    cherrypy.quickstart(Root(), '/', conf)