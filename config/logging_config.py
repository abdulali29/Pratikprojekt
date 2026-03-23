# logging_config.py

import logging


def setup_logging():
    """
    Configure global logging for the application.
    Logs are written to both console and file.
    """

    logging.basicConfig(
        level=logging.INFO,  # Log INFO and above
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        handlers=[
            logging.StreamHandler(),              # Console output
            logging.FileHandler("app.log")        # Log file
        ]
    )

    logging.info("Logging initialized successfully.")