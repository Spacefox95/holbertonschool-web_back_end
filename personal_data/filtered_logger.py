#!/usr/bin/env python3
"""
Function to filter the message
"""

import logging
import os
import re
import mysql.connector
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_db():
    """ Returns a SQL database connection"""
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Replaces sensitive fields with a redaction string."""
    for f in fields:
        message = re.sub(f + "=.*?" + separator,
                         f + "=" + redaction + separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class for log messages."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize formatter with fields to redact."""
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter the values in incoming log records."""
        redacted_message = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        record.msg = redacted_message
        return super().format(record)


def get_logger() -> logging.Logger:
    "Creates and returns a logger named 'user_data"
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    strean_handler = logging.StreamHandler()
    strean_handler.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(strean_handler)

    return logger
