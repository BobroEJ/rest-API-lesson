import os
from utils.requests_helper import BaseSession


# def cats() -> BaseSession:
#     cats_url = os.getenv('cats_api')
#     return BaseSession(base_url=cats_url)
def cats() -> BaseSession:
    cats_url = 'https://catfact.ninja'
    return BaseSession(base_url=cats_url)
