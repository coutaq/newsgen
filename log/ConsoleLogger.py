from log.Logger import Logger


class ConsoleLogger(Logger):
    def emit_message(self, data: str) -> None:
        print(data, flush=True)
