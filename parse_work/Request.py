from requests import Response, get
from fake_useragent import  UserAgent


class RequestEngine:

    def get_response(self, url: str, params: dict | None) -> Response:
        headers = {'UserAgent': UserAgent(platforms='pc').random }
        responce: Response = get(url = url, params=params,headers=headers)
        return responce
