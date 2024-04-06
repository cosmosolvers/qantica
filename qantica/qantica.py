from flask import Flask
from typing import Dict, List, Tuple

    
class QApplication:
    
    def __init__(self, settings: Dict) -> None:
        self._app = Flask(__name__)
        self.settings(settings)
    
    def settings(self, settings: Dict):
        self._app.config.update(settings)
    
    def Routers(self, routers: Tuple):
        """
        (
            ('/home/<str:pk>', {'GET': home, 'POST': home_post}),
            ('/about', {'POST': about_post}),
            ('/contact/<int:pk>', {'PUT': contact, 'DELETE': contact}),
            ('/services/<path:subpath>', {'GET': services})
        )
        """
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




class Qantica:
    
    def __init__(self) -> None:
        pass
    


Qantica = Qantica()
