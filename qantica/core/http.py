import requests



def get(url, headers=None, params=None):
    return requests.get(url, headers=headers, params=params)


def post(url, headers=None, data=None):
    return requests.post(url, headers=headers, data=data)


def put(url, headers=None, data=None):
    return requests.put(url, headers=headers, data=data)


def delete(url, headers=None, data=None):
    return requests.delete(url, headers=headers, data=data)


def patch(url, headers=None, data=None):
    return requests.patch(url, headers=headers, data=data)


def options(url, headers=None, data=None):
    return requests.options(url, headers=headers, data=data)


def head(url, headers=None, data=None):
    return requests.head(url, headers=headers, data=data)


def connect(url, headers=None, data=None):
    return requests.connect(url, headers=headers, data=data)


def trace(url, headers=None, data=None):
    return requests.trace(url, headers=headers, data=data)


def request(method, url, headers=None, data=None):
    return requests.request(method, url, headers=headers, data=data)


def session():
    return requests.Session()
