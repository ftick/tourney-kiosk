import cherrypy
import random
import string
import os 
from .routes import Routes
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
        # ----- start server
        conf = {
            '/': {
                'tools.sessions.on': True,
                'tools.staticdir.root': os.path.abspath(os.getcwd())
            },
            '/ajax': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tools.response_headers.on': True,
                'tools.response_headers.headers': [('Content-Type', 'text/plain')],
            },
            '/ajax/namesearch': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tools.response_headers.on': True,
                'tools.response_headers.headers': [('Content-Type', 'text/plain')],
            },
            '/static': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'public'
            },
            'kiosk': {
                'tourney_type': tourney_type,
                'tourney_vars': tourney_vars,
                'playerbank_type': playerbank_type,
                'playerbank_vars': playerbank_vars
            }
        }
        webapp = Routes._Root()
        webapp.ajax = Routes._Ajax()
        webapp.ajax.namesearch = Routes._AjaxNameSearch()
        cherrypy.quickstart(webapp, '/', conf)
