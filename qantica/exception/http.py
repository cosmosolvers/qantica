




class HTTPError(Exception):
    """
    Exception raised for HTTP errors.

    Attributes:
    - status_code -- HTTP status code
    - message -- explanation of the error
    """

    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"HTTP Error {status_code}: {message}")
    
