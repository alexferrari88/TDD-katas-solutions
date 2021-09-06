from abc import ABC, abstractmethod


class IWebservice(ABC):
    """IWebservice provides an interface for a web service"""

    @abstractmethod
    def notify(self, msg: str) -> None:
        """notify receives the message to send to the web service"""


class Webservice(IWebservice):
    """Web service class"""

    def notify(self, msg: str) -> str:
        """notify receives the message to send to the web service"""
        return "200 OK"