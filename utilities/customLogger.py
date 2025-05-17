import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        Logs_dir = os.path.abspath(os.curdir) + '\\logs'
        os.makedirs(Logs_dir, exist_ok=True)
        path = os.path.join(Logs_dir, "logfile.log")
        # Create a file handler 
        file_handler = logging.FileHandler(path)
        # Create a logging formatter
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # Add the formatter to the handler
        file_handler.setFormatter(formatter)
        # Create a logger
        logger = logging.getLogger()
        # Set the logging level 
        logger.setLevel(logging.DEBUG)
        # Add the file handler to the logger
        logger.addHandler(file_handler)
        # Add a stream handler to log to console
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        # Log a message
        logger.info("Logging setup complete.")
        # Return the logger
        return logger