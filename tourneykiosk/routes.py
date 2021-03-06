import cherrypy
import json

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
            result = cherrypy.engine.publish("braacket-search", name).pop()
            return json.dumps(result)

        def PUT(self):
            return Routes.NULL_STRING

        def DELETE(self):
            return Routes.NULL_STRING

    @cherrypy.expose
    class _AjaxPlayerStats(object):
        @cherrypy.tools.accept(media='text/plain')
        def GET(self):
            return Routes.NULL_STRING

        def POST(self, uuid=""):
            result = cherrypy.engine.publish("braacket-stats", uuid).pop()
            return json.dumps(result)

        def PUT(self):
            return Routes.NULL_STRING

        def DELETE(self):
            return Routes.NULL_STRING