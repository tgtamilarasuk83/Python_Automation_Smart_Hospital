import logging
import os
import sys


def get_logger():
    log_dir = "./Logs"
    os.makedirs(log_dir, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("./Logs/log_report.log", mode="a"),
            logging.StreamHandler(sys.stdout)
        ],
        force=True
    )

    return logging.getLogger("FrameworkLogger")