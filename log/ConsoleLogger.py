from log.Logger import Logger


class ConsoleLogger(Logger):
    def emit_message(self, data):
        print(data)
