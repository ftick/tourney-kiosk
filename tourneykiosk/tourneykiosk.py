import cherrypy
import random
import string

      
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


def quickstart():
    conf = {
        '/': {
            'tools.sessions.on': True
        }
    }
    cherrypy.quickstart(HelloWorld(), '/', conf)