import cherrypy

class Routes(object):

    NULL_STRING = 'null'

    class _Root(object):
        @cherrypy.expose
        def index(self):
            pass

    @cherrypy.expose
    class _Ajax(object):

        @cherrypy.tools.accept(media='text/plain')
        def GET(self):
            return Routes.NULL_STRING

        def POST(self):
            return Routes.NULL_STRING

        def PUT(self):
            return Routes.NULL_STRING

        def DELETE(self):
            return Routes.NULL_STRING

    @cherrypy.expose
    class _AjaxNameSearch(object):
        @cherrypy.tools.accept(media='text/plain')
        def GET(self):
            return Routes.NULL_STRING

        def POST(self, name=""):
            return str(cherrypy.engine.publish("braacket-search", name).pop())

        def PUT(self):
            return Routes.NULL_STRING

        def DELETE(self):
            return Routes.NULL_STRING