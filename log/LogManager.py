from typing import List

from log.Logger import  Logger


class LogManager:
    _loggers: List[Logger] = []

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LogManager, cls).__new__(cls)
        return cls.instance

    def attach(self, logger: Logger):
        self._loggers.append(logger)

    def detach(self, logger: Logger):
        self._loggers.remove(logger)

    def notify(self, data):
        for logger in self._loggers:
            logger.emit_message(data)
