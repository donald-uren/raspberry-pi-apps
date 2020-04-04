from abc import ABC, abstractmethod


class Application(ABC):
    """
    Simple abstract class for use in Task A & B: each of these implement the below methods
    """

    @abstractmethod
    def run(self):
        ...

    @abstractmethod
    def terminate(self):
        ...
