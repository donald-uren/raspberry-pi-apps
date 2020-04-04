from abc import ABC, abstractmethod


class Application(ABC):

    @abstractmethod
    def run(self):
        ...

    @abstractmethod
    def terminate(self):
        ...
