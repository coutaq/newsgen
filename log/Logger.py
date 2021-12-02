from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def emit_message(self, data):
        pass
