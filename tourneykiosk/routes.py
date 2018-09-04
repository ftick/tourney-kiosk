import cherrypy

class Routes(object):
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
            return "AJAX GET"

        def POST(self, post=""):
            return "AJAX POST"

        def POST(self, put=""):
            return "AJAX PUT"

        def DELETE(self):
            return "AJAX DELETE"

    @cherrypy.expose
    class _AjaxNameSearch(object):
        @cherrypy.tools.accept(media='text/plain')
        def GET(self):
            return "test get"

        def POST(self, post=""):
            return "test 'post'=='" + post + "'"

        def POST(self, put=""):
            return "test 'put'=='" + put + "'"

        def DELETE(self):
            return "test delete"