import logging
import threading

class LoggerSingleton:
    _instance = None
    _lock = threading.Lock() 

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(LoggerSingleton, cls).__new__(cls)
                cls._instance._initialize_logger()
            return cls._instance

    def _initialize_logger(self):
        self.logger = logging.getLogger("SingletonLogger")
        self.logger.setLevel(logging.DEBUG)
        if not self.logger.handlers:
            handler = logging.FileHandler("singleton_log.log")
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def log(self, message, level=logging.INFO):
        if level == logging.DEBUG:
            self.logger.debug(message)
        elif level == logging.WARNING:
            self.logger.warning(message)
        elif level == logging.ERROR:
            self.logger.error(message)
        else:
            self.logger.info(message)

logger1 = LoggerSingleton()
logger1.log("This is an info message.")

logger2 = LoggerSingleton()
logger2.log("This is a warning message.", level=logging.WARNING)

print(logger1 is logger2)