#!/usr/bin/env python3
"""
Module for filtering log messages by redacting sensitive information.
"""

import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Replaces sensitive fields with a redaction string."""
    for f in fields:
        pattern = rf"{re.escape(f)}=[^ {re.escape(separator)}]*"
        message = re.sub(pattern, f"{f}={redaction}", message)
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
