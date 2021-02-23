class RAM_Exception(Exception):
    def __init__(self,status_code):
        message = f"Status code was {status_code}"
        super().__init__(message)