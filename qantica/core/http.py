import requests
from PIL import Image
from io import BytesIO

from flask import request

from ..exception.http import HTTPError



class HTTP:
    def __init__(self, method, **kwargs) -> None:
        """
        :param kwargs:
        - url: str
        - headers: dict
        - params: dict
        - data: dict
        - json: dict
        - timeout: int
        - allow_redirects: bool
        - proxies: dict
        - verify: bool
        - cert: tuple
        - cookies: dict
        - hooks: dict
        - stream: bool
        - auth: tuple
        - files: dict
        """
        try:
            self.response = requests.request(method, **kwargs)
        except requests.exceptions.RequestException as e:
            raise HTTPError(self.status_code, e)
    
    @property
    def status_code(self):
        return self.response.status_code
    
    @property
    def headers(self):
        return self.response.headers
    
    @property
    def text(self):
        return self.response.text
    
    @property
    def content(self):
        return self.response.content
    
    @property
    def json(self):
        return self.response.json()
    
    @property
    def cookies(self):
        return self.response.cookies
    
    @property
    def url(self):
        return self.response.url
    
    @property
    def encoding(self):
        return self.response.encoding
    
    @property
    def image(self):
        return Image.open(BytesIO(self.content))
    
    @staticmethod
    def Session():
        return requests.Session()



class Request:

    request = None
    user = None
    method = None
    args = None
    form = None
    json = None
    files = None
    cookies = None
    headers = None
    environ = None
    url = None
    path = None
    full_path = None
    script_root = None
    base_url = None
    url_root = None
    blueprint = None
    endpoint = None
    view_args = None
    data = None
    _cached_json = None
    _cached_data = None
    _cached_form = None
    _cached_files = None
    _cached_args = None
    _cached_cookies = None
    _cached_headers = None
    _cached_method = None
    _cached_url = None
    _cached_path = None
    _cached_full_path = None
    _cached_script_root = None
    _cached_base_url = None
    _cached_url_root = None
    _cached_blueprint = None
    _cached_endpoint = None
    _cached_view_args = None
    _cached_environ = None
    _cached_user = None
    _cached_request = None
    _cached_session = None
    _cached_response = None
    _cached_exception = None

    def __init__(self, request) -> None:
        self.request = request
        self.method = request.method
        self.args = request.args
        self.form = request.form
        self.json = request.json
        self.files = request.files
        self.cookies = request.cookies
        self.headers = request.headers
        self.environ = request.environ
        self.url = request.url
        self.path = request.path
        self.full_path = request.full_path
        self.script_root = request.script_root
        self.base_url = request.base_url
        self.url_root = request.url_root
        self.blueprint = request.blueprint
        self.endpoint = request.endpoint
        self.view_args = request.view_args
        self.data = self.form | self.files
        self._cached_json = request._cached_json
        self._cached_data = request._cached_data
        self._cached_form = request._cached_form
        self._cached_files = request._cached_files
        self._cached_args = request._cached_args
        self._cached_cookies = request._cached_cookies
        self._cached_headers = request._cached_headers
        self._cached_method = request._cached_method
        self._cached_url = request._cached_url
        self._cached_path = request._cached_path
        self._cached_full_path = request._cached_full_path
        self._cached_script_root = request._cached_script_root
        self._cached_base_url = request._cached_base_url
        self._cached_url_root = request._cached_url_root
        self._cached_blueprint = request._cached_blueprint
        self._cached_endpoint = request._cached_endpoint
        self._cached_view_args = request._cached_view_args
        self._cached_environ = request._cached_environ
        self._cached_user = request._cached_user
        self._cached_request = request._cached_request
        self._cached_session = request._cached_session
        self._cached_response = request._cached_response
        self._cached_exception = request._cached_exception

        


get = lambda **kwargs: HTTP('GET', **kwargs)
post = lambda **kwargs: HTTP('POST', **kwargs)
put = lambda **kwargs: HTTP('PUT', **kwargs)
delete = lambda **kwargs: HTTP('DELETE', **kwargs)
patch = lambda **kwargs: HTTP('PATCH', **kwargs)
options = lambda **kwargs: HTTP('OPTIONS', **kwargs)
head = lambda **kwargs: HTTP('HEAD', **kwargs)
session = lambda: HTTP.Session()


# with HTTP.session() as session:
#     response = session.get('https://httpbin.org/get')
#     print(response.status_code)
