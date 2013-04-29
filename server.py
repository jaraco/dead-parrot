import os
import uuid
import json

import cherrypy

class DeadParrot(object):
    """
    http://www.youtube.com/watch?v=4vuW6tQ0218

    A server that just parrots back the content you send to it.
    """

    data = {}
    exposed = True

    def POST(self):
        slug = uuid.uuid4()
        data = dict(
            content=cherrypy.request.body.read(),
            type=cherrypy.request.headers['Content-Type'],
        )
        self.data[unicode(slug)] = data
        url = cherrypy.url('/{slug}'.format(slug=slug))
        cherrypy.request.headers['Access-Control-Allow-Origin'] = '*'
        return json.dumps(dict(url=url))

    def GET(self, slug):
        if not slug in self.data:
            raise cherrypy.NotFound()
        data = self.data.pop(slug)
        cherrypy.response.headers['Content-Type'] = data['type']
        return data['content']

    @classmethod
    def helloooooo(cls):
        config = {
            'global': {
                'server.socket_host': '::0',
                'server.socket_port': int(os.environ.get('PORT', 8080)),
                'environment': 'production',
            },
            '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tools.decode.on': False,
            },
        }
        cherrypy.quickstart(cls(), config=config)

if __name__ == '__main__':
    DeadParrot.helloooooo()
