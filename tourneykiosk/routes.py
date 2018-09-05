import cherrypy

class Routes(object):

    NULL_STRING = 'null'

    class _Root(object):
        @cherrypy.expose
        def index(self):
            return """<html>
                <head>
                    <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js?ver=3.3.1"></script>
                    <script src="static/main.js"></script>
                </head>
                    <body>
                        <form action="/ajax/namesearch" method="post">
                            name: <input id="name_search_input" type="text" name="name">
                        </form>
                        <div id="log_area" style="width:260px;background-color:#ccc;font-family:monospace">
                            test
                        </div>
                    </body>
                </html>"""

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