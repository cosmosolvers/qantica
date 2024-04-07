from flask import Flask
from flask_cors import CORS
from typing import Dict, List, Tuple

    
class Qantica:
    
    def __init__(self) -> None:
        self._app = Flask(__name__)
    
    def settings(self, settings: Dict):
        self._app.config.update(settings)
        self.cors = CORS(self._app, origins='*')
    
    def Routers(self, routers: Tuple[str, Dict[str, callable]]):
        """
        (
            ('/home/<str:pk>', {'GET': home, 'POST': home_post}),
            ('/about', {'POST': about_post}),
            ('/contact/<int:pk>', {'PUT': contact, 'DELETE': contact}),
            ('/services/<path:subpath>', {'GET': services})
        )
        """
        # strict_slashes=False
        self._app.url_map.strict_slashes = False
        for router in routers:
            for method, func in router[1].items():
                self._app.add_url_rule(router[0], view_func=func, methods=[method])
    
    @property
    def app(self):
        return self._app
    
    @property
    def config(self):
        return self._app.config
    
    @property
    def run(self):
        self._app.run()

