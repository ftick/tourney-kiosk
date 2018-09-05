import cherrypy

class Routes(object):

    NULL_STRING = 'null'

    class _Root(object):
        @cherrypy.expose
        def index(self):
            return """<html>
              <head></head>
              <body>
                <p>Nothing Yet...</p>
              </body>
            </html>"""

        @cherrypy.expose
        def signup(self):
            return """<html>
                <head></head>
                <body>
                <p>""" + str(cherrypy.request.app.config['kiosk'])+ """</p>
                </body>
            </html>"""

    @cherrypy.expose
    class _Ajax(object):
        @cherrypy.tools.accept(media='text/plain')
        def GET(self):
            return NULL_STRING

        def POST(self, post=""):
            return NULL_STRING

        def PUT(self, put=""):
            return NULL_STRING

        def DELETE(self):
            return NULL_STRING

    @cherrypy.expose
    class _AjaxNameSearch(object):
        @cherrypy.tools.accept(media='text/plain')
        def GET(self):
            return NULL_STRING

        def POST(self, post=""):
            return "test 'post'=='" + post + "'"

        def PUT(self, put=""):
            return NULL_STRING

        def DELETE(self):
            return NULL_STRING